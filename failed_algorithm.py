"""
This file only exists, so the `suwudo.py` is not too bloated and I don't loose my progress here.

I'm pretty sure the algorithm that maps the old insults to new ones is NP-Hard.
So the first, naive attempt was to bruteforce all possibilities.
The problem is: there are a **lot**.

Maybe one could improve this algorithm somehow or re-write it in C / Rust to get the optimal mapping
in a reasonable amount of time. Currently, it takes ~1s for 13 possibilities.
That is not bad, but the problem scales exponentially, so it is actually pretty bad.
"""

# Mapping explore constants
import math
from typing import Set, Dict, List

bucket_size = 1
recursive_explore_size = 10

num_buckets = math.ceil(max((len(insult) for insult in all_insults)) / bucket_size + 1)

all_solutions: Set[Dict[int, List[int]]] = set()
already_visited: Set[int] = set()
custom_insults_len = len(custom_insults)

for item in all_insults:
    # Make sure there is at lease one item that *could* fit
    assert any(len(item) // bucket_size >= math.ceil(len(insult) / bucket_size) for insult in custom_insults), \
        f"There are no quotes that fit into {item.decode()!r}. Please adapt the bucket size / custom insults"

from numba import njit


@njit(parallel=True)
def add_packed_num(num: int, new_num: int) -> int:
    nn = num + (new_num << 8 * math.ceil(math.log(num + 1, 2 ** 8)))
    print(bin(nn))
    return nn


@profile
@njit(parallel=True)
def _find_mapping_recursive(buckets: List[int], current_solution: Dict[int, int], index: int, done=0) -> None:
    if custom_insults_len - done < custom_insults_len - sum(map(bool, current_solution)):
        return

    base_bucket = math.ceil(len(custom_insults[index]) / bucket_size)

    for i in range(recursive_explore_size):
        if base_bucket + i >= num_buckets:
            break

        if buckets[base_bucket + i] > 0:
            buckets[base_bucket + i] -= 1
            current_solution[index] = add_packed_num(current_solution[index], base_bucket + i)
            done += 1

            if done == custom_insults_len:
                # Correct solution
                # all_solutions.add(copy.deepcopy(current_solution))
                pass
            else:
                new_index = index
                while new_index < custom_insults_len:
                    _find_mapping_recursive(buckets, current_solution, new_index, done)
                    new_index += 1

            buckets[base_bucket + i] += 1
            current_solution[index].pop(-1)
            done -= 1


def find_mapping_recursive() -> Dict[bytes, bytes]:
    buckets = [0 for _ in range(num_buckets)]
    max_nums = [0 for _ in range(num_buckets)]
    current_solution: List[List[int]] = [[0] for _ in range(custom_insults_len)]
    # solution = numba.typed.Dict.empty(key_type=int, value_type=list)

    for item in all_insults:
        max_nums[len(item) // bucket_size] += 1

    s = time.perf_counter()
    i = 0
    while i < custom_insults_len:
        # _find_mapping_recursive(max_nums, {i: 0 for i in range(custom_insults_len)}, i)
        i += 1
    print(f"Took {time.perf_counter() - s:.3f}s")

    # Now generate all possible mappings
    mappings = []
    for solution in all_solutions:
        cur_map = {}
        bucket_map = defaultdict(list)
        for item in all_insults:
            bucket_map[len(item) // bucket_size].append(item)

        for i, insult_nums in enumerate(solution):
            for bucket_num in insult_nums:
                cur_map[bucket_map[bucket_num].pop()] = custom_insults[i]

        for k, v in cur_map.items():
            assert len(v) <= len(k)

        mappings.append(cur_map)

    print(f"Generated {len(mappings)} mappings")
    # print(json.dumps([{k.decode(): v.decode() for k, v in mapping.items()} for mapping in mappings], indent=4))
    exit(0)

    # for item in mappings:
    #     print(f"The variance is {variance(map(custom_insults.index, item.values())):.3f}")
    pass

    return mappings[0]

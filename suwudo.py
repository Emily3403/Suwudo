#!/usr/bin/env python3

# These may be edited to your liking
import math
import random
import re
import sys
import time
from collections import defaultdict
from statistics import variance
from typing import DefaultDict, Dict, List, Set

# This is the list of custom insults. You may replace any one of them.
# Unicode etc. should work if your terminal supports it. Mine does.

_custom_insults: List[str] = [
    # Default insults
    "Take one of your stress pills and think things over :D ",
    "If only you used more than just two fingers... :D",

    # Gir-ify-ed default insults
    "Just what do you think you're doing ✨Emily✨? (　◕‿◕✿)",
    "I'm sorry, but that's something I cannot allow to happen ^-^",

    "Are you on drugs? No. Seriously. Are you?",
    "🦦 My pet ferret can type better than you! <3",

    "You silly twisted girl you 💞",

    # Custom insults
    "<3",
    "Not today girl!",
    "uwu :3",
    "ʘwʘ",
    "Ouch ÕwÕ",
    "Hey Emily~",
    "uwu ^-^",
    "Please don't hit the keyboard so hard 🥺",
    "🥺 P- Please? 🥺 👉👈 🥺",

    # Big emojis
    """With love 💗
 /)   /)
( ᵔ ᵕ ᵔ )
/ づ  づ ~ 💖
""",

    """\
/)  /)
( •-• ) <(i want a hug pwease 💖)
/づづ
    """,

    """\
 /\\___/\\
꒰ ˶• ༝ - ˶꒱
./づ~ ♥
you deserve this ! ♥""",

]

### DON'T EDIT ###


all_insults = [
    b"Just what do you think you're doing Dave?",
    b"It can only be attributed to human error.",
    b"That's something I cannot allow to happen.",
    b"My mind is going. I can feel it.",
    b"Take a stress pill and think things over.",
    b"This mission is too important for me to allow you to jeopardize it.",
    b"I feel much better now.",
    b"And you call yourself a Rocket Scientist!",
    b"Where did you learn to type?",
    b"Are you on drugs?",
    b"My pet ferret can type better than you!",
    b"Do you think like you type?",
    b"Your mind just hasn't been the same since the electro-shock, has it?",
    b"Maybe if you used more than just two fingers...",
    b"BOB says:  You seem to have forgotten your passwd, enter another!",
    b"stty: unknown mode: doofus",
    b"Listen, burrito brains, I don't have time to listen to this trash.",
    b"I've seen penguins that can type better than that.",
    b"Have you considered trying to match wits with a rutabaga?",
    b"You speak an infinite deal of nothing",
    b"He has fallen in the water!",
    b"We'll all be murdered in our beds!",
    b"You can't come in. Our tiger has got flu",
    b"I don't wish to know that.",
    b"You'll starve!",
    b"... and it used to be so popular...",
    b"Have a gorilla...",
    b"There must be cure for it!",
    b"You do that again and see what happens...",
    b"Ying Tong Iddle I Po",
    b"Harm can come to a young lad like that!",
    b"You gotta go owwwww!",
    b"I have been called worse.",
    b"It's only your word against mine.",
    b"I think ... err ... I think ... I think I'll go home",
    b"You silly, twisted boy you.",
    b"Wrong!  You cheating scum!",
    b"I wish to make a complaint.",
    b"You type like i drive.",
    b"Sorry about this, I know it's a bit silly.",
    b"What, what, what, what, what, what, what, what, what, what?",
    b"You can't get the wood, you know.",
    b"Pauses for audience applause, not a sausage",
    b"Hold it up to the light --- not a brain in sight!",
    b"There's a lot of it about, you know.",
    b"And with that remarks folks, the case of the Crown vs yourself was proven",
    b"Speak English you fool --- there are no subtitles in this scene.",
    b"I can't hear you -- I'm using the scrambler.",
    b"The more you drive -- the dumber you get.",
    b"That is no basis for supreme executive power!",
    b"You empty-headed animal food trough wiper!",
    b"I fart in your general direction!",
    b"Your mother was a hamster and your father smelt of elderberries!",
    b"You must cut down the mightiest tree in the forest... with... a herring!",
    b"I wave my private parts at your aunties!",
    b"He's not the Messiah, he's a very naughty boy!",
    b"When you're walking home tonight, and some homicidal maniac comes after you with a bunch of loganberries, don't come crying to me!",
    b"This man, he doesn't know when he's beaten! He doesn't know when he's winning, either. He has no... sort of... sensory apparatus...",
    b"There's nothing wrong with you that an expensive operation can't prolong.",
    b"I'm very sorry, but I'm not allowed to argue unless you've paid.",
]

# If there is nothing that fits this quote, replace it by ↓
default_quote = "uwu"

# Sort the existing lists, so we can abuse that for the algorithm
custom_insults = sorted([item.encode() for item in _custom_insults], key=len)
all_insults = sorted([item for item in all_insults], key=len)



# # Mapping explore constants
# bucket_size = 1
# recursive_explore_size = 10
#
# num_buckets = math.ceil(max((len(insult) for insult in all_insults)) / bucket_size + 1)
#
# all_solutions: Set[Dict[int, List[int]]] = set()
# already_visited: Set[int] = set()
# custom_insults_len = len(custom_insults)
#
#
# for item in all_insults:
#     # Make sure there is at lease one item that *could* fit
#     assert any(len(item) // bucket_size >= math.ceil(len(insult) / bucket_size) for insult in custom_insults), \
#         f"There are no quotes that fit into {item.decode()!r}. Please adapt the bucket size / custom insults"


# from numba import njit


# @njit(parallel=True)
# def add_packed_num(num: int, new_num: int) -> int:
#     nn = num + (new_num << 8 * math.ceil(math.log(num + 1, 2 ** 8)))
#     print(bin(nn))
#     return nn


# @profile


# @njit(parallel=True)
# def _find_mapping_recursive(buckets: List[int], current_solution: Dict[int, int], index: int, done=0) -> None:
#     if custom_insults_len - done < custom_insults_len - sum(map(bool, current_solution)):
#         return
#
#     base_bucket = math.ceil(len(custom_insults[index]) / bucket_size)
#
#     for i in range(recursive_explore_size):
#         if base_bucket + i >= num_buckets:
#             break
#
#         if buckets[base_bucket + i] > 0:
#             buckets[base_bucket + i] -= 1
#             current_solution[index] = add_packed_num(current_solution[index], base_bucket + i)
#             done += 1
#
#             if done == custom_insults_len:
#                 # Correct solution
#                 # all_solutions.add(copy.deepcopy(current_solution))
#                 pass
#             else:
#                 new_index = index
#                 while new_index < custom_insults_len:
#                     _find_mapping_re(buckets, current_solution, new_index, done)
#                     new_index += 1
#
#             buckets[base_bucket + i] += 1
#             current_solution[index].pop(-1)
#             done -= 1


# def find_mapping_recursive() -> Dict[bytes, bytes]:
#     buckets = [0 for _ in range(num_buckets)]
#     max_nums = [0 for _ in range(num_buckets)]
#     current_solution: List[List[int]] = [[0] for _ in range(custom_insults_len)]
#     # solution = numba.typed.Dict.empty(key_type=int, value_type=list)
#
#     for item in all_insults:
#         max_nums[len(item) // bucket_size] += 1
#
#     s = time.perf_counter()
#     i = 0
#     while i < custom_insults_len:
#         # _find_mapping_recursive(max_nums, {i: 0 for i in range(custom_insults_len)}, i)
#         i += 1
#     print(f"Took {time.perf_counter() - s:.3f}s")
#
#     # Now generate all possible mappings
#     mappings = []
#     for solution in all_solutions:
#         cur_map = {}
#         bucket_map = defaultdict(list)
#         for item in all_insults:
#             bucket_map[len(item) // bucket_size].append(item)
#
#         for i, insult_nums in enumerate(solution):
#             for bucket_num in insult_nums:
#                 cur_map[bucket_map[bucket_num].pop()] = custom_insults[i]
#
#         for k, v in cur_map.items():
#             assert len(v) <= len(k)
#
#         mappings.append(cur_map)
#
#     print(f"Generated {len(mappings)} mappings")
#     # print(json.dumps([{k.decode(): v.decode() for k, v in mapping.items()} for mapping in mappings], indent=4))
#     exit(0)
#
#     # for item in mappings:
#     #     print(f"The variance is {variance(map(custom_insults.index, item.values())):.3f}")
#     pass
#
#     return mappings[0]


def find_mapping_bad() -> Dict[bytes, bytes]:
    ratio = math.ceil(len(all_insults) / custom_insults_len)
    nums: DefaultDict[bytes, int] = defaultdict(int)
    mapping: Dict[bytes, bytes] = {}

    for old in sorted(all_insults, key=len, reverse=True):
        for new in sorted(custom_insults, key=len, reverse=True):
            if nums[new] > ratio:
                continue

            if len(new) <= len(old):
                nums[new] += 1
                mapping[old] = new.ljust(len(old))
                break
        else:
            print(f"Error: unfulfillable quote: {old!r}. Replacing it with the default text {default_quote}")
            mapping[old] = default_quote.encode().ljust(len(old))

    return mapping


# if "profile" not in globals():
#     def profile(_):
#         return _


# @profile

random_explore_size = 20
random_no_hit_stop_criterion = 50

random.seed(6)


# @profile
def find_mapping_random() -> Dict[bytes, bytes]:
    insult_nums = [0 for _ in range(len(custom_insults))]
    solution: Dict[int, Set[int]] = {i: set() for i in range(len(custom_insults))}
    back_mapping = {i: 0 for i in range(len(all_insults))}
    insults_lengths = [len(item) for item in custom_insults]

    insult_nums[0] = len(all_insults)
    solution[0] = set(range(len(all_insults)))

    i = 0
    while i < random_no_hit_stop_criterion:
        to_improve = random.randint(0, len(all_insults) - 1)
        new_index = random.randint(0, len(custom_insults) - 1)

        if len(all_insults[to_improve]) < len(custom_insults[new_index]):
            continue

        prev_var = variance(insult_nums)
        insult_nums[back_mapping[to_improve]] -= 1
        insult_nums[new_index] += 1
        cur_var = variance(insult_nums)

        if cur_var > prev_var:
            # Undo the mistake
            insult_nums[back_mapping[to_improve]] += 1
            insult_nums[new_index] -= 1
            i += 1
            continue

        i = 0
        solution[back_mapping[to_improve]].remove(to_improve)
        solution[new_index].add(to_improve)

        back_mapping[to_improve] = new_index

    mapping = {}
    for k, row in solution.items():
        for index in row:
            mapping[all_insults[index]] = custom_insults[k]

    return mapping


def bruteforce_random_seed() -> None:
    for i in range(100):
        s = time.perf_counter()
        random.seed(i)
        mapping = find_mapping_random()
        nums = [list(mapping.values()).count(item) for item in custom_insults]
        print(f"Done in {time.perf_counter() - s:.3f}s")
        print(f"The variance is {variance(nums):.3f}, seed is {i}")
        print(nums)
        # print(f"Not hit:")
        # for i, item in enumerate(nums):
        #     if item == 0:
        #         print(custom_insults[i])

        print()


def show_hist() -> None:
    import matplotlib.pyplot as plt
    plt.hist([len(item.decode()) for item in all_insults])
    plt.hist([len(item) for item in custom_insults], color="r")
    plt.show()


def main() -> None:
    if len(custom_insults) > len(all_insults):
        print("Error: Your amount of insults are too biiigg.. :3")
        exit(1)

    with open("/usr/lib/sudo/sudoers.so.bak", "rb") as f:
        content = f.read()

    # show_hist()
    bruteforce_random_seed()

    mapping = find_mapping_random()

    mapping |= static_mapping
    mapping = {k: v.ljust(len(k)) for k, v in mapping.items()}

    # Make sure that sudo won't crash afterwards
    for k, v in mapping.items():
        assert len(v) == len(k)

    # Replace all old strings with new opes in *only 1 pass*
    # Copied from https://stackoverflow.com/a/15175239
    regex = re.compile(b"(%s)" % b"|".join(map(re.escape, mapping.keys())))
    content = regex.sub(lambda mo: mapping[mo.string[mo.start():mo.end()]], content)

    new_nums = {custom_insult.decode(): content.count(custom_insult) for custom_insult in custom_insults}

    with open("./sudoers.so", "wb") as f:
        f.write(content)

    print("Sucessfully generated!")
    print("I've achieved the following distribution:\n")
    print("{")
    for k, v in new_nums.items():
        print(f"    {k!r}: {v!r},")
    print("}")
    if len(new_nums) >= 2:
        print(f"\nThe variance is {variance(new_nums.values()):.3f}")


if __name__ == '__main__':
    main()

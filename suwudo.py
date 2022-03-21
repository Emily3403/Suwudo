#!/usr/bin/env python3

# These may be edited to your liking
import json
import math
import random
import re
import sys
import time
from collections import defaultdict
from multiprocessing import Pool
from statistics import variance
from typing import DefaultDict, Dict, List, Set, Tuple

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
    "Love you <3",
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
/ づ  づ ~ 💖\
""",

    """\
/)  /)
( •-• ) <(i want a hug pwease 💖)
/づづ\
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

# Sort the existing lists, so we can abuse that for the algorithm
custom_insults = sorted([item.encode() for item in _custom_insults], key=len)
all_insults = sorted([item for item in all_insults], key=len)

# Will stop the algorithm after ↓ unsuccessful attempts
stop_after_iterations = 45

# Set the seed to something preselected. This will guarantee a good mapping.
random.seed(1106)


def find_mapping_random() -> Dict[bytes, bytes]:
    insult_nums = [0 for _ in range(len(custom_insults))]
    solution: Dict[int, Set[int]] = {i: set() for i in range(len(custom_insults))}
    back_mapping = {i: 0 for i in range(len(all_insults))}

    insult_nums[0] = len(all_insults)
    solution[0] = set(range(len(all_insults)))

    i = 0
    while i < stop_after_iterations:
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


def _wasted_space(seed: int) -> Tuple[int, int]:
    random.seed(seed)
    mapping = find_mapping_random()
    return seed, sum(len(item) for item in mapping.keys()) - sum(len(item) for item in mapping.values())


def find_least_space_wasted() -> None:
    s = time.perf_counter()
    with Pool(16) as ex:
        nums = ex.map(_wasted_space, range(3000))

    best = sorted(nums, key=lambda x: x[1])[0]
    print(f"Done in {time.perf_counter() - s:.3f}s")
    print(f"Best seed: {best[0]}, wasted: {best[1]}")


def bruteforce_random_seed() -> None:
    best_wasted = -1
    best = 0
    for i in range(10):
        s = time.perf_counter()
        random.seed(i)
        mapping = find_mapping_random()
        wasted_space = sum(len(item) for item in mapping.keys()) - sum(len(item) for item in mapping.values())
        if wasted_space < best_wasted or best_wasted == -1:
            best = i
            best_wasted = wasted_space

        nums = [list(mapping.values()).count(item) for item in custom_insults]

        print(f"Done in {time.perf_counter() - s:.3f}s")
        print(f"The variance is {variance(nums):.3f}, seed is {i}")
        print(f"Wasted space: {wasted_space}")
        print(nums)
        print()

    print(f"Best seed: {best}")


def show_hist() -> None:
    import matplotlib.pyplot as plt
    plt.hist([len(item.decode()) for item in all_insults])
    plt.hist([len(item) for item in custom_insults], color="r")
    plt.show()


def main() -> None:
    if len(custom_insults) > len(all_insults):
        print("Error: Your amount of insults are too biiigg.. :3")
        exit(1)

    with open("/usr/lib/sudo/sudoers.so", "rb") as f:
        content = f.read()

    # show_hist()
    # find_least_space_wasted()
    # bruteforce_random_seed()

    print("Generating the mapping... This might take a second\n")
    mapping = find_mapping_random()

    mapping = {k: v.ljust(len(k)) for k, v in mapping.items()}

    # Make sure that sudo won't crash afterwards
    for k, v in mapping.items():
        assert len(v) == len(k)

    # Replace all old strings with new opes in *only 1 pass*
    # Copied from https://stackoverflow.com/a/15175239
    regex = re.compile(b"(%s)" % b"|".join(map(re.escape, mapping.keys())))
    content = regex.sub(lambda mo: mapping[mo.string[mo.start():mo.end()]], content)

    new_nums = {custom_insult.decode(): content.count(custom_insult) for custom_insult in custom_insults}

    print("\nI've achieved the following distribution:\n")
    print("{")
    for st, count in new_nums.items():
        print(f"    {st}: {count},")
    print("}")

    with open("./sudoers.so", "wb") as f:
        f.write(content)


# Future ideas
# - sudo terminates after 3 wrong attempts
# - Bring this to the arch user repository
# - ansible config

if __name__ == '__main__':
    main()

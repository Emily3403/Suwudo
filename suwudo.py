#!/usr/bin/env python3

# These may be edited to your liking
import math
import os
from datetime import datetime

custom_insults = [
    b"Just what do you think you're doing Emily?",
    b"This can only be attributed to human error :3",
    b"I'm sorry, but that's something I cannot allow to happen ^-^",
    b"My mind is going. I can feel it.",
    b"Sorry about this I know it's a bit sillyyy~.",
    b"Take one of your stress pills and think things over :D ",
    b"This mission is tuwu important for me to allow you to jeopardize it.",
    b"I feel much better now uwu",
    b"And you call yourself a Rocket Scientist!",
    b"No soap honkie-lips.",
    b"Where did you learn to type?",
    b"Are you on drugs? No. Seriously.",
    b"My pet ferret can type better than you! And it's damn cute <3",
    b"You type like I drive.",
    b"Do you think like you type?",
    b"Your mind just hasn't been the same since the electro-shock has it?",
    b"Maybe if you used more than just two fingers...",
    b"I can't hear you - I'm using the scrambler.",
    b"The more you drive - the dumber you get.",
    b"Listen, burrito brains, I don't have time to listen to this trash.",
    b"You speak an infinite deal of nothing :3",
    b"You silly twisted girl you.",
    b"She has fallen in the water!",
    b"We'll all be murdered in our beds!",
    b"What what what what what what what what what what?",
    b"Pauses for audience applause ...",
    b"Hold it up to the light - not a brain in sight!",
    b"Have a gorilla...",
    b"There must be cure for it!",
    b"There's a lot of it about you know.",
    b"You do that again and see what happens...",
    b"Speak English you fool - there are no subtitles in this scene.",
    b"I have been called worse.",
    b"It's only your word against mine. uwu",
    b"Wrong!  You cheating scum!",
    b"I wish to make a complaint.",
    b"She's not the Messiah, she's a very naughty girl!",
    b"When you're walking home tonight, and some homicidal maniac comes after you with a bunch of loganberries, don't come crying to me!",
    b"There's nothing wrong with you that an expensive operation can't prolong.",
    b"I'm very sorry, but I'm not allowed to argue unless you've paid.",
    b"<3",
    b"Not today girl!",
    b"uwu :3",
]


# Don't edit this.
all_insults = [
    b"Just what do you think you're doing Dave?",
    b"It can only be attributed to human error.",
    b"That's something I cannot allow to happen.",
    b"My mind is going. I can feel it.",
    b"Sorry about this I know it's a bit silly.",
    b"Take a stress pill and think things over.",
    b"This mission is too important for me to allow you to jeopardize it.",
    b"I feel much better now.",
    b"And you call yourself a Rocket Scientist!",
    b"No soap honkie-lips.",
    b"Where did you learn to type?",
    b"Are you on drugs?",
    b"My pet ferret can type better than you!",
    b"You type like I drive.",
    b"Do you think like you type?",
    b"Your mind just hasn't been the same since the electro-shock has it?",
    b"Maybe if you used more than just two fingers...",
    b"BOB says: You seem to have forgotten your passwd enter another!",
    b"stty: unknown mode: doofus",
    b"I can't hear you - I'm using the scrambler.",
    b"The more you drive - the dumber you get.",
    b"Listen, broccoli brains, I don't have time to listen to this trash.",
    b"Listen, burrito brains, I don't have time to listen to this trash.",
    b"I've seen penguins that can type better than that.",
    b"Have you considered trying to match wits with a rutabaga?",
    b"You speak an infinite deal of nothing",
    b"You silly twisted boy you.",
    b"He has fallen in the water!",
    b"We'll all be murdered in our beds!",
    b"You can't come in. Our tiger has got flu",
    b"I don't wish to know that.",
    b"What what what what what what what what what what?",
    b"You can't get the wood you know.",
    b"You'll starve!",
    b"... and it used to be so popular...",
    b"Pauses for audience applause not a sausage",
    b"Hold it up to the light - not a brain in sight!",
    b"Have a gorilla...",
    b"There must be cure for it!",
    b"There's a lot of it about you know.",
    b"You do that again and see what happens...",
    b"Ying Tong Iddle I Po",
    b"Harm can come to a young lad like that!",
    b"Speak English you fool - there are no subtitles in this scene.",
    b"You gotta go owwwww!",
    b"I have been called worse.",
    b"It's only your word against mine.",
    b"I think ... err ... I think ... I think I'll go home",
    b"You silly, twisted boy you.",
    b"Wrong!  You cheating scum!",
    b"You type like i drive.",
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
    b"Your mind just hasn't been the same since the electro-shock, has it?",
    b"BOB says:  You seem to have forgotten your passwd, enter another!",
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


def get_mapping():
    if len(custom_insults) > len(all_insults):
        print("Error: Your amount of insults are too biiigg.. :3")
        exit(1)

    ratio = math.ceil(len(all_insults) / len(custom_insults))
    nums = [0 for _ in range(len(custom_insults))]
    mapping = {}

    for old in sorted(all_insults, key=len, reverse=True):
        for i, new in enumerate(sorted(custom_insults, key=len, reverse=True)):
            if nums[i] < ratio and len(new) <= len(old):
                # Use the entry
                nums[i] += 1
                mapping[old] = new.ljust(len(old))
                break
        else:
            print(f"Error: unfulfillable quote: {old}. Replacing it with the default text \"uwu\"")
            mapping[old] = b"uwu".ljust(len(old))

    return mapping


def main() -> None:
    print("Backing up the previous library ...")
    os.system(f"sudo cp /usr/lib/sudo/sudoers.so /usr/lib/sudo/sudoers.so.bak.{int(datetime.now().timestamp())}")
    print("Done backing up!\n\nBuilding binary ...")

    with open("/usr/lib/sudo/sudoers.so.bak", "rb") as f:
        content = f.read()
        mapping = get_mapping()

        for old, new in mapping.items():
            content = content.replace(old, new)

    with open("./sudoers.so", "wb") as f:
        f.write(content)

    os.system("sudo cp ./sudoers.so /usr/lib/sudo/sudoers.so")
    print("Sucessfully installed!")


if __name__ == '__main__':
    main()

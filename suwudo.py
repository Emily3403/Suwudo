#!/usr/bin/env python3

# These may be edited to your liking
import os

custom_insults = [
    b"^-^ Juwst whawt duwu uwu think uwu'we doing Emily? :3",
    b"uwu Iwt cawn onwy be attwibuted tooo human ewwow. <3",
    b"<3 That's something i cannot awwow tuwu happen. :3",
    b"Are you on drugs? Seriously.",
    b"My pet ferret can type better than you!",
    b"Do you think like you type?",

    b"uwu",
    b"owo",
    b"AYAYA",
    b"<3",
    b":3",
    b"nya~ :3",
    b"UwU",
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
    b"And with that remarks folks the case of the Crown vs yourself was proven.",
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


def get_mapping_all_to_custom():
    if len(custom_insults) > len(all_insults):
        print("Error: Your amount of insults are too biiigg.. :3")
        exit(1)

    insults = custom_insults + [custom_insults[i % len(custom_insults)] for i in range(len(all_insults) - len(custom_insults))]

    mapping = {k: v for k, v in zip(sorted(all_insults, key=len, reverse=True), sorted(insults, key=len, reverse=True))}

    for orig, new in mapping.items():
        if len(new) > len(orig):
            print(f"Error: Tried to insert a word with {len(new)} chars into a space of {len(orig)}. That can't work.")
            exit(1)

        mapping[orig] = new.ljust(len(orig))

    return mapping



def main() -> None:
    print("Backing up the previous library:")
    os.system("sudo cp /usr/lib/sudo/sudoers.so /usr/lib/sudo/sudoers.so.bak")

    print("Generating sudoers.so from `/usr/lib/sudo/sudoers.so`")

    with open("/usr/lib/sudo/sudoers.so", "rb") as f:
        content = f.read()
        mapping = get_mapping_all_to_custom()

        for orig, new in mapping.items():
            content = content.replace(bytes(orig), bytes(new.ljust(len(orig))))

    with open("./sudoers.so", "wb") as f:
        f.write(content)

    print("Successfully generated sudoers.so. Now install it with\n\nsudo cp sudoers.so /usr/lib/sudo/sudoers.so")


if __name__ == '__main__':
    main()

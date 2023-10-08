# 1.2 The Broken Device I
# Cosmo leads you across Cosmo plaza and to a large iron door. To your surprise, it is open. "This is the corridor that leads to a storage room", he explains.

# You enter and find yourself in a dark, torch-lit corridor. On the opposite side of the corridor, there is another door. You approach it and try to open it, but this one is locked. On the door, there is a sequence of symbols and below, there is a dusty keyboard.

# "The next cipher plate is behind this door. Do you remember what I told you about the locks and decoding devices outside?", Cosmo asks. "This is a similar lock. But I have to tell you that this looks more complicated than the one on the chest."

# That is not what you wanted to hear. You turn around, searching for additional hints. On one of the corridor walls, there is a small screen embedded. It displays a similar sequence of strange symbols as the door to the next chamber, and it also has a keyboard attached to it. You were rather looking for answers, not for more questions...

# You are frustrated. But suddenly, Cosmo approaches you: "Hey, look what I found in the corner! I first thought it was a piece of rubbish, but this is one of the ancient decoding devices! I seems to be broken though..."

# You take a look at the device. It has several switches and handles, and some of them are named by the same strange symbols you found on the door. If you could enter the symbols from the door, this device would clearly tell you the solution? You try to turn it on, but nothing happens.

# "Can't you repair such a thing?", you ask Cosmo. "I don't think so", he answers. "I guess it is too damaged. But I have another idea: Maybe I can access the memory of the device. It also has some scratches, but I might be able to extract the devices log. It should contain enough information for you to reverse engineer the problem on the door."

# After a few minutes, Cosmo's eyes start to glow brighter. "Here we go!", he says. "These are the first lines of the log that I could recover. But there is a lot more, I just need more time..."

# input: XXXXXXXX; XXXXXXXX; G; Q; output: 0
# input: XXXXXXXY; XXXXXXXX; G; Q; output: 1
# input: XXXXXXXY; XXXXXXXY; G; Q; output: 10
# input: XXXXXXXX; XXXXXXXX; L; Q; output: 0
# input: XXXXXXXY; XXXXXXXY; L; Q; output: 0
# input: XXXXXXYX; XXXXXXXY; L; Q; output: 1
# input: XXXXXXYX; XXXXXXXY; G; Q; output: 11
# input: XXXXXXYY; XXXXXXXY; L; Q; output: 10
# input: XXXXXYXY; XXXXXXYY; G; Q; output: 1000
# input: XXXXYXXX; XXXXXXXY; L; Q; output: 111
# "Before you continue, what about this small screen in the wall?", you ask. "What does it have to do with the door at the end of the corridor? Do I have to solve this problem, too?"

# "Oh, my bad. I wanted to tell you, but then I found the device and got excited. No, you don't have to solve it. This is an old checkpoint, where the users of the decoding devices could check if they still worked properly. Maybe you should take a look at it. It can help you check if you understand the codes correctly."

# While Cosmo continues looking for more log data in the device's memory, you take a look at the small screen on the wall. It says:

# XXXXXYXY; XXXXYXXY; G; Q;
# XXXXYYXY; XXXXXXYY; L; Q;

# Suddenly, Cosmo's eyes lighten up again. "Now this should be enough to get us through the door!", he exclaims in celebration. You look at the logs Cosmo found:

# input: YXXXXXXX; YXXXXXXX; G; Q; output: 0
# input: YXXXXXXY; YXXXXXXX; G; Q; output: 1
# input: YYXXXXXX; YYYXXXXY; G; Q; output: 10100001
# input: XXXXXXXX; XXXXXXXY; L; Q; output: 11111111
# input: XXXXYYXY; XXXXYYYY; L; Q; output: 11111110
# input: XYYYXXXX; YYYYXXXX; L; Q; output: 10000000
# input: YXXXYXYX; YXXXYXXY; G; Q; output: 10011
# input: YYXXXXYY; YYYXYXXY; L; Q; output: 11011010
# input: YYXXXXXX; YYYXXYYY; G; Q; output: 10100111
# input: XYXXXXXX; YXXYYYYY; L; Q; output: 10100001
# "If you ask me, both of the puzzles seem to build upon each other", he explains. "So the code on the door should work similarly to the code at the checkpoint screen, only with some additional rules to follow."

# With that in mind, you go back to the door and look at the symbols again:

# YXXXXYXY; XXXXXYXY; G; Q;
# YXXXYXYX; YYYXXXXX; L; Q;

import numpy as np

def solve_puzzle(input_str):
    # Split the input string into two parts
    parts = input_str.split("; ")
    part1 = list(parts[0])
    part2 = list(parts[1])

    # Check the third input
    if parts[2] == "G":
        # Generate the output string for "G"
        output = ""
        for i in range(len(part1)):
            if part1[i] == part2[i]:
                output += "0"
            else:
                output += "1"
    elif parts[2] == "L":
        # Generate the output string for "L"
        output = ""
        for i in range(len(part1)):
            if part1[i] != part2[i]:
                output += "1"
            else:
                output += "0"

    # Return the output string
    return output

print(solve_puzzle("XXXXXXXX; XXXXXXXY; L; Q; "))


def solve_puzzle2(input_str):
    # Split the input string into two parts
    parts = input_str.split("; ")
    part1 = int(parts[0].replace("X", "0").replace("Y", "1"), 2)
    part2 = int(parts[1].replace("X", "0").replace("Y", "1"), 2)

    # Check the third input
    if parts[2] == "G":
        # Generate the output string for "G"
        output = bin(part1 ^ part2)[2:].zfill(len(parts[0]))
    elif parts[2] == "L":
        # Generate the output string for "L"
        output = bin(part1 ^ part2)[2:].zfill(len(parts[0]))
        output = output.replace("0", "2").replace("1", "0").replace("2", "1")

    # Return the output string
    return output

print(solve_puzzle2("XXXXXXXX; XXXXXXXY; G; Q; "))
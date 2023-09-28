# 0.3 Traps
# "The third cipher plate is inside the ventilation system," Cosmo says as it points at a small opening on the side of the temple.

# "The ventilation system, huh? But that opening is pretty small. I can't fit in there, Cosmo," you say.

# "No need to worry. I am small enough to go in. However, I cannot get the cipherplate alone. I need your help."

# "What can I do?"

# "You know, human, the passages in the ventilation shafts are rigged with traps. If I run into an active trap, it will destroy my circuits. Luckily, not all traps are active. If you can find out which of the traps are safe, I can find my way around and retrieve the cipherplate."

# "Ok, that doesn't sound complicated," you say, as you start scanning the ventilation system. Looking through the scan results, you go, "What? It is that easy? The traps have log files in plain English. Here, Cosmo, look at the logs of the first couple of traps."

#         1: idle reversed ready reversed toggled reversed reversed
#         2: ready inverted switched quiet inverted flipped reversed
#         3: primed ready switched ready toggled disabled toggled
#         4: live reversed flipped inverted inverted inverted reversed
#         5: inactive flipped flipped reversed active live
#         6: quiet live active inactive armed reversed flipped
#         7: disabled inverted inverted standby flipped switched inverted
#         8: live quiet disabled flipped toggled toggled reversed toggled
#         9: standby toggled inverted reversed reversed switched
#         10: armed live flipped flipped ready reversed         
# "The numbers on the left are the IDs of the traps. And then, there is the actual log."

# "I can explain, how the log works, human!" Cosmo says. "You have to read each line from left to right. Whenever a maintenance bot works on a traps, they add one more word to the log to indicate the state of the trap. The five words inactive, disabled, quiet, standby, idle indicate that the trap was deactivated. The words live, armed, ready, primed, active mean that the bot activated the trap. And finally the words flipped, toggled, reversed, inverted, switched mean, that the state of the trap was changed: if it was active before, then it was deactivated, and vice-versa.

# "Sounds reasonable, Cosmo. So, I see in my example scan, trap number 10 is safe, and all others are unsafe. Let me go ahead and create you a list of the safe traps in the full scan."

import pandas as pd
import numpy as np

# Read the logs
logs = pd.read_csv('data/03_trap_logs.txt', header=None, sep=': ')
logs.columns = ['ID','log']
logs.head()

# List with words that indicate a safe trap
safe_words = ['inactive', 'disabled', 'quiet', 'standby', 'idle']

# List with words that indicate an unsafe trap
unsafe_words = ['live', 'armed', 'ready', 'primed', 'active']

# List with words that indicate a trap was changed
change_words = ['flipped', 'toggled', 'reversed', 'inverted', 'switched']

# Create a function to check if a trap is safe - 
# check for the last safe or unsafe word and then count the number of change words after that
# if there is safe word and the count of change words is even, then the trap is safe
# if there is an unsafe word and the count of change words is odd, then the trap is safe
def is_safe(log):
    # Split the log into words
    words = log.split(' ')
    
    # Find the last safe or unsafe word
    for i in range(len(words)-1, -1, -1):
        if words[i] in safe_words:
            last_safe = words[i]
            break
        elif words[i] in unsafe_words:
            last_safe = words[i]
            break
    
    # Count the number of change words after the last safe or unsafe word
    count = 0
    for i in range(i+1, len(words)):
        if words[i] in change_words:
            count += 1
    
    # Check if the trap is safe
    if last_safe in safe_words and count % 2 == 0:
        return True
    elif last_safe in unsafe_words and count % 2 == 1:
        return True
    else:
        return False
    
# Check if each trap is safe
logs['safe'] = logs['log'].apply(is_safe)
logs.head()

# Find the safe traps
safe_traps = logs[logs['safe'] == True]['ID']

# Print the solution
print(safe_traps)

# Sum the safe trap IDs
print(sum(safe_traps)) # 498996

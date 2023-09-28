# 0.1 The Key Maker
# You approach the workshop where Cosmo detected the first cipher plate - a small building nestled between the trees. Upon further inspection, you see that it was used to teach the craft of making keys. Before a young key maker would be allowed to work in the key makers' chamber inside the temple, they'd have to practice their craft in this workshop outside the temple.

# Inside the storage room of the building, you discover a chest and a large pile of keys.

# "The signal is strong here, human. One of the cipher plates must be in this chest," Cosmo says.

# "Ok, good. But it's locked. How do we find the key to open it? This pile of keys easily contains multiple thousand keys. We don't have the time to try out all of them."

# "Let me take a look..., this is a training chest. It can be opened with any key that conforms to the rules written on its back. This one is a training chest for ordered keys. So we need to find an ordered key in this pile."

# "What is an ordered key, Cosmo?"

# "Here, take a closer look at the pile of keys, human! Each key is made of multiple segments and each segment can have one of six shapes. Let's assign them the letters a to f, so we can represent a key by a string. An ordered key is one, where the segments are in alphabetical order.

# Here are some examples. These keys are ordered:

# b
# cdef
# bddf
# aaabcccccfff
# And these ones are not ordered:

# ba
# acda
# afcdeff
# aaaaabdfdeef
# Now, there is one more thing you need to know. During training, a young key maker would have to sit in this workshop and make keys until they succeed in crafting one valid key. Then, they'd continue with the next lesson. This means, this whole pile of keys here contains exactly one ordered key," Cosmo concludes.

# The complete pile of keys is given in the input file `01_keymaker_ordered.txt` in the data library. Find the one ordered key. The solution code is that key.

import pandas as pd
import numpy as np

# Read in the data
keymaker_ordered = pd.read_csv('data/01_keymaker_ordered.txt', header=None)
keymaker_ordered.columns = ['key']
keymaker_ordered.head()

# Create a function to check if a key is ordered
def is_ordered(key):
    for i in range(len(key)-1):
        if key[i] > key[i+1]:
            return False
    return True

# Check if each key is ordered
keymaker_ordered['ordered'] = keymaker_ordered['key'].apply(is_ordered)
keymaker_ordered.head()

# Find the ordered key
ordered_key = keymaker_ordered[keymaker_ordered['ordered'] == True]['key'].values[0]
print(ordered_key)

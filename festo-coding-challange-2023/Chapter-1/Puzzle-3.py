# 1.3 Sewer System - Traps with Weights
# "We will find another cipher plate in the sewer system below the ground, human," Cosmo explains "and by 'we', I mean 'I', because you won't fit through the tunnels. But you can help me navigate by identifying which traps in the tunnels are safe."

# "That sounds familiar, Cosmo. Are these the same kind of traps as before?"

# "No, sorry, these ones are different. They are weight-based trap mechanisms. Each trap acts like a scale. A trap can be activated or deactivated by placing weights on the left and right side of the scale. To deactivate a trap - and make a passage safe - one has to fulfill the rules of equality and diversity:

# Equality: Both sides of the scale must contain the same number of objects.
# Equality: Both sides of the scale must carry exactly the same weight.
# Diversity: All objects on the scale must have different weights. No two objects may have the same weight."
# "Okay, got it, equality, equality and diversity. How do we know what weight is on each side of the scales?"

# "The inhabitants of the temple used a collection of special flasks. Each flask is labeled with a whole number (1, 2, 3, ...) and the flask with label 'n' has a weight of exactly 1/n weight units. Only these flasks are used on the traps to bring them into balance.

# For example, consider the following trap configuration:

# 4 20 - 5 10
# In this scenario, the flasks 4 and 20 are placed on the left side of the trap, while the flasks 5 and 10 are placed on the right side. By calculating the sum of the weights, we find that:

# 1/4 + 1/20 = 1/5 + 1/10
# Furthermore, the number of flasks on both sides is equal and no two flasks have the same weight. Hence, the trap is deactivated and the passage is safe."

# "Ok, I got it, Cosmo. So this is also a safe configuration, right?

# 2 - 3 6
# Because 1/2 = 1/3 + 1/6!"

# "Not quite," Cosmo replies, "the weights add up correctly, but the number of flasks is not the same on both sides."

# "Ok, then let's just add a very, very, very small flask to the left side of the scale. Like this:

# 2 99999999999999999999999999999999999 - 3 6
# This should be fine now!"

# "I am sorry to disappoint you, human, but the trap mechanisms demand strict mathematical equality of the weights - even if this extra flask has a barely noticable weight, this scale is not exactly balanced."

# "I have to admit, I'm impressed," you say, "The level of precision in these mechanisms is unlike anything I've ever seen. Just to be clear, these configurations are also unsafe, because some flasks occur more than once:"

# 4 4 - 3 6
# 2 4 20 - 2 5 10
# "Exactly!" Cosmo cheers in excitement "That's correct. Now let's go for the cipher plate. In this part of the sewer system, the flasks are fixed on the traps, so we cannot change their balance state. All we can do is observe and identify the safe ones."

# After scanning the sewer system, you obtain a complete list of all trap configurations. You create a list of the following form

import pandas as pd
import numpy as np
from decimal import Decimal

# Read in the data/13_trap_balance.txt file 
# and store it in a variable called trap_balance
trap_balance_df = pd.read_csv('data/13_trap_balance.txt', sep=": ", header=None, index_col=0, engine='python')
trap_balance_df.columns = ['trap']
trap_balance_df.index = trap_balance_df.index.astype(int)

# Calculate the sum of the weights on each side of the trap
trap_balance_df['sum_left'] = trap_balance_df['trap'].apply(lambda x: sum([Decimal(1/int(i)) for i in x.split(' - ')[0].split(' ')]))
trap_balance_df['sum_right'] = trap_balance_df['trap'].apply(lambda x: sum([Decimal(1/int(i)) for i in x.split(' - ')[1].split(' ')]))

# Calculate the number of flasks on each side of the trap
trap_balance_df['num_left'] = trap_balance_df['trap'].apply(lambda x: len(x.split(' - ')[0].split(' ')))
trap_balance_df['num_right'] = trap_balance_df['trap'].apply(lambda x: len(x.split(' - ')[1].split(' ')))

# find the count of unique flasks on each side of the trap
trap_balance_df['unique_left'] = trap_balance_df['trap'].apply(lambda x: len(set(x.split(' - ')[0].split(' '))))
trap_balance_df['unique_right'] = trap_balance_df['trap'].apply(lambda x: len(set(x.split(' - ')[1].split(' '))))

# find the unique flasks left to not be in the unique right and vice versa
trap_balance_df['unique_both'] = trap_balance_df.apply(lambda x: len(set(x['trap'].split(' - ')[0].split(' ')).intersection(set(x['trap'].split(' - ')[1].split(' ')))), axis=1)

# Find the traps that are safe
# 1. Equality: Both sides of the scale must contain the same number of objects.
# 2. Equality: Both sides of the scale must carry exactly the same weight.
# 3. Diversity: All objects on the scale must have different weights. No two objects may have the same weight.
equality_1 = (trap_balance_df['num_left'] == trap_balance_df['num_right'])
equality_2 = (trap_balance_df['sum_left'] == trap_balance_df['sum_right'])
diversity_3 = (trap_balance_df['unique_both'] == 0) & (trap_balance_df['unique_left'] == trap_balance_df['num_left']) & (trap_balance_df['unique_right'] == trap_balance_df['num_right'])
trap_balance_df['safe'] = equality_1 & equality_2 & diversity_3

print(trap_balance_df[trap_balance_df['safe'] == True])
print("count: ", len(trap_balance_df[trap_balance_df['safe'] == True]))

# Export safe traps to a file
trap_balance_df[trap_balance_df['safe'] == True].to_csv('data/13_safe_traps.txt', sep=":", header=None)

# Sum the IDs of the safe traps
print(sum(trap_balance_df[trap_balance_df['safe'] == True].index))



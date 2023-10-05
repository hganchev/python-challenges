# 1.1 The Key Maker - Recipes
# "We will find one Cipher plate in the workshop of the key maker. It is that building over there." Cosmo says.

# As you enter the workshop, you find a room with a collection of special hammers. Cosmo explains:

# "These are the hammers used for forging keys. The keys here inside the temple have unique shapes, unlike the ones we found outside - but there are again six different shapes, so let's assign them capital letters A to F.

# When crafting a new key, the key maker always starts with a base segment A. They utilize different hammers to transform segments into other segments. Each hammer is designed to work on a specific segment and convert it into two new segments. Here is the complete collection of the hammers available:

# 1. A -> BC
# 2. A -> CB
# 3. B -> DD
# 4. B -> BD
# 5. C -> CD
# 6. C -> FE
# 7. D -> AF
# 8. D -> FA
# Let's consider an example of how the key maker could forge a key: Starting with A, they would use the first hammer to transform the A into BC. Then, employing the third hammer, they would convert the B into DD, resulting in the key DDC. Continuing this process, applying the seventh hammer to the second D would yield the key DAFC."

# The list of hammers is given in hammer_collection.txt.

# As you further explore the building, you find another chest, and Cosmo confirms that the cipher plate is inside. Next to the chest, there is a notebook full with hand-written numbers and symbols.

# "This is a recipe book, human. Each line is a recipe. It shows what hammers have to be used on what segment to forge a specific key. Recipes have the form

# (Hammer Index, Position) - (Hammer Index, Position) - ...
# The key DAFC from the example above can be made with the following recipe:

# (1, 1) - (3, 1) - (7, 2)
# It means: apply hammer 1 to position 1, then hammer 3 to position 1, then hammer 7 to position 2."

# "Ok, got it, Cosmo," you say "but how does this help us open the chest?"

# "If we follow the recipe in the book, we will get the key that opens the chest."

# "What do you mean by 'the recipe', Cosmo?" you ask "The book is full of recipes, not just one."

# "The key makers liked to hide their secrets, human. There is only one correct recipe in the book - all other ones are invalid. A recipe is invalid if it contains at least one step that cannot be executed.

# As an example, the recipe

# (1, 1) - (6, 1) - (7, 2)
# is invalid because, in the second step, the sixth hammer requires a letter C, but it is used on a letter B."

# "So that means, I just have to find the one correct recipe, then we can forge the key ourselves?"

# "That's correct, human!"

import pandas as pd
import numpy as np

# Read the hammer collection from hammer_collection.txt to a DataFrame
hammer_collection_df = pd.read_csv('data/hammer_collection.txt', sep=' ', header=None)
hammer_collection_df.index += 1
del hammer_collection_df[0]
del hammer_collection_df[2]
hammer_collection_df.columns = ['hammer', 'segment']

# Read the recipe book from data - 11_keymaker_recipe.txt and make a sequence row by row
with open('data/11_keymaker_recipe.txt') as f:
    recipe_book_df = pd.DataFrame(f.readlines())
recipe_book_df.columns = ['recipe']
recipe_book_df['valid'] = True
recipe_book_df['key'] = np.nan

# Find the valid recipe
valid_recipe = None
for index in recipe_book_df.index:
    recipe = recipe_book_df['recipe'][index]
    recipe_df = pd.DataFrame(recipe.split(' - '), columns=['hammer'])
    recipe_df[['hammer_index', 'position']] = recipe_df['hammer'].str.extract(r'\((\d+), (\d+)\)')
    
    # Add a column to recipe_df to store the segment after each step
    recipe_df['segment'] = np.nan

    # First step - Start with A
    recipe_df['segment'][0] = 'A'

    # next steps - take the segment from the previous step and apply the hammer
    for i, row in recipe_df[0:].iterrows():
        hammer_index = int(row['hammer_index'])
        position = int(row['position'])
        try:
            if(i == 0):
                segment = recipe_df['segment'][i]
            else:
                segment = recipe_df['segment'][i - 1]
            if segment[position - 1] == hammer_collection_df['hammer'][hammer_index]:
                recipe_df['segment'][i] = segment[: position - 1] \
                    + hammer_collection_df['segment'][hammer_index] \
                    + segment[position:]
            else:
                recipe_book_df['valid'][index] = False
                break
        except IndexError:
            recipe_book_df['valid'][index] = False
            break
        except KeyError:
            recipe_book_df['valid'][index] = False
            break
    if recipe_book_df['valid'][index] == True:
        recipe_book_df['key'][index] = recipe_df['segment'][i]


valid_recipes = recipe_book_df[recipe_book_df['valid'] == True]['recipe'].values
print(f'The valid recipe is: {valid_recipes}, \
      index: {recipe_book_df[recipe_book_df["valid"] == True].index}, \
      segment-key: {recipe_book_df[recipe_book_df["valid"] == True]["key"]}, \
      count: {len(recipe_book_df[recipe_book_df["valid"] == True])}')

# AFDFCDAFFE




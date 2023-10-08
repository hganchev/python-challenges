# Chapter 1 - Cosmo Plaza
# As you pass Titan's Gateway, you find yourself standing in the middle of a beautiful garden landscape. The hum of a nearby creek and the gentle rustling of leaves from surrounding trees fill the air, creating a peaceful atmosphere that welcomes all who enter.

# "This is Cosmo Plaza", Cosmo explains, "it was once a popular gathering spot for the alien inhabitants of this temple."

# "Cosmo Plaza... is it named after you, Cosmo?" you ask.

# "Nah, this is pure coincidence. My full name is C.O.S.M.O, which stands for Cybernetic Organism with Sentient Machine Operations. Cosmo Plaza was build long before I was here," Cosmo explains.

# "Let's stay on track, Cosmo. We're here to find that teleporter," you say, focusing on the task at hand. But as soon as you speak the words, you notice a strange expression on your robot companion's face.

# "What's wrong?" you ask.

# "I'm sorry, but I just realized something," Cosmo says, "The way you said that reminded me of someone else who came here years ago. Her name was Nova."

# "Nova? Who is she?" you inquire.

# "Nova Nyquist," Cosmo replies, "She was a remarkable treasure hunter who had many adventures of her own."

# "Nova Nyquist?" you repeat, a sense of disbelief filling your mind, "That's my grandmother!"

# Cosmo nods in confirmation, "Oh, that explains a lot. She used to speak those exact same words you just said - let's stay on track. And in 2358, she had that teleporter accident and was stranded here - just like you. I helped her find the way back."

# "Speaking of which," you interrupt, "Do you have any idea where we might find the teleporter?"

# Cosmo tilts its head slightly, "Well, next, we need to gain access to the inside of the temple building. The entrance is over there. Again, it opens with a 4-digit code on the access panel. The cipher matrix is the same as before, but we need to find new cipher plates. I sense some weak signals. Let me guide you!"

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# Read the cipher matrix from the file cipher_matrix.png and add it to the plot.
cifer_matrix_img = Image.open('cipher_matrix.png')


# Read the cipher plates from the files plate_01.png, plate_02.png and plate_03.png and add them to the plot.
plate_1_img = Image.open('plate_11.png')
# plate_2_img = Image.open('plate_12.png')
# plate_3_img = Image.open('plate_13.png')

# Create a plot with 1 row and 1 column and show the cipher matrix and the cipher plates on top.
cifer_matrix_img_array = np.array(cifer_matrix_img)
plate_1_img_array = np.array(plate_1_img)
# plate_2_img_array = np.array(plate_2_img)
# plate_3_img_array = np.array(plate_3_img)

imgplot = plt.imshow(cifer_matrix_img_array)
imgplot = plt.imshow(plate_1_img_array)
# imgplot = plt.imshow(plate_2_img_array)
# imgplot = plt.imshow(plate_3_img_array)
plt.show()

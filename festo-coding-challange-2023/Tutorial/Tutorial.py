# Titan's Gateway
# After what feels like hours of walking, you and Cosmo finally arrive at the temple. There, towering before you, is the great gate known as Titan's Gateway. You can't help but feel awed by its sheer size and the intricacies of its design.

# Robot Companion
# But then you notice that the gate is closed, blocking your path. "How do we open it?" you ask Cosmo.

# Cosmo focuses its visual sensors on the gate and then back at you. "There's an access panel next to the gate. To open it, you need to input a 4-digit code."

# "How do I get the code?" you ask.

# "There are several cipher plates that you need to find. By aligning the cipher plates in front of the cipher matrix, the correct code will be revealed," Cosmo explains in its synthetic voice.

# You nod, processing this information. "What is the cipher matrix? And where do I find the cipher plates?" you inquire.

# "The cipher matrix - easy. It is engraved on the wall here. The cipher plates – that's where things get tricky," Cosmo says with a series of blinking lights showing its excitment. "They are hidden somewhere nearby. Let me help you find them. My sensors detect some weak signals. Let me see... one cipher plate must be in this workshop over there, one is on top of that hill and a third one is inside the ventilation shaft. Let's go!"

# "Uhm, ok!"

# "No worries, human! I have computed high probabilities of success with you. Humans seem to be quite the puzzle-solvers. By the way, one more thing: there are three plates altogether, but you will only need two of them to open the gate. Any two of the three will do."

# "Why do three plates exist, then, Cosmo? Is there any benefit in collecting all three of them?"

# "Maybe."

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Read the cipher matrix from the file cipher_matrix.png and add it to the plot.
cifer_matrix_img = Image.open('cipher_matrix.png')

# Read the cipher plates from the files plate_01.png, plate_02.png and plate_03.png and add them to the plot.
plate_1_img = Image.open('plate_01.png')
plate_2_img = Image.open('plate_02.png')
plate_3_img = Image.open('plate_03.png')

# Create a plot with 1 row and 1 column and show the cipher matrix and the cipher plates on top.
cifer_matrix_img_array = np.array(cifer_matrix_img)
plate_1_img_array = np.array(plate_1_img)
plate_2_img_array = np.array(plate_2_img)
plate_3_img_array = np.array(plate_3_img)

imgplot = plt.imshow(cifer_matrix_img_array)
imgplot = plt.imshow(plate_1_img_array)
imgplot = plt.imshow(plate_2_img_array)
imgplot = plt.imshow(plate_3_img_array)
plt.show()


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('./euros2_quarter.bmp')

# Create a figure with two subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, threshold1=150, threshold2=255, L2gradient=True)

# Show the image in the first subplot
axs[0][0].imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
axs[0][0].set_title('Edge Detection')
# plt.show()

# Define kernel size for dilation
kernel_size = 20

# Create a kernel for dilation
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

# Dilate the edges
edges = cv2.dilate(edges, kernel)

# Erode the edges
edges = cv2.erode(edges, kernel)

# Apply Gaussian blur
edges = cv2.GaussianBlur(edges, (21, 21), 0)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask to fill the contours in the image
mask = np.zeros_like(edges)

# Fill the contours in the mask
for cnt in contours:
    cv2.fillPoly(mask, [cnt], 255)

# Fill the holes in the mask
mask = cv2.bitwise_not(mask)
mask = cv2.dilate(mask, kernel)
mask = cv2.bitwise_not(mask)

# Apply the mask to the image
masked_image = cv2.bitwise_and(gray, gray, mask=mask)

# Show the image in the first subplot
axs[0][1].imshow(cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB))
axs[0][1].set_title('Fill contours')
# plt.show()

# Find circles with radius using Hough transform
circles = cv2.HoughCircles(masked_image, cv2.HOUGH_GRADIENT, dp=1, minDist=15, param1=190, param2=40, minRadius=15, maxRadius=40)
radiuses = []

# Draw the circles on the image
if circles is not None: 
    for circle in circles[0]:
        radiuses.append(circle[2])
        x, y, r = map(int, circle)
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

# Show the second image in the second subplot
axs[1][0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[1][0].set_title('Find Circles')

# Find the pixel per mm for the the smallest radius
print(radiuses)
ppm = 16.25 / min(radiuses)
print(str(ppm), 'min: ', str(min(radiuses)))

# Coins parameters
refRadius_1Cent = 16.25
rLim_1Cent = 2
color_1Cent = (80,127,255) # coral

refRadius_2Cent = 18.75
rLim_2Cent = 1.2
color_2Cent = (0,140,255) # darkorange

refRadius_5Cent = 21.25
rLimLow_5Cent = -0.8
rLimHigh_5Cent = 2
color_5Cent = (220,20,60) # crimpson

refRadius_10Cent = 19.75
rLimLow_10Cent = 1
rLimHigh_10Cent = 2.1
color_10Cent = (0,215,255) # gold1

refRadius_20Cent = 22.25
rLimLow_20Cent = 0.95
rLimHigh_20Cent = 1.6
color_20Cent = (20,105,139) # goldenrod4

refRadius_50Cent = 24.25
rLimLow_50Cent = -1.1
rLimHigh_50Cent = 1.5
color_50Cent = (255,191,0) # deepskyblue1

refRadius_1Euro = 23.25
rLimLow_1Euro = 0
rLimHigh_1Euro = 2.5
color_1Euro = (139,61,72) # darkslateblue

refRadius_2Euro = 25.75
rLimLow_2Euro = 0
rLimHigh_2Euro = 2.5
color_2Euro = (10,30,255) # 

# Find coins
for circle in circles[0]:
    rad = circle[2]
    x, y, r = map(int, circle)
    actualR = rad*ppm
    print("rad:", rad, "actualR: ", str(actualR))
    if actualR > refRadius_1Cent - rLim_1Cent and actualR < refRadius_1Cent + rLim_1Cent:
        #cv2.putText(image,"1Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_1Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_1Cent, 2)
    elif actualR > refRadius_2Cent - rLim_2Cent and actualR < refRadius_2Cent + rLim_2Cent:
        #cv2.putText(image,"2Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_2Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_2Cent, 2)
    elif actualR > refRadius_5Cent - rLimLow_5Cent and actualR < refRadius_5Cent + rLimHigh_5Cent:
        #cv2.putText(image,"5Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_5Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_5Cent, 2)
    elif actualR > refRadius_10Cent - rLimLow_10Cent and actualR < refRadius_10Cent + rLimHigh_10Cent:
        #cv2.putText(image,"10Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_10Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_10Cent, 2)
    elif actualR > refRadius_20Cent - rLimLow_20Cent and actualR < refRadius_20Cent + rLimHigh_20Cent:
        #cv2.putText(image,"10Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_20Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_20Cent, 2)
    elif actualR > refRadius_50Cent - rLimLow_50Cent and actualR < refRadius_50Cent + rLimHigh_50Cent:
        #cv2.putText(image,"10Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_50Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_50Cent, 2)
    elif actualR > refRadius_1Euro - rLimLow_1Euro and actualR < refRadius_1Euro + rLimHigh_1Euro:
        #cv2.putText(image,"10Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_1Euro, thickness= 3)
        cv2.circle(image, (x, y), r, color_1Euro, 2)
    elif actualR > refRadius_2Euro - rLimLow_2Euro and actualR < refRadius_2Euro + rLimHigh_2Euro:
        #cv2.putText(image,"10Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_2Euro, thickness= 3)
        cv2.circle(image, (x, y), r, color_2Euro, 2)
    else:
        cv2.circle(image, (x, y), r, (255,255,255), 2)

# Show the image in the third subplot
axs[1][1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[1][1].set_title('Coin Detection')

# Display the figure
plt.show()


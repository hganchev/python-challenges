import cv2
import numpy as np

# Load the image
image = cv2.imread('./euros2_quarter.bmp')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 200, 255)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask to fill the contours in the image
mask = np.zeros_like(edges)

# Fill the contours in the mask
for cnt in contours:
    cv2.fillPoly(mask, [cnt], 255)

# Apply the mask to the edges
edges[mask == 0] = 0

# Find circles with radius using Hough transform
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=15, param1=50, param2=30, minRadius=15, maxRadius=50)
radiuses = []

# Draw the circles on the image
if circles is not None:
    for circle in circles[0]:
        x, y, r = map(int, circle)
        radiuses.append(r)
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

# # Show the result
# cv2.imshow('Result', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Find the pixel per mm for the the smallest radius
print(radiuses)
ppm = 16.25 / min(radiuses)
print(str(ppm), 'min: ', str(min(radiuses)))

# Coins parameters
refRadius_1Cent = 16.25
rLim_1Cent = 2
color_1Cent = (250,128,114) # salmon

refRadius_2Cent = 18.75
rLim_2Cent = 0.95
color_2Cent = (255,0,0) # red

refRadius_5Cent = 21.25
refRadius_10Cent = 19.75
refRadius_20Cent = 22.25
refRadius_50Cent = 24.25
refRadius_1Euro = 23.25
refRadius_2Euro = 25.75


# Find coins
for circle in circles[0]:
    x, y, r = map(int, circle)
    actualR = r*ppm
    print("actualR: ", str(actualR))
    if actualR > refRadius_1Cent - rLim_1Cent and actualR < refRadius_1Cent + rLim_1Cent:
        #cv2.putText(image,"1Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_1Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_1Cent, 2)
    elif actualR > refRadius_2Cent - rLim_2Cent and actualR < refRadius_2Cent + rLim_2Cent:
        #cv2.putText(image,"1Cent",(x, y), fontFace= 0, fontScale= 0.5, color = color_2Cent, thickness= 3)
        cv2.circle(image, (x, y), r, color_2Cent, 2)

# Show the result
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


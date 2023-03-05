import cv2
import numpy as np

# Load the image
img = cv2.imread('./euros2_quarter.bmp')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, threshold1=50, threshold2=120, L2gradient=True)

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

# Detect circles using Hough transform
circles = cv2.HoughCircles(masked_image, cv2.HOUGH_GRADIENT, dp=1, minDist=15, param1=190, param2=40, minRadius=15, maxRadius=40)

# Sort circles by size
circles = np.round(circles[0, :]).astype("int")
circles = sorted(circles, key=lambda x: x[2], reverse=True)
print(str(circles))

# Define coin sizes
euro_sizes = {1: (np.arange(18.25 - 1, 18.25 + 1), 1, (80,127,255)), 
              2: (np.arange(25.75 - 1, 25.75 + 1), 2, (0,140,255)), 
              5: (np.arange(23.25 - 1, 23.25 + 1), 5, (220,20,60)), 
              10: (np.arange(19.75 - 1, 19.75 + 1), 10, (0,215,255)), 
              20: (np.arange(22.25 - 1, 22.25 + 1), 20, (20,105,139)), 
              50: (np.arange(24.25 - 1, 24.25 + 1), 50, (255,191,0)), 
              100: (np.arange(30.25 - 1, 30.25 + 1), 100, (139,61,72)), 
              200: (np.arange(25.75 - 1, 25.75 + 1), 200, (10,30,255))}

# Classify each coin
values = []
colors = []
for c in circles:
    # Determine the size of the coin
    r = c[2]
    diam = round(r * 2) * 0.43
    for i in euro_sizes.keys():
        if diam not in euro_sizes[i][0]:
            continue
        # Determine the value of the coin based on its size
        value = euro_sizes[i][1]
        values.append(value)
        color = euro_sizes[i][2]
        colors.append(color)

# Display the sorted coins with their values
for i, c in enumerate(circles):
    if i in range(len(values)):   
        cv2.circle(img, (c[0], c[1]), c[2], colors[i], 2)
        cv2.putText(img, str(values[i]), (c[0]-20, c[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.circle(img, (c[0], c[1]), c[2], (0, 255, 0), 2)

cv2.imshow('Coins', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

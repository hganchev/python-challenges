import cv2
#==================================================================
# if we have a images with the same size we can get a calibration
#==================================================================
def get_calibration(ref_image_path, ref_radius):
    # Load the image
    img = cv2.imread(ref_image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to remove noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Apply Canny edge detection to find edges
    edges = cv2.Canny(blur, 50, 150)

    # Find circles using Hough transform
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is None:
        print("Could not detect reference coin.")
        return None

    # Get the radius of the reference coin
    radius = int(round(circles[0][0][2]))

    # Calculate the pixel/mm calibration
    ppm = ref_radius / radius

    return ppm

# Get pixels per milimeter
ppm = get_calibration('./1Cent.bmp', 16.25)
print(str(ppm))
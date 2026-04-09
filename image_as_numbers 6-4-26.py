import cv2

img = cv2.imread("image.jpg")

print("Shape:", img.shape)
print("Pixel Values (first pixel):", img[0][0])
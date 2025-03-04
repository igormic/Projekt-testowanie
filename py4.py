import cv2

# Wczytanie obrazu w skali szarości
image_gray = cv2.imread("sebek.png", cv2.IMREAD_GRAYSCALE)

# Zapisanie obrazu w skali szarości do nowego pliku
cv2.imwrite("sebek_gray.png", image_gray)
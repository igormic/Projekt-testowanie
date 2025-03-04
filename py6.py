import cv2

# Wczytanie obrazu
image = cv2.imread("sebek.png")

# Tworzenie okna, które można dostosować do rozmiaru ekranu
cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)
cv2.imshow("Obraz", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
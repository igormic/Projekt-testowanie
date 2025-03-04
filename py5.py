import cv2

# Wczytanie obrazów
image1 = cv2.imread("sebek.png")
image2 = cv2.imread("sebek_gray.png")

# Wyświetlenie dwóch obrazów w różnych oknach
cv2.imshow("Obraz 1", image1)
cv2.imshow("Obraz 2", image2)

cv2.waitKey(0)  # Czeka na naciśnięcie klawisza
cv2.destroyAllWindows()  # Zamknięcie wszystkich okien
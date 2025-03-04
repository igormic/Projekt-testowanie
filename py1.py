import cv2

# Wczytanie obrazu z pliku
image = cv2.imread("sebek.png")

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imshow("Wyświetlony obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
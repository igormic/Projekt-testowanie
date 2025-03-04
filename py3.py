import cv2

# Wczytanie obrazu w odcieniach szarości
image_gray = cv2.imread("sebek.png", cv2.IMREAD_GRAYSCALE)

# Wyświetlenie liczby kanałów
(h, w) = image_gray.shape  # Obraz w skali szarości ma tylko dwa wymiary
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: 1')  # Obraz w skali szarości ma tylko jeden kanał
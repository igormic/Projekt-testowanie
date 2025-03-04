import cv2

# Wczytanie obrazu w kolorze
image = cv2.imread("sebek.png")

# Ustalenie wymiarów zdjęcia oraz liczby kanałów
(h, w, c) = image.shape
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')

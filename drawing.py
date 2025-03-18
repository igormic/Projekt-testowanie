import cv2
import numpy as np

image = cv2.imread('cat.jpg')

def zadanie_1():
    img = image.copy()
    height, width = img.shape[:2]
    center = (width // 2, height // 2)
    bottom_right = (width, height)
    blue = (255, 0, 0)
    cv2.line(img, center, bottom_right, blue, 2)
    cv2.imshow('Zadanie 1', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie_2():
    canvas = np.zeros((400, 400, 3), dtype="uint8")
    green = (0, 255, 0)
    red = (0, 0, 255)
    cv2.rectangle(canvas, (0, 0), (100, 50), green, -1)
    cv2.rectangle(canvas, (300, 350), (400, 400), red, 3)
    cv2.imshow('Zadanie 2', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie_3():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    blue = (255, 0, 0)
    red = (0, 0, 255)
    cv2.circle(canvas, (50, 50), 40, blue, -1)
    cv2.circle(canvas, (150, 150), 60, red, -1)
    cv2.imshow('Zadanie 3', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie_4():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    center = (150, 150)
    white = (255, 255, 255)
    cv2.rectangle(canvas, (100, 100), (200, 200), white, 1)
    cv2.circle(canvas, center, 30, white, 1)
    cv2.imshow('Zadanie 4', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie_5():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    center = (150, 150)
    white = (255, 255, 255)
    for size in range(0, 150, 20):
        top_left = (center[0] - size // 2, center[1] - size // 2)
        bottom_right = (center[0] + size // 2, center[1] + size // 2)
        cv2.rectangle(canvas, top_left, bottom_right, white, 1)
    cv2.imshow('Zadanie 5', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie_6():
    img = image.copy()
    eye1 = (100, 100)
    eye2 = (150, 100)
    mouth = (125, 150)
    face_center = (125, 125)
    face_radius = 80

    cv2.circle(img, eye1, 10, (0, 0, 255), -1)
    cv2.circle(img, eye2, 10, (0, 0, 255), -1)

    cv2.rectangle(img, (mouth[0] - 20, mouth[1] - 10), (mouth[0] + 20, mouth[1] + 10), (0, 255, 0), -1)

    cv2.circle(img, face_center, face_radius, (255, 0, 0), 2)

    cv2.imshow('Zadanie 6', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

zadanie_1()
zadanie_2()
zadanie_3()
zadanie_4()
zadanie_5()
zadanie_6()

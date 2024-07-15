import numpy as np
import matplotlib.pyplot as plt
import PTL.Image as Image
import os
import cv2

class DataProcessing:
    def __init__(self, path):
        self.path = path

    def load_image(self):
        image = cv2.imread(self.path)
        return image

    def resize_image(self, image, size):
        image = cv2.resize(image, size)
        return image

    def show_image(self, image):
        plt.imshow(image)
        plt.show()

    def save_image(self, image, path):
        cv2.imwrite(path, image)

    def convert_to_gray(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def threshold_image(self, image, threshold):
        ret, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        return thresh

    def find_contours(self, image):
        contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def draw_contours(self, image, contours):
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        return image

    def get_contour_area(self, contour):
        area = cv2.contourArea(contour)
        return area

    def get_contour_perimeter(self, contour):
        perimeter = cv2.arcLength(contour, True)
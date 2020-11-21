import os
from PIL import Image
import numpy as np
from keras_preprocessing.image import img_to_array, load_img


def image_preprocessing(image_path):
    image = load_img(image_path)
    image = image.resize((128, 128), Image.LANCZOS)
    image = img_to_array(image)
    image /= 255.0
    return image


class MaskData:
    def __init__(self):
        self.image_dir = os.path.join(os.getcwd(), 'RMFD', 'self-built-masked-face-recognition-dataset')
        print('Data loader from {}'.format(self.image_dir))

    def load_data(self):
        self.X = []
        self.y = []
        positive_image_dir = os.path.join(self.image_dir, 'AFDB_masked_face_dataset')
        negative_image_dir = os.path.join(self.image_dir, 'AFDB_face_dataset')
        positive_dir_count = len(os.listdir(positive_image_dir))
        current_positive_dir = 1
        for filename in os.listdir(positive_image_dir):
            print('Loading positive image {} / {}'.format(current_positive_dir, positive_dir_count))
            positive_image_dir_second = os.path.join(positive_image_dir, filename)
            for image_name in os.listdir(positive_image_dir_second):
                image_path = os.path.join(positive_image_dir_second, image_name)
                image = image_preprocessing(image_path)
                self.X.append(image)
                self.y.append(1)
                del image
            current_positive_dir += 1
        negative_dir_count = len(os.listdir(negative_image_dir))
        current_negative_dir = 1
        for filename in os.listdir(negative_image_dir):
            print('Loading negative image {} / {}'.format(current_negative_dir, negative_dir_count))
            negative_image_dir_second = os.path.join(negative_image_dir, filename)
            for image_name in os.listdir(negative_image_dir_second):
                image_path = os.path.join(negative_image_dir_second, image_name)
                image = image_preprocessing(image_path)
                self.X.append(image)
                self.y.append(0)
                del image
            current_negative_dir += 1

        print('Load {} images. \nPositive: {}\nNegative: {}'
              .format(len(self.X), self.y.count(1), self.y.count(0)))
        count_positive = 0
        count_negative = 0
        X_balanced = []
        y_balanced = []
        balanced_length = min(self.y.count(0), self.y.count(1))
        for i in range(len(self.y)):
            if self.y[i] == 1 and count_positive < balanced_length:
                X_balanced.append(self.X[i])
                y_balanced.append(self.y[i])
                count_positive += 1
            elif self.y[i] == 0 and count_negative < balanced_length:
                X_balanced.append(self.X[i])
                y_balanced.append(self.y[i])
                count_negative += 1
        self.X = np.array(X_balanced)
        self.y = y_balanced
        print('{} images after balanced.\nPositive: {}\nNegative: {}'
              .format(len(self.X), self.y.count(1), self.y.count(0)))
        return self.X, self.y

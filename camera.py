import cv2
from PIL import Image


class camera:
    def __init__(self, size=(1280, 720)):
        self.width = size[0]
        self.height = size[1]
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.capture.set(3, self.width)  # width
        self.capture.set(4, self.height)  # height

    def show_video(self):
        while self.capture.isOpened():
            status, frame = self.capture.read()
            cv2.imshow('video', frame)
            k = cv2.waitKey(1)

    def get_frame(self):
        if self.capture.isOpened():
            status, frame = self.capture.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = Image.fromarray(frame)
            frame = frame.toqpixmap()
            k = cv2.waitKey(1)
            return frame


if __name__=="__main__":
    my_camera = camera()
    my_frame = my_camera.get_frame()
    cv2.imshow('frame', my_frame)
    k = cv2.waitKey(1000)

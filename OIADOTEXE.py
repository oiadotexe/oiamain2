import cv2
import os

class VideoToAscii:
    def __init__(self, video_path, width=80, height=40):
        self.video_path = video_path
        self.width = width
        self.height = height
        self.video_capture = cv2.VideoCapture(video_path)

    def __pixel_to_ascii(self, pixel):
        chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
        gray = 0.2989 * pixel[2] + 0.5870 * pixel[1] + 0.1140 * pixel[0]
        return chars[int(gray / 256 * len(chars))]

    def __frame_to_ascii(self, frame, divider=8):
        ascii_list = []
        ascii_frame = ""
        frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)
        for index, row in enumerate(frame, start=1):
            for pixel in row:
                ascii_frame += self.__pixel_to_ascii(pixel)
            ascii_frame += "\n"
        ascii_list.append(ascii_frame)
        return ascii_list

    def __load_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            return None
        return frame

    def display_video_ascii(self):
        while True:
            frame = self.__load_frame()
            if frame is None:
                break
            ascii_frame = self.__frame_to_ascii(frame)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n".join(ascii_frame), flush=True)

if __name__ == "__main__":
    video_path = "oia.mp4"
    video_to_ascii = VideoToAscii(video_path, width=80, height=40)
    video_to_ascii.display_video_ascii()

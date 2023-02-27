import cv2
import numpy



class ImageProcess:
    def __init__(self):
        print("...start...\n\n")


    def run(self, frame, matrix, kernel):
        frame_info = frame.shape
        self.frame_screen_height = int(frame_info[0]) + 1
        self.frame_screen_height_numpy = numpy.arange(self.frame_screen_height + 1)

        self.frame_screen_width = int(frame_info[1]) + 1
        self.frame_screen_width_numpy = numpy.arange(self.frame_screen_width + 1)

        self.frame = frame
        self.matrix = matrix
        self.kernel = kernel

        self.kernel1 = kernel[0]
        self.kernel2 = kernel[1]
        self.kernel3 = kernel[2]

        self.loc1 = (0, 0)
        self.loc2 = (0, 0)
        self.loc3 = (0, 0)
        self.loc4 = (0, 0)
        self.loc5 = (0, 0)
        self.loc6 = (0, 0)
        self.loc7 = (0, 0)
        self.loc8 = (0, 0)
        self.loc9 = (0, 0)


        for height in range(self.frame_screen_height):
            for weight in range(self.frame_screen_width):
                self.index_parse(height + 1, weight +1)
                self.process(height + 1, weight + 1)


    def index_parse(self, index_x, index_y):
        self.loc1 = (index_x - 1, index_y)
        self.loc2 = (index_x - 1, index_y - 1)
        self.loc3 = (index_x, index_y - 1)
        self.loc4 = (index_x + 1, index_y - 1)
        self.loc5 = (index_x + 1, index_y)
        self.loc6 = (index_x + 1, index_y + 1)
        self.loc7 = (index_x, index_y + 1)
        self.loc8 = (index_x - 1, index_y + 1)
        self.loc9 = (index_x, index_y)

    def pixel_show(self, pixel_xy):
        pixel_x = pixel_xy[0]
        pixel_y = pixel_xy[1]
        pixels = None
        try:
            pixels = self.frame[pixel_x, pixel_y]
        except:
            pass
        return pixels

    def filter_sum(self, *args):
        try:
            return numpy.sum(args)
        except:
            pass

    def filter_multiply(self, multiply_x, multiply_y):
        try:
            return numpy.multiply(multiply_x, multiply_y)
        except:
            pass

    def process(self, x, y):
        self.x = x
        self.y = y

        self.data_loc1 = self.filter_multiply(self.pixel_show(self.loc1), self.kernel1[1])
        self.data_loc2 = self.filter_multiply(self.pixel_show(self.loc2), self.kernel1[0])
        self.data_loc3 = self.filter_multiply(self.pixel_show(self.loc3), self.kernel2[0])
        self.data_loc4 = self.filter_multiply(self.pixel_show(self.loc4), self.kernel3[0])
        self.data_loc5 = self.filter_multiply(self.pixel_show(self.loc5), self.kernel3[1])
        self.data_loc6 = self.filter_multiply(self.pixel_show(self.loc6), self.kernel3[2])
        self.data_loc7 = self.filter_multiply(self.pixel_show(self.loc7), self.kernel2[2])
        self.data_loc8 = self.filter_multiply(self.pixel_show(self.loc8), self.kernel1[2])
        self.data_loc9 = self.filter_multiply(self.pixel_show(self.loc9), self.kernel2[1])

        total = self.filter_sum(self.data_loc1, self.data_loc2, self.data_loc3,
                                self.data_loc4, self.data_loc5, self.data_loc6,
                                self.data_loc7, self.data_loc8, self.data_loc9)
        try:
            total = int(total / 9)
            self.frame[self.x, self.y] = (int(total))
        except:
            pass


    def show(self):

        cv2.imshow("live", frame)
        cv2.imshow("live2", frame_orginal)




video = cv2.VideoCapture("2.mp4")
video_process_object = ImageProcess()

while True:
    ret, frame = video.read()
    ret_, frame_orginal = video.read()

    frame = cv2.resize(frame, (500, 300))
    frame_orginal = cv2.resize(frame_orginal, (500, 300))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    video_process_object.run(
        frame,
        3,
        [ [1,1,1], [1,1,1], [1,1,1] ]
    )
    video_process_object.show()

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
frame.release()
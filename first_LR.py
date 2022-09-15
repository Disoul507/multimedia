import cv2
# windows to display image
#cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
#cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow("Image", cv2.WINDOW_KEEPRATIO)
# read image
#cv.imread(filename[, flags]) -> retval
#image = cv2.imread('E:/new/photo/sheet.jpg')
#image = cv2.imread('E:/new/photo/sky.png')
#image = cv2.imread('E:/new/photo/kuzia.bmp')
# show image
#cv2.imshow("Image", image)
# exit at closing of window
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# cv2.namedWindow('frame')
# cap = cv2.VideoCapture(r'E:/new/photo/mov.mp4', cv2.CAP_ANY)
# while (True):
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break


def readIPWriteTOFile():
    cv2.namedWindow('img')
    video = cv2.VideoCapture(0)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.mov", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()
        cv2.imshow('img', img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    video.release()
    cv2.destroyAllWindows()

def print_cam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # When everything done, release the capture


readIPWriteTOFile()
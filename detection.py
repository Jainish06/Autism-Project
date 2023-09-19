import cv2
import numpy as np

# specifying source of camera
video_cap = cv2.VideoCapture(0)
p_circle = None
dist = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

# cv window
while True:
    # getting frame of the video
    ret, frame = video_cap.read()
    if not ret: break

    # converting frame to grayscale and blurring it.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (17,17), 0)

    # using Hough circles to detect circles in frame.
    circles = cv2.HoughCircles(blur_frame, cv2.HOUGH_GRADIENT, 1.2, 100, 1, 100, 30,
                               75, 400)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if p_circle is not None:
                if dist(chosen[0],chosen[1],p_circle[0],p_circle[1]) <= dist(i[0],i[1],p_circle[0],p_circle[1]):
                    chosen = i
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0,100,100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (0,0,139), 3)
        p_circle = chosen
    # printing list of circles
    print(circles)

    cv2.imshow("Game", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video_cap.release()
cv2.destroyAllWindows()

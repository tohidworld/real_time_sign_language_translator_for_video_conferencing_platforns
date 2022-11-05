import pyvirtualcam
import cv2

cap = cv2.VideoCapture(0)
fmt = pyvirtualcam.PixelFormat.BGR
with pyvirtualcam.Camera(width=640, height=480, fps=30, fmt=fmt) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        ret_val, frame = cap.read()
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.BORDER_DEFAULT)
        #cv2.imshow('my webcam', frame)
        cam.send(frame)
        cam.sleep_until_next_frame()
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()
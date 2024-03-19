from ultralytics import YOLO
import cv2

model = YOLO('yolo-weights/yolov9e.pt')
result = model('Images/bus.jpg', show=True)
cv2.waitKey(0)

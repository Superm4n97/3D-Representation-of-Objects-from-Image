from types import LambdaType
import cv2 as cv
import numpy as np
from numpy.core.defchararray import center

# Load Yolo
path =r"C:\Users\Superm4n\Desktop\YOLO"
weight = path+r"\yolov3-320\yolov3.weights"
cfg = path+r"\yolov3-320\yolov3.cfg"
net = cv.dnn.readNetFromDarknet(cfg,weight)
classes = []
with open(path+"\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

#print(classes)

def getCenterPoints(img):
    height,width,_ = img.shape

    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layers_outputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layers_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)

            if class_id != 0:
                continue

            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv.FONT_HERSHEY_PLAIN

    points = []

    if (len(indexes) > 0):
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence_str = str(round(confidences[i],2))

            #color = colors[i] #Random Color
            color = (0,255,0)

            cv.rectangle(img,(x,y),(x+w, y+h), color, 2)
            points.append((int((x+x+w)/2),int((y+y+h)/2)))
            #cv.putText(img, label + " " + confidence_str, (x,y+20), font, 2, (255,255,255), 2)

    #cv.imshow("win",img)
    #cv.waitKey(0)
    return points
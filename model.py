import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO

model1 = YOLO('yolov10s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('test1.mp4')

with open("coco.txt", "r") as my_file:
    data = my_file.read()
class_list = data.split("\n")

# Define all areas and their metadata
areas = [
    [(40, 77), (118, 77), (118, 164), (40, 164)],
    [(118, 77), (210, 77), (210, 164), (118, 164)],
    [(210, 77), (314, 77), (314, 164), (210, 164)],
    [(314, 77), (426, 77), (426, 164), (314, 164)],
    [(426, 77), (517, 77), (517, 164), (426, 164)],
    [(517, 77), (615, 77), (615, 164), (517, 164)],
    [(615, 77), (712, 77), (712, 164), (615, 164)],
    [(718, 366), (718, 452), (616, 452), (616, 366)],
    [(616, 366), (616, 452), (520, 452), (520, 366)],
    [(520, 366), (520, 452), (425, 452), (425, 366)],
    [(425, 366), (425, 452), (321, 452), (321, 366)],
    [(321, 366), (321, 452), (210, 452), (210, 366)]
]

# Pre-convert areas to numpy arrays
area_arrays = [np.array(area, np.int32) for area in areas]

# Spot label positions for drawing
spot_labels = [
    (50, 441), (106, 440), (175, 436), (250, 436), (315, 429),
    (386, 421), (456, 414), (527, 406), (591, 398), (649, 384),
    (697, 377), (752, 371)
]

# Valid classes to detect
valid_classes = {'car', 'cell phone', 'bottle'}




while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (1020, 500))

    results = model1.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    
    # Use a list of lists instead of 12 separate variables
    spot_counts = [[] for _ in range(12)]
    
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        
        # Check if class contains any valid class name (preserving original substring matching)
        if any(valid_class in c for valid_class in valid_classes):
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            
            # Check area1 first (original code draws text only for area1)
            drawn = False
            if cv2.pointPolygonTest(area_arrays[0], (cx, cy), False) >= 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                cv2.putText(frame, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                spot_counts[0].append(c)
                drawn = True
            
            # Check remaining areas (draw rectangle/circle but no text)
            for area_idx in range(1, 12):
                if cv2.pointPolygonTest(area_arrays[area_idx], (cx, cy), False) >= 0:
                    if not drawn:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                        drawn = True
                    spot_counts[area_idx].append(c)
    
    # Calculate counts for each spot
    counts = [len(spot_list) for spot_list in spot_counts]
    occupied = sum(counts)
    space = 12 - occupied
    print(space)
    
    # Draw all spots using a loop
    for spot_idx, (count, area_array, label_pos) in enumerate(zip(counts, area_arrays, spot_labels), 1):
        if count == 1:
            cv2.polylines(frame, [area_array], True, (0, 0, 255), 2)
            cv2.putText(frame, str(spot_idx), label_pos, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
            print(f"Spot {spot_idx} is filled")
        else:
            cv2.polylines(frame, [area_array], True, (0, 255, 0), 2)
            cv2.putText(frame, str(spot_idx), label_pos, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.putText(frame, str(space), (23, 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
    
    cv2.imshow("RGB", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


from ultralytics import YOLO
import cv2
import numpy as np
import supervision as sv
from pathlib import Path
import logging

logging.getLogger("ultralytics").setLevel(logging.ERROR)

def webcam_detection(model_path, gun_threshold=0.7, knife_threshold=0.4):
    """
    Run real-time weapon detection on webcam feed with class-specific confidence thresholds
    """
    # Load the trained model
    model = YOLO(model_path)
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)  # Use 0 for default webcam
    
    # Initialize annotator
    box_annotator = sv.BoxAnnotator(thickness=2)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Run inference
        results = model(frame)[0]
        
        # Extract bounding boxes, class ids, and confidence scores
        boxes = results.boxes.xyxy.cpu().numpy()  # Bounding boxes
        confidences = results.boxes.conf.cpu().numpy()  # Confidence scores
        class_ids = results.boxes.cls.cpu().numpy().astype(int)  # Class IDs
        
        # Separate valid detections based on class-specific thresholds
        valid_indices = [
            i for i, (class_id, confidence) in enumerate(zip(class_ids, confidences))
            if (class_id == 0 and confidence >= gun_threshold) or (class_id == 1 and confidence >= knife_threshold)
        ]
        
        # Filtered bounding boxes, confidences, and class IDs based on class-specific thresholds
        filtered_boxes = boxes[valid_indices]
        filtered_confidences = confidences[valid_indices]
        filtered_class_ids = class_ids[valid_indices]
        
        # Convert filtered detections to supervision format
        detections = sv.Detections(
            xyxy=filtered_boxes,
            confidence=filtered_confidences,
            class_id=filtered_class_ids
        )
        
        # Annotate frame with filtered detections
        frame = box_annotator.annotate(
            scene=frame,
            detections=detections
        )
        
        # Draw labels for each detection
        for i in range(len(filtered_class_ids)):
            class_id = filtered_class_ids[i]
            confidence = filtered_confidences[i]
            label = f"{model.names[class_id]} {confidence:.2f}"
            x1, y1, x2, y2 = filtered_boxes[i].astype(int)
            cv2.putText(
                frame, label, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2
            )
        
        # Display the frame
        cv2.imshow('Weapon Detection', frame)
        
        # Break loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    # Run webcam detection with class-specific confidence thresholds
    webcam_detection(
        model_path=r'best.pt',
        gun_threshold=0.7,
        knife_threshold=0.4
    )

if __name__ == "__main__":
    main()

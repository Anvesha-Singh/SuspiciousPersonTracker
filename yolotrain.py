from ultralytics import YOLO
import yaml
import os
import cv2
import numpy as np
import supervision as sv
from pathlib import Path

def create_dataset_yaml(dataset_dir):
    names = ['gun', 'knife']  # Class names in order of class ids (0: gun, 1: knife)
    
    data = {
        'train': str(Path(dataset_dir) / 'train' / 'images'),
        'val': str(Path(dataset_dir) / 'val' / 'images'),
        'test': str(Path(dataset_dir) / 'test' / 'images'),
        'names': names,
        'nc': len(names)
    }
    
    with open('dataset.yaml', 'w') as f:
        yaml.dump(data, f)
    
    return 'dataset.yaml'

def train_weapon_detector(dataset_dir, epochs=5, imgsz=640, batch_size=8):
    """
    Train YOLOv8 model for knife and gun detection
    """
    # Create dataset configuration
    dataset_yaml = create_dataset_yaml(dataset_dir)
    
    # Initialize YOLOv8 model
    model = YOLO('yolov8n.pt')
    
    # Train the model
    results = model.train(
        data=dataset_yaml,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch_size,
        patience=20,        # Early stopping
        save=True,         
        device='cpu'       # Use 'cpu' for laptop without GPU, '0' for GPU
    )
    
    return model

def main():
    # Train model (uncomment to train)
    model = train_weapon_detector(r"C:\Users\anves\Downloads\Weapon 2.v2i.yolov8")

if __name__ == "__main__":
    main()
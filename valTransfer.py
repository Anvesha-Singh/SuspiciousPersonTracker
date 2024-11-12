#Code to create Validation Dataset
import os
import random
import shutil

# Set paths
data_path = r"C:\Users\anves\Downloads\Weapon 2.v2i.yolov8\train"  # Update to your dataset path
images_path = os.path.join(data_path, 'images')
labels_path = os.path.join(data_path, 'labels')

# Define val directory structure
val_images_path = os.path.join(data_path, 'val', 'images')
val_labels_path = os.path.join(data_path, 'val', 'labels')
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# Set validation split ratio (e.g., 20% of data for validation)
val_ratio = 0.2
total_images = os.listdir(images_path)
val_count = int(len(total_images) * val_ratio)

# Randomly sample images for validation
val_images = random.sample(total_images, val_count)

# Move images and corresponding labels to the validation folder
for img_file in val_images:
    # Define image and label paths
    img_source = os.path.join(images_path, img_file)
    label_source = os.path.join(labels_path, os.path.splitext(img_file)[0] + '.txt')

    # Define destination paths
    img_dest = os.path.join(val_images_path, img_file)
    label_dest = os.path.join(val_labels_path, os.path.splitext(img_file)[0] + '.txt')

    # Move files to validation folder
    shutil.move(img_source, img_dest)
    shutil.move(label_source, label_dest)

print(f"Moved {val_count} images and labels to the validation folder.")
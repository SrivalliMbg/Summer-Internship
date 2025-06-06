from ultralytics import YOLO
import os
import cv2

model = YOLO("yolov8n-seg.pt")

input_folder= "video_segmentation/extracted_frames"
output_folder= "video_segmentation/segmented_frames"
  
os.makedirs(output_folder, exist_ok=True)

for img_file in sorted(os.listdir(input_folder)):
  if img_file.lower().endswith((".jpg",".jpeg",".png")):
    img_path = os.path.join(input_folder, img_file)
    model.predict(
       source=img_path,
       save=True,
       project=output_folder,
       name=" ",
       exist_ok=True
      )

print("Image Segmentation Completed.")

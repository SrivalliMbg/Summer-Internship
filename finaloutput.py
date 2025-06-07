import cv2 
import os 

folder =  "frames"
images = sorted([img for img in os.listdir(folder) if img.endswith(".jpg")])

if not images:
    print("no images found")
    exit()
 
frame = cv2.imread(os.path.join(folder, images[0]))
if frame is None:
    print("Error")
    exit()
    
height, width, _ = frame.shape

video = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

for image in images:
    img_path = os.path.join(folder, image)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Warning: could not read {img_path}, skipping ")
        continue
    video.write(img)
    
video.release()
print("video is saved ")

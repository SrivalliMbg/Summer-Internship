import os

folder = "extracted_frames"
files = sorted([f for f in os.listdir(folder) if f.endswith(".jpg")])
for i, filename in enumerate(files):
   new_name = f"frame_{i+1:04}.jpg"
   os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
   
print("Renaming Complete")















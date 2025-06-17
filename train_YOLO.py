from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="/home/vboxuser/Downloads/African-wildlife/African-wildlife.yaml",
    epochs=20,
    imgsz=640,
    project="African-wildlife-project",
    name="exp"
)



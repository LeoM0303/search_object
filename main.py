#pip install ultralytics

from ultralytics import YOLO
from collections import Counter
from pathlib import Path

#detect
def detect_object(model: YOLO, image_path:str) -> None:
    print('[INFO] Start of recognizing objects')
    result = model(image_path, verbose=False)[0]

    if result.names and result.boxes is not None:
        labels = result.boxes.cls.tolist()

        label_names = [result.names[int(cls)] for cls in labels]

        counts = Counter(label_names)

        print("[INFO] Find object: ")
        for label, count in counts.items():
            print(f'[+] {label}: {count}]')
        else:
            print('[!] Object not found')

        save_path = result.save(filename=f"RESULT_{Path(image_path).stem}.png")
        print(f'[+] Result of saving in file: {save_path}')
#main part
def main():
    model = YOLO('yolo11n.pt')

    detect_object(model, 'IMAGES/img_3.png')

    ## Train the model on the COCO8 example dataset for 100 epochs
    #results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

if __name__ == '__main__':
    main()
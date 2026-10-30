# Training a YOLO detector

This folder contains a starter pipeline for **object detection**, matching the
`YOLO("yolo26n.pt")` model used in the project. It does not train on the sample
bus image: you need to supply and label your own images first.

## 1. Install the training dependency

From the repository root, activate your virtual environment and run:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-training.txt
```

If PowerShell blocks activation, run the commands using the virtual environment's
Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-training.txt
```

## 2. Add and label images

Put each image in one of these folders and create a YOLO-format label file with
the same filename in the matching `labels` folder:

```text
training/
  data.yaml
  train.py
  dataset/
    images/
      train/
      val/
      test/
    labels/
      train/
      val/
      test/
```

For example, `images/train/photo01.jpg` must have a corresponding
`labels/train/photo01.txt`. Use an annotation tool that can export **YOLO
Detection** labels (for example, CVAT or Roboflow). Each line in a label file
represents one bounding box:

```text
class_id x_center y_center width height
```

The four coordinates are normalized from 0 to 1 relative to the image size.
Class IDs start at 0. Images with no target objects can have an empty `.txt`
label file. Split images into train, validation, and test sets (for example
70% / 20% / 10%); keep near-duplicate photos in the same split to avoid
misleading validation results.

## 3. Set your classes

Edit [`data.yaml`](./data.yaml). Replace `object` with the name of the class you
annotate. For multiple classes, add each class with its zero-based ID:

```yaml
names:
  0: egg
  1: other
```

The IDs in the annotation files must match these IDs. If your goal is to detect
individual eggs, label each egg as a separate box and use `egg` as the class.
Choose a different class or task if you want to detect something else. YOLO
detection finds objects and their locations; it does not read arbitrary text
from images (OCR).

## 4. Train

Run this from the repository root:

```powershell
python training\train.py
```

The starter script fine-tunes the project's `yolo26n.pt` weights for 100 epochs
at 640px. If those weights are not present, download the official compatible
Ultralytics weights or choose another compatible detection model:

```powershell
python training\train.py --model yolo26n.pt --epochs 100 --imgsz 640 --batch 16
```

You can select a GPU (`--device 0`) or force CPU (`--device cpu`). Reduce
`--batch` (for example, to 8 or 4) if you run out of GPU memory. Training
outputs are saved under `training/runs/ovitrampas/`; the best weights are
`training/runs/ovitrampas/weights/best.pt`.

## 5. Use and evaluate the trained model

Run inference on a new image:

```powershell
yolo predict model=training/runs/ovitrampas/weights/best.pt source=path\to\new-image.jpg
```

If you created a test split, evaluate against it after training:

```powershell
yolo val model=training/runs/ovitrampas/weights/best.pt data=training/data.yaml split=test
```

Review the predictions and validation metrics. If results are poor, check the
labels and class IDs first, then add representative, consistently labeled
images. Keep training images, labels, and generated weights out of Git; the
repository ignores these files by default.

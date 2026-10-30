import argparse
from pathlib import Path

from ultralytics import YOLO


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a YOLO object detector.")
    parser.add_argument("--data", type=Path, default=ROOT / "training" / "data.yaml")
    parser.add_argument("--model", type=Path, default=ROOT / "yolo26n.pt")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--device", default=None, help="For example: 0, cpu")
    parser.add_argument("--name", default="ovitrampas")
    args = parser.parse_args()

    model = YOLO(str(args.model))
    model.train(
        data=str(args.data),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        project=str(ROOT / "training" / "runs"),
        name=args.name,
    )


if __name__ == "__main__":
    main()

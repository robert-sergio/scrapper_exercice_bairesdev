import os
import pathlib
from ultralytics import YOLO


class Detection:

    def __init__(self) -> None:
        self.confidence = 0.4
        if os.name == "posix":
            pt_path = (
                "file://"
                + str(pathlib.Path(__file__).parent.resolve())
                + "/config/yolov8n.pt"
            )
        else:
            pt_path = (
                str(pathlib.Path(__file__).parent.resolve()) + "/config/yolov8n.pt"
            )
        self.model = YOLO(pt_path)

    def check(self, img, object_names):
        for result in self.model(img, stream=False):
            result.boxes
            if result.summary() is None:
                os.remove(result.path)
                return False

            if len(result.summary()) == 0:
                os.remove(result.path)
                return False
            name = result.summary()[0].get("name")
            confidence = round(result.summary()[0].get("confidence"), 2)
            if name not in object_names:
                continue

            if confidence > self.confidence:
                os.remove(result.path)
                return True

        os.remove(result.path)
        return False


if __name__ == "__main__":
    check = Detection()

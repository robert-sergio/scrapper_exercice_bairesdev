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
        try:
            results = self.model(img, stream=False)
        except Exception as ex:
            return False

        for result in results:
            result.boxes
            if result.summary() is None:
                return False

            if len(result.summary()) == 0:
                return False
            name = result.summary()[0].get("name")
            confidence = round(result.summary()[0].get("confidence"), 2)
            if name not in object_names:
                continue

            if confidence > self.confidence:
                return True

        return False


if __name__ == "__main__":
    check = Detection()

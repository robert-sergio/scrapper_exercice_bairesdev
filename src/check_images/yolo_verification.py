import os
import pathlib
from ultralytics import YOLO


class Detection:

    def __init__(self) -> None:
        self.confidence = 0.7
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
        for result in self.model(img):
            result.boxes
            name = result.summary()[0].get("name")
            confidence = round(result.summary()[0].get("confidence"), 2)
            if name in object_names and confidence > self.confidence:
                os.remove(result.path)
                return True

        os.remove(result.path)
        return False


if __name__ == "__main__":
    check = Detection()
    check.check(
        img="https://img.freepik.com/free-photo/isolated-happy-smiling-dog-white-background-portrait-4_1562-693.jpg",
        # "C:\\Users\\mirla\\OneDrive\\Documentos\\CODES\\scrapper_exercice_bairesdev\\src\\check_images\\imgs\\dog.jpg",
        object_names=["dog"],
    )

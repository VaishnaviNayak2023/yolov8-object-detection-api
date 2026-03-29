from fastapi import FastAPI
from pydantic import BaseModel
from app.detector import YOLODetector
from app.utils import decode_image, encode_image

app = FastAPI()
detector = YOLODetector()

class ImageRequest(BaseModel):
    image: str  # base64 string

@app.get("/")
def home():
    return {"message": "YOLOv8 Object Detection API"}

@app.post("/detect")
def detect_objects(request: ImageRequest):
    frame = decode_image(request.image)

    detections, results = detector.detect(frame)
    annotated = detector.draw_boxes(frame, results)

    encoded_img = encode_image(annotated)

    return {
        "detections": detections,
        "image": encoded_img
    }
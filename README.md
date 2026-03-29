# YOLOv8 Object Detection API

A fast and lightweight Object Detection API built using FastAPI, YOLOv8, and OpenCV.
This API allows users to upload images and receive real-time object detection results with bounding boxes.

---

## Features

* FastAPI-based REST API
* YOLOv8 object detection
* Direct image upload (no base64 required)
* Modular and clean code structure
* Easy local setup
* Extendable for production use

---

## Tech Stack

* Python 3.8+
* FastAPI
* OpenCV
* Ultralytics YOLOv8
* Uvicorn

---

## Project Structure

```id="ojx0ny"
yolov8-object-detection-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # API entry point
│   ├── detector.py      # YOLOv8 detection logic
│   └── utils.py         # helper functions
│
├── models/              # optional model storage
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash id="f9xqpd"
git clone https://github.com/VaishnaviNayak2023/yolov8-object-detection-api.git
cd yolov8-object-detection-api
```

---

### 2. Create Virtual Environment

Windows:

```bash id="3h63jy"
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash id="y2jwmo"
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash id="n42f53"
pip install -r requirements.txt
```

---

## Running the API

```bash id="rbj1c3"
python -m uvicorn app.main:app --reload
```

Expected output:

```id="2dw8jw"
Uvicorn running on http://127.0.0.1:8000
```

---

## API Endpoints

### Home

```id="lrb4yt"
GET /
```

### Detect Objects

```id="0qynl2"
POST /detect
```

* Input: Image file (JPG/PNG)
* Output: Detected objects with bounding boxes

---

## Testing the API

1. Open:

```id="z7bnhw"
http://127.0.0.1:8000/docs
```

2. Select `POST /detect`
3. Click "Try it out"
4. Upload an image
5. Click "Execute"

---

## Example Response

```json id="2m9p6h"
{
  "detections": [
    {
      "label": "person",
      "confidence": 0.91,
      "bbox": [120, 60, 300, 420]
    }
  ],
  "message": "Detection successful"
}
```

---

## Model Details

* Default model: `yolov8n.pt`
* Automatically downloaded on first run

---

## Common Issues

### Import Errors

Run from the project root:

```bash id="ew8bxg"
python -m uvicorn app.main:app --reload
```

### Model Not Downloading

Ensure internet connection is available.

### Slow Performance

* Use GPU (CUDA)
* Use smaller model

---

## Future Improvements

* Real-time video detection
* Cloud deployment (AWS, GCP, Render)
* Detection dashboard
* GPU acceleration
* Custom model training

---

## Contributing

Contributions are welcome. Please open an issue before making major changes.

---

## License

MIT License

---

## Author

Vaishnavi Nayak
https://github.com/VaishnaviNayak2023

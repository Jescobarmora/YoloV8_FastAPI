from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import numpy as np
import cv2

# Inicializar la aplicación FastAPI
app = FastAPI()

# Cargar el modelo YOLOv8 preentrenado
model = YOLO('yolov8n.pt')

# Ruta de prueba para verificar que la API esté en funcionamiento
@app.get("/")
def read_root():
    return {"message": "API de detección de objetos con YOLOv8"}

# Ruta para detectar objetos en una imagen
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    # Leer la imagen desde el archivo cargado
    file_bytes = np.frombuffer(await file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convertir la imagen de BGR a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Realizar la detección de objetos
    results = model(image_rgb)
    
    # Obtener las predicciones de la primera imagen en el lote
    detections = []
    class_names = model.names
    
    for detection in results[0].boxes.data.cpu().numpy():
        x1, y1, x2, y2, conf, cls = detection
        
        detections.append({
            "class": class_names[int(cls)],
            "confidence": float(conf),
            "coordinates": {
                "top_left": [int(x1), int(y1)],
                "bottom_right": [int(x2), int(y2)]
            }
        })
    
    # Devolver las predicciones en formato JSON
    return JSONResponse(content={"detections": detections})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
FROM python:3.12-slim

WORKDIR /app

# Install deps first so this layer is cached on rebuilds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy trained model artifacts
COPY best_model.keras .
COPY src/xgb_model.pkl src/
COPY src/label_encoder.pkl src/
COPY src/predict.py src/

# predict.py runs from src/ so ../best_model.keras resolves correctly
WORKDIR /app/src

ENTRYPOINT ["python", "predict.py"]

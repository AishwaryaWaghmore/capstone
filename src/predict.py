"""
Dog Health Prediction — Team 193, PES University
Usage:
    python predict.py --image path/to/dog.jpg --symptoms "dog is scratching, red patches on belly"
"""

import argparse
import numpy as np
import joblib
import tensorflow as tf
from sentence_transformers import SentenceTransformer
from PIL import Image

# ── Paths (relative to src/) ──────────────────────────────────────────────────
IMAGE_MODEL_PATH = '../best_model.keras'
XGB_MODEL_PATH   = './xgb_model.pkl'
LE_PATH          = './label_encoder.pkl'

# ── Fusion weight (from grid search) — adjust if your results differ ──────────
IMAGE_WEIGHT = 0.7
TEXT_WEIGHT  = 0.3

RISK_MAP = {
    'Healthy':          ('Low',    'No action needed. Continue regular vet check-ups.'),
    'Dermatitis':       ('Medium', 'Consult a vet. Avoid known allergens and use prescribed cream.'),
    'Fungal_infections':('Medium', 'Antifungal treatment required. Keep skin clean and dry.'),
    'Hypersensitivity': ('High',   'See a vet promptly. Identify and remove the allergen.'),
    'demodicosis':      ('High',   'Vet visit required. Prescription antiparasitic treatment needed.'),
    'ringworm':         ('Medium', 'Antifungal medication needed. Isolate the dog — ringworm is contagious.'),
}


def load_models():
    print('Loading models ...')
    image_model = tf.keras.models.load_model(IMAGE_MODEL_PATH)
    xgb_model   = joblib.load(XGB_MODEL_PATH)
    le          = joblib.load(LE_PATH)
    sbert       = SentenceTransformer('all-MiniLM-L6-v2')
    print('Models loaded.\n')
    return image_model, xgb_model, le, sbert


def predict_image(image_model, image_path):
    img = Image.open(image_path).convert('RGB').resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)
    probs = image_model.predict(arr, verbose=0)[0]
    return probs


def predict_text(xgb_model, sbert, symptom_text):
    embedding = sbert.encode([symptom_text.lower()])
    probs = xgb_model.predict_proba(embedding)[0]
    return probs


def fuse_and_predict(img_probs, txt_probs, le, img_w=IMAGE_WEIGHT, txt_w=TEXT_WEIGHT):
    fused   = img_w * img_probs + txt_w * txt_probs
    idx     = int(np.argmax(fused))
    disease = le.inverse_transform([idx])[0]
    confidence = float(fused[idx]) * 100
    return disease, confidence, fused


def print_result(disease, confidence, fused_probs, le, img_probs, txt_probs):
    risk, advice = RISK_MAP.get(disease, ('Unknown', 'Consult a vet.'))

    print('=' * 52)
    print(f'  Predicted Disease : {disease}')
    print(f'  Confidence        : {confidence:.1f}%')
    print(f'  Risk Level        : {risk}')
    print(f'  Recommendation    : {advice}')
    print('=' * 52)

    print('\nPer-class probabilities (fused):')
    for cls, p in sorted(zip(le.classes_, fused_probs), key=lambda x: -x[1]):
        bar = '█' * int(p * 30)
        print(f'  {cls:<22} {p*100:5.1f}%  {bar}')

    print(f'\nImage-only top guess : {le.classes_[np.argmax(img_probs)]} ({max(img_probs)*100:.1f}%)')
    print(f'Text-only top guess  : {le.classes_[np.argmax(txt_probs)]} ({max(txt_probs)*100:.1f}%)')


def main():
    parser = argparse.ArgumentParser(description='Dog Health Predictor — Team 193')
    parser.add_argument('--image',    required=True, help='Path to dog skin image (JPG/PNG)')
    parser.add_argument('--symptoms', required=True, help='Symptom description in plain English')
    parser.add_argument('--img_w',    type=float, default=IMAGE_WEIGHT,
                        help=f'Image model weight (default {IMAGE_WEIGHT})')
    args = parser.parse_args()

    image_model, xgb_model, le, sbert = load_models()

    img_probs = predict_image(image_model, args.image)
    txt_probs = predict_text(xgb_model, sbert, args.symptoms)
    txt_w     = 1.0 - args.img_w

    disease, confidence, fused = fuse_and_predict(img_probs, txt_probs, le, args.img_w, txt_w)
    print_result(disease, confidence, fused, le, img_probs, txt_probs)


if __name__ == '__main__':
    main()

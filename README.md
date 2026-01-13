# Emotion Detection System

## Why This Exists
Emotion detection is often presented without proper evaluation or deployment
considerations. This project focuses on building a clear, testable emotion
classification pipeline suitable for real-world integration.

## Architecture
Input Data  
→ Preprocessing  
→ Feature Extraction  
→ Classification Model  
→ Emotion Output

The pipeline is modular to allow experimentation with different models
and modalities.

## Key Design Decisions
- Modular pipeline for easy experimentation
- Emphasis on data preprocessing
- Simple baseline models before complexity
- Clear separation of training and inference

## Features
- Emotion classification
- Preprocessing pipeline
- Model evaluation
- Predictive inference

## Getting Started
```bash
pip install -r requirements.txt
python main.py

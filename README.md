# multimodal-rec-sys
Multimodal Recommendation System

# Multi-modal Content Recommendation System

An experimental recommendation system that explores how to combine image, text, and video understanding for personalized content suggestions.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.10+-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

This project is my first exploration into building a multi-modal recommendation system. It focuses on:

- 📷 Processing and understanding content across multiple modalities (images, text, videos)
- 🧠 Creating a shared embedding space for cross-modal similarity
- 🧭 Generating content suggestions based on user queries or sample inputs
- 🔍 Experimenting with retrieval, fusion, and hybrid recommendation techniques

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/LadaVilada/multimodal-rec-sys.git
cd multimodal-rec-sys

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt
```

---

## 🧪 Getting Started

Once installed, run the system locally using sample data:

### 🔄 1. Preprocess Sample Data

```bash
python -m scripts.preprocess --dataset sample
```

### 🧠 2. Train a Model

```bash
python -m scripts.train --config configs/sample.yaml
```

### 🌐 3. Start the API (FastAPI backend)

```bash
python -m api.main
# or using uvicorn
uvicorn api.main:app --reload
```
## 📘 API Documentation (Swagger)

Once the FastAPI server is running, you can explore and test the available endpoints using the auto-generated Swagger UI:

📍 [http://localhost:8000/docs](http://localhost:8000/docs)  
📍 [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces provide a visual way to interact with the API, send requests, and view responses in real time.

You can also use tools like Postman or curl to interact with the API endpoints directly.
Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

### 💻 4. Start the Frontend (React)

```bash
cd frontend
npm install
npm start
```

Visit: [http://localhost:3000](http://localhost:3000)

---

## 🧠 Project Structure

```
MultiModal-RecSys/
├── data/              # Preprocessing scripts and sample data
├── models/            # Encoders, fusion logic, and recommendation engines
├── api/               # FastAPI backend
├── scripts/           # Training and evaluation scripts
├── frontend/          # React interface
├── notebooks/         # Experiments and visualizations
├── tests/             # Unit and integration tests
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).


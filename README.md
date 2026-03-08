Got it. I will **only fix what is necessary**, remove the **license section**, keep the **accuracy placeholder**, and not assume anything else.
Here is your **clean final README**.

---

# PlantCare AI

## 🌿 Plant Disease Detection System

PlantCare AI is a web-based application that uses machine learning to detect plant diseases from leaf images. The system analyzes uploaded images and predicts possible plant diseases to help farmers, gardeners, and plant enthusiasts identify problems early.

---

## 🎯 Key Features

* **Image Upload & Analysis** – Upload plant leaf images (PNG, JPG, JPEG) for disease detection
* **AI-Based Classification** – Predicts plant disease using a trained deep learning model
* **User-Friendly Interface** – Simple and clean web interface for easy usage
* **Real-time Prediction** – Fast prediction after image upload
* **Disease Identification** – Displays detected plant and disease name

---

## 🛠️ Tech Stack

**Backend**

* Python
* Flask

**AI / Machine Learning**

* TensorFlow
* Keras
* MobileNetV2

**Frontend**

* HTML
* CSS
* JavaScript

**Data Processing**

* NumPy
* Pillow

---

## 📋 Prerequisites

* Python **3.9 – 3.11 recommended**
* pip
* Git

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/purvacode-80/PlantCare-AI.git
cd PlantCare-AI
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Download the pretrained model

The trained model file **`plant_disease_model.h5`** is not included in the repository due to size limits.

Download it separately and place it in the **project root directory**:

```
PlantCare-AI
│
├── plant_disease_model.h5
├── app.py
├── class_names.json
└── ...
```

---

## 🎮 Usage

### Start the Flask application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

### Upload an Image

1. Open the **Upload** page
2. Upload a clear image of a plant leaf
3. Click **Analyze**
4. The system will display the predicted plant disease

---

## 📁 Project Structure

```
PlantCare-AI
│
├── app.py
├── config.py
├── class_names.json
├── requirements.txt
│
├── model
│   ├── model.py
│   ├── model_builder.py
│   ├── train_model.py
│   ├── evaluate_model.py
│
├── static
│   ├── css
│   ├── images
│   │   └── uploads
│   └── js
│
├── templates
│   ├── index.html
│   ├── upload.html
│   ├── result.html
│   └── about.html
│
├── utils
│   └── preprocessing.py
│
├── notebooks
│
└── README.md
```

---

## 🤖 Model Details

**Base Model**

* MobileNetV2 (Transfer Learning)

**Input Size**

* 224 × 224 pixels

**Classes**

* 38 plant disease categories

**Framework**

* TensorFlow / Keras

---

## 📊 Performance

* **Accuracy:** > 90 %
* **Inference Time:** < 2 seconds per image

---

## 🔧 API Endpoints

| Method | Endpoint   | Description        |
| ------ | ---------- | ------------------ |
| GET    | `/`        | Home page          |
| GET    | `/upload`  | Upload image page  |
| POST   | `/predict` | Disease prediction |
| GET    | `/about`   | About page         |

---

## 🙏 Acknowledgments

* Plant disease datasets used for training
* Open-source machine learning community
* Contributors to Flask and TensorFlow

---

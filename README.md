# 🩺 AI-Based Automated Cobb's Angle Measurement System

An AI-inspired Computer Vision project that automates **Cobb's Angle measurement** from spinal X-ray images using **Python** and **OpenCV**.

> **Note:** This project is currently a prototype that demonstrates the automated Cobb's Angle calculation workflow. The current implementation uses predefined landmark points for demonstration purposes and serves as a foundation for future AI-based landmark detection.

---

## 📌 Overview

Cobb's Angle is one of the most widely used measurements for evaluating spinal curvature from X-ray images.

Traditionally, this angle is measured manually by clinicians, which can be time-consuming and subject to inter-observer variability.

This project demonstrates an automated workflow where the system:

* Loads a spinal X-ray
* Identifies vertebral landmark points
* Draws vertebral reference lines
* Calculates the Cobb's Angle
* Displays the result automatically

---

## 🚀 Features

* Automated Cobb's Angle calculation
* OpenCV-based image processing
* Automatic landmark visualization
* Real-time angle computation
* Clean graphical output
* Beginner-friendly implementation
* Modular Python code

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV
* NumPy
* Math
* Time

---

## 📂 Project Structure

```
AI-Cobb-Angle-Measurement/
│
├── spine.jpg              # Sample X-ray image
├── main.py                # Main application
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Cobb-Angle-Measurement.git
```

Navigate into the project

```bash
cd AI-Cobb-Angle-Measurement
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 📊 Workflow

```
Input X-ray
      │
      ▼
Load Image
      │
      ▼
Landmark Detection
      │
      ▼
Reference Line Generation
      │
      ▼
Cobb's Angle Calculation
      │
      ▼
Display Results
```

---

## 📸 Output

The system automatically displays:

* Detected vertebral landmarks
* Vertebral reference lines
* Calculated Cobb's Angle
* Annotated X-ray image

---

## 🔬 Future Improvements

* AI-based vertebral landmark detection
* Deep Learning integration (YOLO/Keypoint Detection)
* Support for multiple spinal curves
* Clinical-grade measurement pipeline
* Flask/Web Application
* Report generation (PDF)
* DICOM image support
* Model evaluation on real medical datasets

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Computer Vision
* Medical Image Processing
* OpenCV
* Geometric Angle Calculations
* Python Application Development
* Healthcare AI Concepts

---

## ⚠️ Disclaimer

This repository is intended for educational and research purposes only.

It is **not a clinically validated medical device** and should not be used for medical diagnosis or clinical decision-making.

---

## 👨‍💻 Author

**Ayush Yadav**

AI/ML Engineer Intern

Computer Science (Data Science) Student

Interested in:

* Artificial Intelligence
* Machine Learning
* Computer Vision
* Healthcare AI
* Deep Learning

---

## ⭐ Support

If you found this project interesting, consider giving the repository a **⭐ Star** and sharing your feedback. Contributions, suggestions, and improvements are always welcome.

#  Fruit & Vegetable Classifier

A deep learning-powered web application that classifies fruits and vegetables from images using TensorFlow and Streamlit.

---

## 📸Demo

Upload any fruit or vegetable image and the model will instantly predict what it is!

---

## 🚀 Features

- 🔍 Real-time image classification

- 🧠 Powered by a trained TensorFlow/Keras CNN model

- 🎨 Beautiful dark-themed UI with gradient styling

- 📤 Simple drag-and-drop image upload

- ⚡ Fast predictions using NumPy preprocessing

---

## 🛠️ Tech Stack

| Technology | Purpose |

|---|---|

| Python | Core programming language |

| TensorFlow / Keras | Deep learning model |

| Streamlit | Web application framework |

| NumPy | Image array processing |

| Pillow (PIL) | Image loading and handling |

---

## 📁 Project Structure

Image_clasi/

│

├── app.py                             # Main Streamlit application

├── image_classification_model.ipynb  # Model training notebook

├── Image_classify.keras               # Trained Keras model file

├── requirements.txt                   # Python dependencies

└── README.md                          # Project documentation

---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/thakshana22/Image_clasi.git

cd Image_clasi

### 2. Create a virtual environment

python -m venv venv

venv\Scripts\activate       # Windows

source venv/bin/activate    # Mac/Linux

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the app

streamlit run app.py

# Or if streamlit is not in PATH:

python -m streamlit run app.py

---

## 📦 Requirements

tensorflow

streamlit

numpy

Pillow

# Install all at once:

pip install tensorflow streamlit numpy Pillow

---

## 🧠 Model Details

- **Framework:** TensorFlow / Keras

- **Input:** RGB image resized to model's expected input shape

- **Output:** Predicted class label with confidence score

- **Model file:** `Image_classify.keras`

---

## 📌 How to Use

1. Run the app using the command above

2. Open your browser at `http://localhost:8501`

3. Upload a fruit or vegetable image (JPG, PNG, etc.)

4. View the predicted class instantly on screen

---

## 🐛 Common Issues

| Problem | Solution |

|---|---|

| `streamlit not recognized` | Run `python -m streamlit run app.py` |

| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |

| Model not found error | Make sure `Image_classify.keras` is in the same folder as `app.py` |

| LF/CRLF Git warning | Run `git config core.autocrlf false` |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Made with ❤️ — feel free to connect on [GitHub](https://github.com/your-username)

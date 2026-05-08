
import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Fruit & Vegetable Classifier",
    page_icon="🍎",
    layout="centered"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    }

    h1 {
        text-align: center;
        background: linear-gradient(90deg, #f7971e, #ffd200);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 46px;
        font-weight: 900;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #11998e, #38ef7d);
        color: white;
        margin-top: 25px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 20px rgba(56, 239, 125, 0.4);
    }

    .stButton>button {
        background: linear-gradient(90deg, #f7971e, #ffd200);
        color: #1a1a2e;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 12px 30px;
        font-size: 18px;
        width: 100%;
        cursor: pointer;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 4px 15px rgba(247, 151, 30, 0.5);
    }

    .stFileUploader label {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------
st.markdown("<h1>🍎 Fruit & Veggie AI 🥦</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload any fruit or vegetable image — AI will identify it instantly!</p>', unsafe_allow_html=True)

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_my_model():
    return load_model(r"D:\ML_project\Image_clasi\Image_classify.keras")

model = load_my_model()

# ----------------------------
# Categories
# ----------------------------
data_cat = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage',
    'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn',
    'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes',
    'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango',
    'onion', 'orange', 'paprika', 'pear', 'peas',
    'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans',
    'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip',
    'watermelon'
]

img_height = 180
img_width = 180

# ----------------------------
# Upload Section
# ----------------------------
st.markdown("---")
uploaded_file = st.file_uploader(
    "",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption="Your uploaded image", use_container_width=True)

    # Preprocess
    img_resized = image.resize((img_width, img_height))
    img_arr = tf.keras.utils.img_to_array(img_resized)
    img_bat = tf.expand_dims(img_arr, 0)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔍 Identify This!"):
        with st.spinner("🤖 AI is thinking..."):
            predict = model.predict(img_bat)
            score = tf.nn.softmax(predict[0])

            predicted_class = data_cat[np.argmax(score)]
            confidence = np.max(score) * 100

        st.markdown(f"""
            <div class="result-box">
                <div style="font-size: 28px; margin-top: 10px;">
                    {predicted_class.title()}
                </div>
                <div style="font-size: 16px; opacity: 0.85; margin-top: 6px;">
                    Confidence: {confidence:.2f}%
                </div>
            </div>
        """, unsafe_allow_html=True)
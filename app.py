import streamlit as st
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
from PIL import Image
import io

st.title("Image Data Augmentation App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).resize((150, 150))
    st.image(img, caption="Original Image", use_container_width=True)

    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    augmented_images = []
    for batch in datagen.flow(x, batch_size=1):
        augmented_images.append(array_to_img(batch[0]))
        if len(augmented_images) == 5:
            break

    st.image(augmented_images, caption=[f"Augmented {i+1}" for i in range(5)], width=150)

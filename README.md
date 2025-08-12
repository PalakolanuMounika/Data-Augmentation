# 🖼️ Data Augmentation App with Streamlit

An interactive web app for performing **image data augmentation** using **TensorFlow Keras** and **Streamlit**.  
Upload an image, choose augmentation techniques, and instantly preview the results.

---

## 📌 Features
- Upload images in **JPG** or **PNG** format
- Apply common data augmentation techniques:
  - Rotation
  - Width/Height Shift
  - Shear
  - Zoom
  - Horizontal Flip
  - Brightness & Channel Shift
- Preview multiple augmented images at once
- Download augmented images
- Built with **Streamlit** for an easy-to-use interface

---

## 🛠️ Technologies Used
- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [TensorFlow Keras](https://www.tensorflow.org/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

---

## 📂 Project Structure
```
📦 data-augmentation-app
 ┣ 📜 app.py                # Streamlit application
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 README.md             # Project documentation
 ┗ 📂 sample_images         # Example images
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/data-augmentation-app.git
cd data-augmentation-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

### 4️⃣ Open in Browser
Go to **http://localhost:8501** in your browser to use the app.

---

## 📸 Demo
![Data Augmentation Example](sample_images/demo.png)

---

## 📝 Example Output
Original Image | Augmented Image  
:------------: | :-------------:  
<img src="sample_images/original.jpg" width="250"/> | <img src="sample_images/augmented.jpg" width="250"/>  

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Pull requests are welcome!  
If you have ideas for new augmentation techniques, feel free to open an issue or submit a PR.

---

## ⭐ Acknowledgments
- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Albumentations](https://albumentations.ai/) for inspiration

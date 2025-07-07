#  Interactive Watershed Segmentation with Marker Lines

This project implements **interactive image segmentation** using the **Watershed algorithm** guided by hand-drawn seed lines. With this approach, you can mark the regions on an image using white lines, and the algorithm will segment the image into distinct color-coded regions based on your input.

Built using **Streamlit**, **OpenCV**, and **Drawable Canvas**, the app offers a simple and visual experience for classic watershed segmentation.

---

##  How It Works

1. Upload any image (JPG/PNG).
2. Use your mouse to draw **white marker lines** on different regions.
3. Each marker acts as a seed point for watershed expansion.
4. The watershed algorithm assigns each segment a **unique random color**.
5. Boundaries between regions are highlighted in **red**.

---

##  Features

- ✅ Fully interactive UI with Streamlit
- ✅ Draw freehand seed lines directly on the image
- ✅ Watershed segmentation with distinct random-colored regions
- ✅ Combined before/after image saved in `outputs/`
- ✅ Downloadable result

---


## 🚀 How to Run

```bash
# Clone the repo or this subfolder's parent project
git clone https://github.com/snz-mlcoder/image-segmentation-projects.git
cd image-segmentation-projects/watershed_app


# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py

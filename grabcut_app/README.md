# 🖼️ Interactive Image Segmentation with GrabCut (Streamlit App)

This project demonstrates how to perform object segmentation using the **GrabCut** algorithm through an interactive web app built with **Streamlit**. Users can upload an image, draw a bounding box around the object of interest, and segment it from the background with just one click.

---

## 📌 Features

- Upload any image (`.png`, `.jpg`, `.jpeg`)
- Draw a bounding box interactively using the mouse
- Apply the GrabCut segmentation algorithm (based on Graph Cuts)
- View both the segmented output and the binary mask
- Download the result as an image
- Saves outputs automatically in the `outputs/` folder

---

## About GrabCut

GrabCut is an image segmentation technique that models the foreground and background color distributions using **Gaussian Mixture Models (GMM)**, and applies **Graph Cuts** to minimize energy and segment the object.




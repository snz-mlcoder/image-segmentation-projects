import streamlit as st
import numpy as np
import cv2
from PIL import Image
import os
import uuid
from streamlit_drawable_canvas import st_canvas
from watershed import apply_label_watershed

# Streamlit app configuration
st.set_page_config(page_title="Watershed Segmentation", layout="centered")
st.title("🌈 Marker-Based Watershed Segmentation")

st.write("""
Draw freehand **white marker lines** on the image to define seed regions.  
The watershed algorithm will expand these seeds and assign each region a unique color.
""")

# Upload section
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    # Convert uploaded image to NumPy array
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)

    st.image(image, caption="Original Image", use_column_width=True)

    st.subheader("🖌️ Draw white marker lines as seed regions")

    # Interactive canvas for drawing
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 1)",  # White marker
        stroke_width=5,
        stroke_color="white",
        background_image=image,
        update_streamlit=True,
        height=img_np.shape[0],
        width=img_np.shape[1],
        drawing_mode="freedraw",
        key="canvas",
    )

    # If the user has drawn something
    if canvas_result.image_data is not None:
        drawn_mask = np.array(canvas_result.image_data).astype(np.uint8)
        st.image(drawn_mask, caption="🖍️ Your Marker Mask", use_column_width=False)

        if st.button("🌀 Run Watershed"):
            with st.spinner("Processing..."):
                # Run the watershed algorithm
                result = apply_label_watershed(img_np, drawn_mask)

                # Show the segmented result
                st.image(result, caption="🎨 Segmented Output", use_column_width=True)

                # Combine original and result side by side
                comparison = np.hstack((img_np, result))

                # Save to outputs/ folder
                os.makedirs("outputs", exist_ok=True)
                filename = f"outputs/comparison_{uuid.uuid4().hex[:6]}.png"
                cv2.imwrite(filename, cv2.cvtColor(comparison, cv2.COLOR_RGB2BGR))

                # Display and download combined image
                st.image(comparison, caption="📸 Original (left) vs Segmented (right)", use_column_width=True)

                with open(filename, "rb") as f:
                    st.download_button("📥 Download Comparison Image", data=f, file_name="comparison_result.png")

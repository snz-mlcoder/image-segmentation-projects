import streamlit as st
import cv2
import numpy as np
from grabcut import apply_grabcut
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import os
import uuid

st.set_page_config(page_title="GrabCut Segmentation", layout="centered")
st.title("🖼️ GrabCut Image Segmentation App")

st.write("Upload an image and draw a rectangle to segment the object.")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)
    st.image(image, caption="Original Image", use_column_width=True)

    # Canvas for drawing
    st.subheader("🖌️ Draw rectangle around the object")
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",
        stroke_width=2,
        stroke_color="green",
        background_image=image,
        update_streamlit=True,
        height=img_np.shape[0],
        width=img_np.shape[1],
        drawing_mode="rect",
        key="canvas",
    )

    # If a rectangle is drawn
    if canvas_result and canvas_result.json_data["objects"]:
        obj = canvas_result.json_data["objects"][-1]
        left = int(obj["left"])
        top = int(obj["top"])
        width = int(obj["width"])
        height = int(obj["height"])
        rect = (left, top, width, height)

        st.success(f"Rectangle: x={left}, y={top}, w={width}, h={height}")

        if st.button("✂️ Run GrabCut"):
            with st.spinner("Processing..."):
                output, mask = apply_grabcut(img_np, rect)

            st.image(output, caption="Segmented Output", use_column_width=True)
            st.image(mask * 255, caption="Binary Mask", use_column_width=True, clamp=True)

            # Save to file
            os.makedirs("outputs", exist_ok=True)
            filename = f"outputs/output_{uuid.uuid4().hex[:8]}.png"
            cv2.imwrite(filename, cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
            st.success(f"Image saved to: {filename}")

            # Download button
            result_image = Image.fromarray(output)
            st.download_button("📥 Download Result", data=result_image.tobytes(), file_name="output.png")

    else:
        st.warning("Please draw a rectangle on the image before running GrabCut.")

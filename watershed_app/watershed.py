import cv2
import numpy as np
import random

def apply_label_watershed(img, marker_mask):
    """
    Applies watershed segmentation using hand-drawn marker lines.
    
    Parameters:
        img (ndarray): Original RGB image.
        marker_mask (ndarray): Marker image (with white seed lines).
        
    Returns:
        output (ndarray): RGB image with regions colored distinctly.
    """

    # Convert RGBA to RGB if needed
    if marker_mask.shape[2] == 4:
        marker_mask = cv2.cvtColor(marker_mask, cv2.COLOR_RGBA2RGB)

    # Convert marker image to grayscale
    gray = cv2.cvtColor(marker_mask, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    # Label connected components (seed regions)
    num_labels, markers = cv2.connectedComponents(binary)
    markers = markers.astype(np.int32)

    # Apply watershed algorithm
    markers = cv2.watershed(img.copy(), markers)

    # Generate color output image
    output = np.zeros_like(img)
    colors = {}

    for label in np.unique(markers):
        if label == -1:
            color = [255, 0, 0]  # Red for boundaries
        elif label == 0:
            color = [0, 0, 0]    # Black for unknown
        else:
            # Random color for each segment
            color = [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)]
        colors[label] = color
        output[markers == label] = color

    return output

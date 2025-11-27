import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

def detect_crop_type(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(image, image, mask=mask)
    ratio = np.count_nonzero(mask) / (image.shape[0] * image.shape[1])
    if ratio > 0.1:
        return "Given Image Is Detected as Crop"
    else:
        return "Given Image Is Detected as Not a Crop"

def detect_crop():
    image_path = filedialog.askopenfilename()
    image = cv2.imread(image_path)
    crop_type = detect_crop_type(image)
    result_label.config(text=f"Detected crop type: {crop_type}")

root = tk.Tk()
select_button = tk.Button(root, text="Select image", command=detect_crop)
select_button.pack()

# Create a label to display the results
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()

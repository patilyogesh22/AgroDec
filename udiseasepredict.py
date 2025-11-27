import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

# Load the pre-trained machine learning model
model = ResNet50(weights='imagenet')

def predict_disease():
    # Open the file dialog to select the crop image
    file_path = filedialog.askopenfilename()

    # Load the selected image
    img = Image.open(file_path)
    img = img.resize((224, 224))
    img_array = np.array(img)

    # Preprocess the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Make the prediction
    preds = model.predict(x)
    decoded_preds = decode_predictions(preds, top=3)[0]

    # Display the prediction
    for i, prediction in enumerate(decoded_preds):
        print(f"{i+1}. {prediction[1]}: {prediction[2]*100:.2f}%")

# Create the Tkinter window
window = tk.Tk()
window.title("Crop Disease Prediction")

# Create the button to select the crop image
select_button = tk.Button(window, text="Select Crop Image", command=predict_disease)
select_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

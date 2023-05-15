import serial
import time

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    arduino.flush()
    time.sleep(0.1)
    data = arduino.readline()
    return data

from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

labels_file = "smile_open_mouth_labels.txt"
model_file = "smile_open_mouth_model.h5"

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(model_file, compile=False)

# Load the labels
class_names = open(labels_file, "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def check_all(results, state):
    result = True
    for s in results:
        if s != state:
            return False
    return result

results = []
while True:
    if len(results) == 10:
        if check_all(results, 1) == True:
            for i in range(100):
                arduino.write(bytes(str(1), 'utf-8'))
            arduino.flush()
            results = []
        elif check_all(results, 0) == True:
            for i in range(100):
                arduino.write(bytes(str(0), 'utf-8'))
            arduino.flush()
            results = []
        else:
            results = []

    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    if "smile" in class_name:
        results.append(0)
    else:
        results.append(1)

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("pneumonia.h5")

def pneumoniapredictPage(img):

    img = Image.open(img)
    img = img.resize((36, 36))
    img = np.asarray(img)
    img = img.reshape((1, 36, 36, 1))
    img = img / 255.0

    pred = np.argmax(model.predict(img)[0])

    return pred

# print(pneumoniapredictPage("test1.jpeg"))
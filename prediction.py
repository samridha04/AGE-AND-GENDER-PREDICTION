import cv2
import numpy as np
from keras.models import load_model


def getAge(distr):
    distr = distr*4
    if distr >= 0.65 and distr <= 1.4:
        return "0-18"
    if distr >= 1.65 and distr <= 2.4:
        return "19-30"
    if distr >= 2.65 and distr <= 3.4:
        return "31-80"
    if distr >= 3.65 and distr <= 4.4:
        return "80 +"
    return "Unknown"


def getGender(prob):
    if prob < 0.5:
        return "Male"
    else:
        return "Female"


def getAgeGender(image_path):
    # Loading the uploaded Image:
    image = cv2.imread(image_path,0)
    image = cv2.resize(image,dsize=(64,64))
    image = image.reshape((image.shape[0],image.shape[1],1))

    # Loading the trained model:
    model = load_model('data.h5')
    # model.summary()

    # Getting the predictions:
    image = image/255
    val = model.predict(np.array([image]))
    age = getAge(val[0])
    gender = getGender(val[1])
    return age, gender


import streamlit as st
import model
from PIL import Image


st.title("Pneumonia Detection")

t1, t2  = st.tabs(["Home", "Pneumonia"])

with t1:


    st.header("Pneumonia")

    # Pneumonia
    st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses, and fungi, can cause pneumonia.")

    st.header("Symptoms")

    st.write("- Cough, which may produce greenish, yellow or even bloody mucus.")
    st.write("- Fever, sweating, and shaking chills.")
    st.write("- Shortness of breath.")
    st.write("- Rapid, shallow breathing.")


with t2:

    # image uploader

    uploader = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploader:

        image = Image.open(uploader)

        prediction = model.pneumoniapredictPage(uploader)

        if prediction == 1:
            st.error("You have Pneumonia! Consult a doctor")
        else:
            st.success("Congtazzz! You dont have pneumonia")
        

        # display image
        st.image(image, caption='Sunrise by the mountains', width = 500)
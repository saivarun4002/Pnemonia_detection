import streamlit as st
import model
from PIL import Image

st.title("Pneumonia Detection")


t1, t2, t3 = st.tabs(["Home", "Pneumonia", "Group Members"])

# Home Tab
with t1:
    st.header("Pneumonia")

    st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses, and fungi, can cause pneumonia.")

    st.header("Symptoms")

    st.write("- Cough, which may produce greenish, yellow or even bloody mucus.")
    st.write("- Fever, sweating, and shaking chills.")
    st.write("- Shortness of breath.")
    st.write("- Rapid, shallow breathing.")
    

# Pneumonia Tab
with t2:
    # ... (existing content for the Pneumonia tab)
    uploader = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploader:
        image = Image.open(uploader)
        prediction = model.pneumoniapredictPage(uploader)
        if prediction == 1:
            st.error("You have Pneumonia! Consult a doctor")
        else:
            st.success("Congtazzz! You don't have pneumonia")
        st.image(image, caption='Sunrise by the mountains', width=500)

# Group Members Tab
with t3:
    st.header("Group Members")
    st.write("- Sai Nikhil")
    st.write("- Sai Varun")
    st.write("- Mohit Yadav")
    st.write("- Shiva Tilak")
    st.write("- Yasin Syed")
    st.write("- Khitish Behara")
    

# Library imports
import numpy as np
import streamlit as st
from PIL import Image
from keras.models import load_model
from openai import OpenAI

# Loading the Model
model = load_model('plant_disease_model.h5')

# OpenAI API Key
api_key = "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"
client = OpenAI(api_key=api_key)

# Name of Classes
CLASS_NAMES = ('Tomato-Bacterial_spot', 'Potato-Early_blight', 'Corn-Common_rust')

# Main function
def main():
    # Setting Title of App
    st.title("Plant Disease Detection")
    st.markdown("Upload an image of the plant leaf")

    # Uploading the image
    plant_image = st.file_uploader("Choose an image...", type="jpg")

    # On predict button click
    if st.button('Predict Disease'):
        if plant_image is not None:
            # Convert the file to an Image object.
            image = Image.open(plant_image)
            
            # Displaying the image
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Resizing the image
            image = image.resize((256, 256))
            
            # Convert image to numpy array
            image = np.array(image)
            
            # Normalize image
            image = image / 255.0
            
            # Reshape image
            image = np.expand_dims(image, axis=0)
            
            # Make Prediction
            Y_pred = model.predict(image)
            result = CLASS_NAMES[np.argmax(Y_pred)]
            st.title(f"This is {result.split('-')[0]} leaf with {result.split('-')[1]}")

            # Get recommendations from ChatGPT
            treatment, fertilizer = get_recommendations(result)
            
            # Display treatment recommendation
            st.subheader("Recommended Treatment:")
            st.write(treatment)
            
            # Display fertilizer recommendation if available
            if fertilizer:
                st.subheader("Recommended Fertilizer to Avoid Future Disease:")
                st.write(fertilizer)

def get_recommendations(plant_disease):
    # Prompt for ChatGPT
    prompt = f"I have detected {plant_disease}. Can you recommend a treatment or remedy to cure this plant disease? Also, which fertilizer can be used to avoid the disease in the future?"

    # Generate response from ChatGPT
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an agricultural assistant, skilled in providing recommendations for plant diseases and fertilizers."},
            {"role": "user", "content": prompt}
        ]
    )

    # Initialize treatment and fertilizer recommendations
    treatment = ""
    fertilizer = ""

    # Extracting treatment and fertilizer recommendations from ChatGPT response
    for choice in completion.choices:
        message = choice.message.content  # Accessing 'content' attribute
        if "Fertilizer Recommendation:" in message:
            fertilizer = message.split("Fertilizer Recommendation:")[1].strip()
        else:
            treatment = message.strip()

    return treatment, fertilizer

if __name__ == "__main__":
    main()

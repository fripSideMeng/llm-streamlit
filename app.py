import streamlit as st
from transformers import pipeline
from PIL import Image

def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

# Initialize the Hugging Face pipeline with a text generation model
generator = pipeline('text-generation', model='Austism/chronos-hermes-13b-v2')

st.title('Hugging Face LLM Chatbot')

# Text input for user query
user_input = st.text_input("Talk to the chatbot:")

if user_input:
    # Generate a response using the model
    response = generator(user_input, max_length=50, num_return_sequences=1)
    st.text_area("Chatbot says:", value=response[0]['generated_text'], height=200)

image_path = 'background.png'
image = Image.open(image_path)
st.image(image, caption='Welcome to My Chatbot Website', use_column_width=True)

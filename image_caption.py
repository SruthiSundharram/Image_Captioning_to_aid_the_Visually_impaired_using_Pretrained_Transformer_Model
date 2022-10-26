import streamlit as st
from gtts import gTTS

import warnings,logging
from transformers import pipeline
from IPython.display import Image
from PIL import Image
warnings.simplefilter('ignore')
logging.disable(logging.WARNING)

# Method to generate captions for the images using Transformer pipeline 'image-to-text'
def image_to_speech(buff):
    #read the image from the buffer and save it to a file with jpg extension
    with open ('test.jpg','wb') as file:
          file.write(buff.getbuffer())
    file_path='test.jpg'
    #pass the image to the pretrained model for text caption generation
    caption = pipeline('image-to-text')
    caption_=caption(file_path)
    
    #Text to speech conversion using Google Text to speech module
    inp_text = caption_[0]['generated_text']
    st.write(inp_text)
    my_aud = gTTS(inp_text) #converts the text into speech
    my_aud.save('demo.mp3') 

    #Display the audio caption generated using streamlit
    audio_file = open('demo.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

st.title("Image Captioning")
img_file_buffer = st.camera_input("Take a picture") #Click a picture using webcam
uploaded_file = st.file_uploader("Choose an image...", type="jpg")  #upload an image

if img_file_buffer is not None:       #if a picture is captured through the camera
    bytes_data = img_file_buffer.getvalue()
    image_to_speech(img_file_buffer)

if uploaded_file is not None:       #if a picture is uploaded
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    image_to_speech(uploaded_file)
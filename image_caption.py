import streamlit as st
from gtts import gTTS
from transformers import pipeline
from IPython.display import Image
from PIL import Image

# Stores loaded model in cache so that we don't need to reload model repeatedly for each input
@st.cache(allow_output_mutation=True) 
def load_model():
	"""Retrieves the trained model"""
	model = pipeline('image-to-text')
	return model

# Method to generate captions for the images using Transformer pipeline 'image-to-text'
def image_to_speech(buff, caption):
	"""Takes image buffer as input received from user and generates image description using ML models
	   input : Image, img-to-text model
	   output : Outputs an audio file
	"""

    #read the image from the buffer and save it to a file with jpg extension
    with open ('test.jpg','wb') as file:
          file.write(buff.getbuffer())
    file_path='test.jpg'
    #pass the image to the pretrained model for text caption generation
    caption_=caption(file_path)
    
    #Text to speech conversion using Google Text to speech module
    inp_text = caption_[0]['generated_text']
    st.write(inp_text)
    #converts the text into speech
    my_aud = gTTS(inp_text) 
    my_aud.save('demo.mp3') 

    #Display the audio caption generated using streamlit
    audio_file = open('demo.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

def main():
	model = load_model()
	st.title("Welcome to Image to Speech app")
	instructions = """Click an image using inbuilt camera or upload an image file"""
	st.write(instructions)

	# Click a picture using webcam
	img_file_buffer = st.camera_input("Take a picture") 
	# Upload an image from user
	uploaded_file = st.file_uploader("Choose an image...", type="jpg")  

	# If a picture is captured through the camera
	if img_file_buffer is not None:       
	    bytes_data = img_file_buffer.getvalue()
	    image_to_speech(img_file_buffer, model)
	# If a picture is uploaded
	elif uploaded_file is not None:       
	    image = Image.open(uploaded_file)
	    st.image(image, caption='Uploaded Image.', use_column_width=True)
	    image_to_speech(uploaded_file, model)

if __name__ == '__main__' : 
	main()
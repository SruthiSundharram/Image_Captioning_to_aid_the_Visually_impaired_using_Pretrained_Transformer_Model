import gradio as gr
from transformers import pipeline
from gtts import gTTS 
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
import os

# load the model
model = pipeline('image-to-text')

# defining the image to speech function
def img2Speech(image):
  description = model(image)
  generated_text = description[0]['generated_text']
  generated_audio = gTTS(generated_text)
  generated_audio.save("demo.mp3")
  return 'demo.mp3'

# design the interface using gradio
demo = gr.Interface(
    # call img to speech conversion function
    fn = img2Speech,
    # specify the input format
    inputs = gr.Image(source="webcam", type='pil'),
    # specify the output format
    outputs=gr.Audio()

)

# launch the application
demo.launch(debug=True)
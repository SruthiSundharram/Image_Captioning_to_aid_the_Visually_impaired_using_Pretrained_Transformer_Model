import gradio as gr
from transformers import pipeline
from gtts import gTTS 
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
import os

model = pipeline('image-to-text')

def img2Speech(image):
  #image = Image(image)
  description = model(image)
  generated_text = description[0]['generated_text']
  generated_audio = gTTS(generated_text)
  generated_audio.save("demo.mp3")

  #song = AudioSegment.from_mp3("demo.mp3")
  #play(song)
  #os.system("demo.mp3")
  #return play(song)
  return 'demo.mp3'

demo = gr.Interface(
    fn = img2Speech,
    inputs = gr.Image(), #source="webcam", type='pil'), #source="webcam", source='upload', type='pil'
    outputs=gr.Audio() # gr.Audio(),

)

demo.launch(debug=True)

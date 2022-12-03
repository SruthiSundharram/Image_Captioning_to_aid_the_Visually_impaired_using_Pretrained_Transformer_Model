import gradio as gr
from transformers import pipeline
from gtts import gTTS 
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
import os

model = pipeline('image-to-text')

def img2Speech(image):
  description = model(image)
  generated_text = description[0]['generated_text']
  generated_audio = gTTS(generated_text)
  generated_audio.save("demo.mp3")
  song = AudioSegment.from_mp3("demo.mp3")
  play(song)
  return play(song)

demo = gr.Interface(
    fn = img2Speech,
    source=gr.Image()
    outputs=gr.Audio(),

)

demo.launch(debug=True)
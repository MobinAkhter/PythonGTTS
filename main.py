import os
from gtts import gTTS

filename = 'text.txt'
file = open(filename, 'r')
text = ''

for line in file:
    text += line

file.close()

tts = gTTS(text)
tts.save('speech.mp3')
os.system('speech.mp3')

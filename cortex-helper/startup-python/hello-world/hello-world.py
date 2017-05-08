#!/usr/bin/env python3
from gtts import gTTS
import subprocess
tts = gTTS(text='Hey Claudine, reminder from daddy, honey did you take some water, more water no boo boos', lang='en')
tts.save("good.mp3")
subprocess.call(["mpg321", "./good.mp3"])
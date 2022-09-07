from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_silence
import speech_recognition as sr
from googletrans import Translator, constants
from gtts import gTTS
import os
import playsound
import random
import pydub


def recog(audio,recog_text,lan):
	r=sr.Recognizer()
	a=sr.AudioFile(audio)
	with a as source:
		r.adjust_for_ambient_noise(source)
		Audio=r.record(a)
	try:
		recognised_text=r.recognize_google(Audio,language=lan)
		trans=Translator()	
		A=trans.translate(recognised_text)
		recog_text.append(A.text)
	except sr.UnknownValueError:
		pass

audio=#'specify audio path'
recog_text=[]
lan=#'Specify language code'

recog(audio,recog_text,lan)
print(recog_text)
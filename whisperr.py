# -*- coding: utf-8 -*-
"""whisper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fyk9TdDpAtOpRpHl2_8OJUZCOKISxANC

**Defining the objective**

The aim of this project is to create a Speech-To-Text application using an ASR (Automatic Speech Recognition) system, Whisper.

Whisper has been trained for 680,000 hours on huge amount of speech data collected from the internet. The diverse dataset allows Whisper to understand different accents, and filter background noise. The Whisper architecture is a simple end-to-end approach, implemented as an encoder-decoder Transformer. Input audio is split into 30-second chunks, converted into a log-Mel spectrogram, and then passed into an encoder. A decoder is trained to predict the corresponding text caption, intermixed with special tokens that direct the single model to perform tasks such as language identification, phrase-level timestamps, multilingual speech transcription, and to-English speech translation.

 You can learn more about Whisper from https://openai.com/blog/whisper/

**Installing Required Libraries**
"""

#Importing the necessary libraries
import torch
import whisper
import pytube
import librosa
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd

"""**Loading the Model**

There are five model sizes to choose from, four have English-only versions, offering speed and accuracy trade-offs. The model sizes are:
- tiny: 39M Parameters, English-only model (tiny.en), Multilingual model (tiny), Required VRAM (1GB), Relative speed (32x)
- base: 74M Parameters, English-only model (base.en), Multilingual model (base), Required VRAM (1GB), Relative speed (16x)
- small: 244M Parameters, English-only model (small.en), Multilingual model (small), Required VRAM (2GB), Relative speed (6x)
- medium: 769M Parameters, English-only model (medium.en), Multilingual model (medium), Required VRAM (5GB), Relative speed (2x)
- tiny: 1550M Parameters, English-only model (N/A), Multilingual model (large), Required VRAM (10GB), Relative speed (1x)
The tiny model can be utilized best for light weight applications, the large model if accuracy is most important, and the base, small or medium models for everything in between. For this project, we would be using the medium model.
"""

model_m = whisper.load_model('medium')

"""**Loading the file**"""

file_path = '/content/Rec.mp3'

#Loading
audio_13 = whisper.load_audio(file_path)
audio_13

"""Задаем время голосовго файла -12 секунд"""

T = 12

#Checking the number of samples in our audio file
n_samples =  audio_13.shape[0]
n_samples

#Time between samples
delta = T/n_samples
delta

#Sampling frequency
Fs = 1/delta
Fs

#Time of each sample
time = np.linspace(0,(n_samples-1) * delta,n_samples)
time

"""Now we plot the amplitude with respect to time:"""

plt.figure(figsize=(20,10))
plt.title('Signal')
plt.plot(time,audio_13)
plt.ylabel('amplitude')
plt.xlabel('seconds')
plt.show()

audio = whisper.pad_or_trim(audio_13)

#Number of samples in our trimmed/padded audio
n_samples =  audio.shape[-1]
#Time of each sample
time = np.linspace(0,(n_samples-1)*delta,n_samples)

plt.figure(figsize=(20,10))
plt.title('Signal')
plt.plot(time,audio)
plt.ylabel('amplitude')
plt.xlabel('seconds')
plt.show()

"""Next, we can start plotting a mel spectogram by applying a log_mel_spectogram() funtion to our audio file. It converts the y-axis (frequency) into the mel scale:"""

mel = whisper.log_mel_spectrogram(audio).to(model_m.device)

fig, (ax1, ax2) = plt.subplots(2)
fig.tight_layout(pad=5.0)
ax1.plot(time,audio)
ax1.set_title('Signal')
ax1.set_xlabel('Time, seconds')
ax1.set_ylabel('Amplitude')
ax2.imshow((mel.numpy()*mel.numpy())**(1/2),interpolation='nearest', aspect='auto')
ax2.set_title('Mel Spectrogram of a Signal')
ax2.set_xlabel('Time, seconds')
ax2.set_ylabel('Mel Scale')

"""Next, we can move on to language detection.

**Language detection**
"""

sr=22050
ipd.Audio(audio, rate=sr)

probs = model_m.detect_language(mel)

probs

"""**Transcription**"""

file_path2= 'Rec.mp3'

transcription = model_m.transcribe(file_path2, fp16 = False)['text']

transcription

pip install nltk jiwer

import nltk

nltk.download('punkt')

def calculate_wer(reference, hypothesis):
    return jiwer.wer(reference, hypothesis)

reference_transcription = "one Go to settings and delete the calculator application two Turn on the telegram application and open a correspondence with Denis three Close all tabs on my computer and turn on system update"
wer = calculate_wer(reference_transcription, transcription)
print(f"WER: {wer}")
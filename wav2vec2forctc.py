# -*- coding: utf-8 -*-
"""Wav2Vec2ForCTC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UZiDC--sLq8ccaa3IsK1Jk96RdpLnzru
"""

# Установка необходимых библиотек
!pip install jiwer nltk

# Импорт библиотек
import transformers
import librosa
import torch
import IPython.display as display
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import numpy as np
import jiwer
import nltk
from nltk.translate.bleu_score import sentence_bleu

nltk.download('punkt')

def calculate_wer(reference, hypothesis):
    return jiwer.wer(reference, hypothesis)

# Загрузка предобученной модели и токенизатора
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

audio, sampling_rate = librosa.load("/content/Rec.mp3", sr=16000)

display.Audio("/content/Rec.mp3", autoplay=True)

# Токенизация входных значений
input_values = tokenizer(audio, return_tensors='pt').input_values

logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcriptions = tokenizer.decode(predicted_ids[0])

transcriptions

reference_transcription = "one Go to settings and delete the calculator application two Turn on the telegram application and open a correspondence with Denis three Close all tabs on my computer and turn on system update"

wer = calculate_wer(reference_transcription, transcriptions)
print(f"WER: {wer}")
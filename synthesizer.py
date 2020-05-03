#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:54:35 2020

@author: tanmay
"""
import librosa

import numpy as np

from pathlib import Path
from encoder import inference as encoder
from vocoder import inference as vocoder
from synthesizer.inference import Synthesizer


# Load Model

encoder_weights = Path("encoder/saved_models/pretrained.pt")
vocoder_weights = Path("vocoder/saved_models/pretrained/pretrained.pt")
syn_dir = Path("synthesizer/saved_models/logs-pretrained/taco_pretrained")
encoder.load_model(encoder_weights)
synthesizer = Synthesizer(syn_dir)
vocoder.load_model(vocoder_weights)


def synth(text, audio_file):
    """

    Parameters
    ----------
    text : string
        text to be said in synthesized voice
    audio_file : filepath
        filepath for audio file in wav format

    Returns
    -------
    generated_wav : numpy.ndarray
        Numpy padded array of synthesized audio signal

    """
    
    in_fpath = Path("audio.wav") 
    original_wav, sampling_rate = librosa.load(in_fpath)
    preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
    embed = encoder.embed_utterance(preprocessed_wav)
    print("Synthesizing new audio...")
    specs = synthesizer.synthesize_spectrograms([text], [embed])
    generated_wav = vocoder.infer_waveform(specs[0])
    generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode = "constant")
    
    return generated_wav
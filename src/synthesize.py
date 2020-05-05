#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import librosa

import numpy as np

from pathlib import Path
from encoder import inference as encoder
from vocoder import inference as vocoder
from synthesizer.inference import Synthesizer


# Load Model

encoder_weights = Path("pre_train/encoder/saved_models/pretrained.pt")
vocoder_weights = Path("pre_train/vocoder/saved_models/pretrained/pretrained.pt")
syn_dir = Path("pre_train/synthesizer/saved_models/logs-pretrained/taco_pretrained")
encoder.load_model(encoder_weights)
synthesizer = Synthesizer(syn_dir)
vocoder.load_model(vocoder_weights)

def choose_speaker_audio(speaker_name):
    """
     Parameters
    ----------
    speaker_name : string
        name of speaker whose voice to be cloned

    Returns
    -------
    filepath : string
        speaker audio file path
        
    """
    pass

def save_audio_local(generated_wav):
    pass

def synthesized_voice(text, speaker_name):
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
    in_fpath = Path("src\samples\honey_singh.mp3") # Audio file to be synthesized, can be changed to audio file of choice, refer synthesizer.py
    reprocessed_wav = encoder.preprocess_wav(in_fpath)
    original_wav, sampling_rate = librosa.load(in_fpath)
    preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
    embed = encoder.embed_utterance(preprocessed_wav)
    print("Synthesizing new audio...")
    with io.capture_output() as captured:
        specs = synthesizer.synthesize_spectrograms([text], [embed])
    generated_wav = vocoder.infer_waveform(specs[0])
    generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")
    print("Synthesized audio generated")

    return generated_wav, synthesizer.sample_rate


if __name__ == "__main__" :
    
    print(synthesized_voice("text", "asdasdad"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import librosa
import numpy as np

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
    ## TODO implement this function if you want to change the speaker 
    pass

def save_audio_local(generated_wav, speaker_name, sample_rate):
    
    save_dir = 'src\samples\Original Samples'
    file_path = os.path.join(save_dir, speaker_name + "_synthesized.mp3")
    librosa.output.write_wav(file_path, generated_wav, sample_rate)

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
    sample_dir = "src\samples\Original Samples"
     
    in_fpath = os.path.join(sample_dir, speaker_name + '.mp3') # Audio file to be synthesized, can be changed to audio file of choice, refer synthesizer.py
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
    
    ## For saving samples you can call save_audio_local
    ## save_audio_local(generated_wav, speaker_name, synthesizer.sample_rate)

    return generated_wav, synthesizer.sample_rate


if __name__ == "__main__" :
    
    print(synthesized_voice("text", "asdasdad"))
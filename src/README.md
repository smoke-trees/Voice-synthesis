# **Real time Voice cloning and TTS based Model**

The aim of this project is to design a model for converting any text to any speakers voice based on user selection. The project has two parts namely

- Voice Cloning
- Text to speech synthesis

## **Research work**

**Text to speech synthesis** <br>

### **Approaches for TTS**

All the TTS based systems are judged base on 2 factors

- Naturalness
- Intelligibility 

There are two specific methods for Text-to-Speech(TTS) conversion. Parametric TTS and Concatenative TTS.

- Concatenative approach:
    - Relies on high quality sound
    - Restricitve and requires huge data
    - Combines diferent speeches to synthesise new speeech
    - Sounds clean but no emotions and phenotically not sound
    - Intelligable but not natural

- Parametric approach:
    - Less restricitve
    - Statisitical approach and uses sound features like spectrum, freq, amplitude
    - More robust and requires less data 
    

#### Parametric approach or Statistical Approach

<br/>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/TTS_System.svg/550px-TTS_System.svg.png"/>
</p>
<br/>
<br/>
Occurs in 2 stages

- Extract lingusitic features like phonemes, duration etc.
- Extract vocoder features of sound like spectrum, cepstra, freq etc. [Engineered features]

**Vocoder** <br/><br/>
It is a mathematical model which take in the engineered features and linguistics one to create waveforms which will gice correct TTS ouput taking into consideration things like phase, prosody(rhythm and stress), intonation, etc.

#### Drawbacks
- Time consuming
- Error prone
- Lot of manipulative values need to be decided


### **Deep Learning approach (Our approach)**

We will be using the deep learning approach for the Synthesis process.

The best way to produce tts synthesis output is to produce directly the sound samples rather than audio waveforms in a time series format and the generating the audio from it.

The models that we tested and experimented with:
- [Wavenet/Melnet](https://arxiv.org/abs/1609.03499) : Data requirement was very high and cannot afford that.
- [DeepVoice](https://arxiv.org/abs/1702.07825) : This model works on few samples but the result were not satisfying.
- [SV2TTS](https://arxiv.org/pdf/1806.04558.pdf) : Real time Voice cloning with zero shot learning. The thing we were looking for so we went ahead with it.

#### SV2TTS Model - Real time Voice cloning (Model we are using!!)

A NN based approach for text-to-speech (TTS) synthesis that is able to generate speech audio in the voice of different speakers, including those
unseen during training (The reason why we chose it !).
<br>

The model is having three independent neural networks trained independently: <br>
1. Speaker Encoder Network(Encoder): This model identifies the speaker based on his voice waveforms and generate an ebedding vector for that speaker.
2. Synthesizer (Seq-Seq Network): This model is used to create a mel-spectogram from text using embedding vectors of speaker. This model is based on [Tacotron2](https://arxiv.org/abs/1712.05884)
3. Vocoder(Auto-Regressive Model): This model generate waveforms from the mel spectogram using the auto-regressive Wavenet based Vocoder network.
<br><br>

<p align="center">
<img src="..\Assets\model_overview.PNG"/>
</p>


## **About Datasets**

- The datasets required for training speaker emebedding vectors are done on the following datasets:
    - [Librispeech Dataset](http://www.openslr.org/12/) : LibriSpeech is a corpus of approximately 1000 hours of 16kHz read English speech. The data is derived from read audiobooks from the LibriVox project, and has been carefully segmented and aligned. The data used specifically here are :
        - LibriSpeech/test-clean
        - LibriSpeech/test-other
        - LibriSpeech/dev-clean
        - LibriSpeech/dev-other
        - LibriSpeech/train-clean-100
        - LibriSpeech/train-clean-360
        - LibriSpeech/train-other-500

    - [LibriTTS Dataset](https://research.google/tools/datasets/libri-tts/) : LibriTTS is a multi-speaker English corpus of approximately 585 hours of read English speech at 24kHz sampling rate. The LibriTTS corpus is designed for TTS research. It is derived from the original materials (mp3 audio files from LibriVox and text files from Project Gutenberg) of the LibriSpeech corpus. The data used here are :
        - LibriTTS/test-clean
        - LibriTTS/test-other
        - LibriTTS/dev-clean
        - LibriTTS/dev-other
        - LibriTTS/train-clean-100
        - LibriTTS/train-clean-360
        - LibriTTS/train-other-500
    
    - [VoxCeleb Dataset](http://www.robots.ox.ac.uk/~vgg/data/voxceleb/) : VoxCeleb is an audio-visual dataset consisting of short clips of human speech, extracted from interview videos uploaded to YouTube. The data used here are:
        - VoxCeleb1
        - VoxCeleb2

- The Celebrity Samples that we tested the model on are:
    - [Honey Singh](samples/Original_Samples)
    - [Samuel A Jackson](samples/Original_Samples)


## Results and Findings

We tested the samples of English actors and celebrities and we managed to get great results on some of the actors.

- Experiment with honey singh voice sample: The results of the model on this sample was very good on custom text. Even the indian accent was fairly cloned. The visualization of the spectogram is given below:<br>
    <p align="center">
    <img src="..\Assets\Results\hs1.PNG"/>
    </p>

    The result of this experiment can be found [here](ENTER_URL_OF_AUDIO_SAMPLE)  

- Experiment with Samuel A Jackson Sample : The result was very astonishing for us and we managed to get awesome results on any custom text. The visual graphs of the spectograms is given below:<br>

    <p align="center">
    <img src="..\Assets\Results\sj1.PNG"/><br><br>
    <img src="..\Assets\Results\sj2.PNG"/>
    </p>

    The result of this experiment can be found [here](ENTER_URL_OF_AUDIO_SAMPLE)  










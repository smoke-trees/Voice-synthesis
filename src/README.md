# Real time Voice cloning and TTS based Model

The aim of this project is to design a model for converting any text to any speakers voice based on user selection. The project has two parts namely

- Voice Cloning
- Text to speech synthesis

## Research work

### Text to speech synthesis

#### Approaches for TTS

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

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/TTS_System.svg/550px-TTS_System.svg.png" align="center"/>

<br/>
<br/>
Occurs in 2 stages

- Extract lingusitic features like phonemes, duration etc.
- Extract vocoder features of sound like spectrum, cepstra, freq etc. [Engineered features]

**Vocoder** <br/><br/>
It is a mathematical model which take in the engineered features and linguistics one to create waveforms which will gice correct TTS ouput taking into consideration things like phase, prosody(rhythm and stress), intonation, etc.

This approach has some drawbacks
- Time consuming
- Error prone
- Lot of manipulative values need to be decided


#### Deep Learning approach (Our approach)

We will be using the deep learning approach for the Synthesis process.

The best way to produce tts synthesis output is to produce directly the sound samples rather than audio waveforms in a time series format and the generating the audio from it.

The model that we will be using is DeepVoice model which is also termed Neural Voice Sampling model by BAIDU






## Steps to Execute

- Create a virtual env

    ``` bash
    virtualenv env
    ```
    If you dont have virtualenv check it out here to [install](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)
  
- Activate the virtualenv

    Windows

    ``` bash
    cd env/scripts
    activate
    ```
    Linux

    ``` bash
    source ./env/bin/activate
    ```
- Install all the requirements

    ``` bash 
    pip install -r requirements.txt
    ```
- Run jupyter notebook for executing the notebook

    ``` bash
    jupyter notebook
    ``` 

    ## Status of work

    In progress

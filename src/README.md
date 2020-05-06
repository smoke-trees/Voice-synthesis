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
    <img src="..\Assets\Results\sj2.PNG"/>
    </p>

    The result of this experiment can be found [here](ENTER_URL_OF_AUDIO_SAMPLE)  


## Training Your Own Custom Model

This section basically defines the procedure you have to do indorder to train your own model on your custom dataset.

### Data Requirements
Inorder to train models on your own custom dataset. You need to follow the following steps

- Find a multispeaker dataset of the particular language you want to synthesize. It should have following specifications
    - Multispeaker voice samples (As many as possible). 
    - Propely annotated
    - Phoenotics of each syllable clearly defined
- Clean you datasets using some audio tools like [Audacity](https://www.audacityteam.org/). You can remove the backgrund noise from the audio to make it more resonating and clear.
- Some of the probable type of audio recording can be considered for celebrity actors voice samples are:
    - Youtube Videos of Interviews
    - Monologues from any film
    - Speech given by any celebrities<br> 


The audio synthesis in any language can be done based on the availability of an annotated data.
Some of the data sources where you can search for data is:
- [Google dataset Search Engine](https://datasetsearch.research.google.com/)
- [Kaggle](https://www.kaggle.com/)
- [TDIL](https://tdil-dc.in/index.php?lang=en)
- [IndicTTS](https://www.iitm.ac.in/donlab/tts/database.php)


### Steps to train your own model

In order to train your own model you should take the following steps:

- Setup your environment
    - Pre-Requisites
        - GPU
        - Python (3.6 or 3.7)
        - Nvidia Drivers
        - CUDA compatible with your NVIDIA Drivers
        - Requirement Packages
        - IDE
    - Get the code from the repo by cloning it.

- Configure your Encoder model on your custom speaker dataset and create new embeddings
    - Edit you encoder configurations and tweak the code based on your language preference
    - Train the new embeddings which can be found in this [folder](pre_train/encoder)
    <br>
    
    Details about the encoder model can be found [here](encoder/README.md)

- Change the syntheiszer and generate new mel spectograms based on your new embedding vectors. All the trained model checkpoints can be found [here](pretrain/synthesizer). <br>
All the details about the synthesizer can be found [here](synthesizer/README.md)

- Finally change the Vocoder network and generate new waveforms in synthesized form. All the trained model checkpoints can be found [here](pretrain/vocoder). <br>
All the details about the vocoder can be found [here](vocoder/README.md)


### Steps to test your model

Follow the details for testing the model in this [file](./synthesize.py)
- Load all the trained models
    ``` python
    encoder_weights = Path("pre_train/encoder/saved_models/pretrained.pt")
    vocoder_weights = Path("pre_train/vocoder/saved_models/pretrained/pretrained.pt")
    syn_dir = Path("pre_train/synthesizer/saved_models/logs-pretrained/taco_pretrained")
    encoder.load_model(encoder_weights)
    synthesizer = Synthesizer(syn_dir)
    vocoder.load_model(vocoder_weights)
    ```
- Pass the custom text to the synthesize function and get the generated waveform in the foerm of numpy arrays.
    ``` python
    def synthesized_voice(text, speaker_name):

        sample_dir = "src\samples\Original Samples"
        in_fpath = os.path.join(sample_dir,         speaker_name + '.mp3') 
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

    ```
- You can even save this generated waveform by passing it to the following function
    ``` python
    def save_audio_local(generated_wav, speaker_name, sample_rate):
    
        save_dir = 'src\samples\Synthesised_Samples'
        file_path = os.path.join(save_dir, speaker_name + "_synthesized.mp3")
        librosa.output.write_wav(file_path, generated_wav, sample_rate)
    ```
    All the saved files can be found [here](samples/Synthesised_Samples)

    You can run the following file by the following command:
    ``` bash
    ## If you are in root of the work dir
    cd src
    python synthesize.py
    ```


There is a testing [jupyter notebook](test/voice_synthesis_example.ipynb) included for convenience.









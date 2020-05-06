pip install -q -r requirements.txt
apt-get install -qq libportaudio2

#for getting all the prerained embeddings
cd src/pre_train
gdown https://drive.google.com/uc?id=1n1sPXvT34yXFLT47QZA6FIRGrwMeSsZc
unzip pretrained.zip


<p align="center">
	<h2 align="center"> Voice Cloning and Text to Speech Synthesis</h2>
	<h4 align="center"> A Standalone service for cloning your own voice and synthesize any text in English in your own voice.<h4>
</p>
<br>

Read more about the procedure we followed and the findings [here](src/README.md)

---

## Functionalities
- [X]  Clone voices after feeding samples to it
- [X]  Synthesized voice on custom texts
- [X]  Speech-to-text facility for input using microphones
- [X]  RestAPI with a testing UI for testing the model

<br>


## Instructions to run the trained models 

If you want to try and test out the samples trained and how the model is performing on custom text you can follow these instructions.<br>


* Pre-requisites:

	- For Windows
		-  python (3.6 or 3.7 works best)
		-  virtualenv <br>
			> If you dont have virtualenv check it out here to [install](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)
		- Trained embeddings from [here](https://drive.google.com/uc?id=1n1sPXvT34yXFLT47QZA6FIRGrwMeSsZc)

	- For linux<br>
		- Bash shell for executing the scripts

* Directions to install:

	- For windows
		- Clone the repo 
		- Setup Virtualenv
			``` cmd
			virtualenv env
			cd env/scripts
			activate
			```
		- Install all requirements packages
			``` cmd
			pip install -r requirements.txt
			```
	- For Linux
		- Run the run.sh file to install the project
			``` bash
			./run.sh
			```

	<br> 
	After installing all the dependencies and environment prerequisites run the below file to check you are ready and good to go!<br>
	
	``` bash
	cd src
	python3 check_env.py
	```

* Directions to execute

	- Test through interface
		- Start the python flask server 
			``` python 
			python app.py
			```
		- Log on to localhost:5000 to test the model

	- Test through the Synthesize function
		- Follow the instructions given [here](src/README.md)

<br>

## Instructions to train your own models

If you want to work with the source code and want to train your own models on different dataset and different language medium you can check out the instructions mentioned [here](src/README.md)
<br><br>
For more information about the samples tested and there results you can get all the information from [here](src/README.md)

## Contributors

* [SMOKE TREES](https://github.com/smoke-trees)
* [TANMAY](https://github.com/Tanmay244)




import os
import io
import base64
import json

from flask import Flask, request , make_response, Response, render_template
from flask_cors import CORS,cross_origin
import pyaudio
import numpy

# from src import synthesize as syn

# Initialize the Flask application
app = Flask(__name__)
## for allowing cors origin
cors = CORS(app, allow_headers='Content-Type', CORS_SEND_WILDCARD=True)

	
# route http posts to this method
@app.route('/api/test' , methods=['POST','GET'])
@cross_origin(origins='*', send_wildcard=True)
def synthesize_speech_sound(): 
    
    target_text = request.form.get('target_text')
    target_speaker = request.form.get('target_speaker')
    
    if target_text == '':
        data = {'status' : 'No target text provided'}
        return Response(json.dumps(data), status=401, mimetype='application/json')
    
    if target_speaker == '':
        data = {'status' : 'No target speaker provided'}
        return Response(json.dumps(data), status=402, mimetype='application/json')
    
    # output, RATE = syn.synthesized_voice(target_text, target_speaker)
    output = 'ashgdasgdhasgdh'
    def generate():
        
        fwav = io.StringIO(output.tobytes())
        data = fwav.read(1024)
        while data:
            yield data
            data = fwav.read(1024)
            
   
    return Response(generate(), mimetype="audio/mp3")

        
@app.route('/')
def index():
    
    """ Audio streaming home page. """
    
    return render_template('test_stream.html')

# start flask app
if __name__ == "__main__":
    
    ## Change debug to False when deployed to production
    app.run(debug=True,host="localhost", port=5000)
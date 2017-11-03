from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import speech_recognition as sr

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'aabhososjfk'
socketio = SocketIO(app)

#initialize default microphone source ---Important Note--speech recognition requires pyaudio
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
#recognize speech input
try:
    print("You said " + r.recognize(audio))
except LookupError:
    print("Could not understand audio")

#Transcribe a WAV audio file


#Start the chat server

@app.route('/')
def index():
    return render_template('./ChatApper.html')

@socketio.on('my event')
def cust_evhandler(json):
    print('receive something: ' + str(json))
    socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)
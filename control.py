from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/on')
def on():
    GPIO.output(11, GPIO.HIGH)
    return render_template('on.html')

@app.route('/off')
def off():
    GPIO.output(11, GPIO.LOW)
    return render_template('off.html')

if __name__ == '__main__':
    app.run(debug=True)
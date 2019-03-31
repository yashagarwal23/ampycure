from flask import Flask, request
from flask import jsonify
from werkzeug.utils import secure_filename
import threading, os

app = Flask(__name__)

result_list = [0, 0, 0]

def autism_check(filename):
    from Autism.AutismCheck import predict
    prediction = predict(filename)
    result_list[0] = int(prediction[0])


def parkinson_check(filename):
    from Parkinson.ParkinsonCheck import predict
    prediction = predict(filename)
    result_list[1] = int(prediction[0])


def depression_check(filename):
    from Depression.DepressionCheck import predict
    prediction = predict(filename)
    result_list[2] = int(prediction[0])


@app.route('/check', methods = ['POST', 'GET'])
def predict():
    if request.method == 'GET':
        filename = "sample.wav"
    elif request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)
    autism_thread = threading.Thread(target=autism_check, args=[filename])
    parkinson_thread = threading.Thread(target=parkinson_check, args=[filename])
    depression_thread = threading.Thread(target=depression_check, args=[filename])

    autism_thread.start()
    parkinson_thread.start()
    depression_thread.start()

    autism_thread.join()
    parkinson_thread.join()
    depression_thread.join()

    if filename != 'sample.wav':
        os.remove(filename)

    return jsonify(result_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


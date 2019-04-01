from flask import Flask, request
from flask import jsonify
from werkzeug.utils import secure_filename
import threading, os

app = Flask(__name__)

done = False
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


@app.route('/')
def index():
    return "Apmycure Homepage"


def diagnose(filename):
    autism_thread = threading.Thread(target=autism_check, args=[filename])
    parkinson_thread = threading.Thread(target=parkinson_check, args=[filename])
    depression_thread = threading.Thread(target=depression_check, args=[filename])

    autism_thread.start()
    parkinson_thread.start()
    depression_thread.start()

    autism_thread.join()
    parkinson_thread.join()
    depression_thread.join()

    global done
    done = True

    if filename != 'sample.wav':
        os.remove(filename)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(filename)
    diagnose_thread = threading.Thread(target=diagnose, args=[filename])
    diagnose_thread.daemon = True
    diagnose_thread.start()

    return "upload done"


@app.route('/done', methods=['POST', 'GET'])
def done_func():
    return "true" if done else "false"


@app.route('/getresult', methods=['POST', 'GET'])
def return_result():
    global done
    done = False
    return jsonify(result_list)


if __name__ == '__main__':
    app.run()


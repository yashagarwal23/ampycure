from flask import Flask, request
from flask import jsonify
from werkzeug.utils import secure_filename
import threading, os

app = Flask(__name__)

results = {"autism" : 0};

def autism_check(filename):
    from Autism.AutismCheck import predict
    prediction = predict(filename)
    results['autism'] = str(prediction[0])


@app.route('/check', methods = ['POST', 'GET'])
def predict():
    if request.method == 'GET':
        filename = "Autism/sample.wav"
    elif request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)
    autism_thread = threading.Thread(target=autism_check(filename))
    autism_thread.start()
    autism_thread.join()
    if filename != 'Autism/sample.wav':
        os.remove(filename)
    return jsonify({"results": results})


if __name__ == '__main__':
    app.run(host='0.0.0.0')


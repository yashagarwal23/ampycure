from flask import Flask
from flask import jsonify
import threading

app = Flask(__name__)

results = {"autism" : 0};

def autism_check(filepath):
    from Autism.AutismCheck import predict
    prediction = predict(filepath)
    results['autism'] = str(prediction[0])


@app.route('/check')
def predict():
    filepath = ""
    autism_thread = threading.Thread(target=autism_check(filepath))
    autism_thread.start()
    autism_thread.join()
    return jsonify({"results": results})


if __name__ == '__main__':
    app.run()


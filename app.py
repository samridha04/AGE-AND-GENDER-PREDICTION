from flask import Flask, render_template, jsonify, request, redirect, url_for
from prediction import getAgeGender

app = Flask(__name__)

mediaDir = "./static/uploaded/"

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        print("Post request sent on Home Page.")
        return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        f = request.files['upload']
        if f.filename != "":
            image_path = mediaDir + f.filename
            uploaded_file_path = "uploaded/" + f.filename
            f.save(image_path)
            age, gender = getAgeGender(image_path)
            return render_template("prediction.html", AGE=age, GENDER=gender, FILEPATH=uploaded_file_path)
        else:
            return render_template("no_image.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, use_reloader=True, debug=True)

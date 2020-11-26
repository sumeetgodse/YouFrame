import requests,os,re
from flask import Flask,redirect,url_for,render_template,request
from werkzeug.utils import secure_filename

app=Flask(__name__)

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/uploader")
def uploader():
        path = 'static/uploads/'
        uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
        print(uploads)
        #uploads = os.listdir('static/uploads')
        uploads = ['uploads/' + file for file in uploads]
        uploads.reverse()
        return render_template("index.html",uploads=uploads)

app.config['UPLOAD_PATH'] = 'static/uploads'
@app.route("/upload",methods=['GET','POST'])
def upload_file():
        if request.method == 'POST':
                f = request.files['file']
                print(f.filename)
                #f.save(secure_filename(f.filename))
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
                return redirect("/uploader")

if __name__=="__main__":
    app.run()

from flask import Flask,render_template,url_for,request,url_for,jsonify
import requests
app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def home():
    status= "closed"
    if request.method == 'POST':
        if request.form['bt'] == 'opened': 
            status="opened"
            return render_template("website.html",state = status) 
        elif request.form['bt'] == 'closed': 
            status="closed"
            return render_template("website.html",state = status)
        else:
            pass
    return render_template("website.html",state = status )




if __name__ == "__main__":
    app.run(debug=True)

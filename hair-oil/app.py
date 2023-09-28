from flask import Flask,render_template,sessions,request, session
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('oil.html')

 @app.route('/submit' ,methods=["GET","POST"])
 def submit():
    name = request.form.get("name")
    return render_templet('greet.html',person=name)


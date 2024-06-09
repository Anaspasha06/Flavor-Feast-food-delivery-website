from flask import Flask,render_template,url_for
app = Flask(__name__)
@app.route('/')
def start():
    return render_template('start.html')

@app.route('/order')
def order():
   return render_template('order.html')

@app.route('/sign')
def singup():
   return render_template('sign.html')

@app.route('/login')
def login():
   return render_template('login.html')
+9
if __name__ == '__main__':
    app.run(debug=True)

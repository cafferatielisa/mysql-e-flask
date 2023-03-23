from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', name='Elisa')


    @app.route('/units')
def unitList():
        mycursor.execute("SELECT * FROM Clash_Unit")
        my result = mycursur.fetchall()
        return render_template('clash_units.html', units=myresult)
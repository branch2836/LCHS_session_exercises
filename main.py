from flask import Flask, request, redirect, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():

    
    if request.method == 'POST':
        
        guess=int(request.form['guess'])
        magic_number = session['magic_number']
        high = session['high_value']
        low= session['low_value']

        if guess < low or guess > high:
            message = "Invalid entry: Please enter a number within the range"
        else:
            if guess == magic_number:
                message = "CORRECT!"
                session['still_guessing'] = False
            elif guess < magic_number:
                message = "Your guess is too low"
                session['low_value']= guess
            elif guess > magic_number:
                message = "your guess is too high"
                session['high_value']= guess


    else:
        low_value = 1
        high_value = 25
        session["magic_number"] = random.randint(low_value, high_value)
        session["high_value"] = high_value
        session["low_value"] = low_value
        session['still_guessing'] = True
        message = ''


    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run()

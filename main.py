from flask import Flask, request, redirect, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        low_value = 1
        high_value = 25
        session["magic_number"] = random.randint(low_value, high_value)
        session["high_value"] = high_value
        session["low_value"] = low_value

        message = ''

    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run()

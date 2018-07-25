from flask import Flask, render_template, request
from typograph import launch_typograph
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = 'secret_key'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def form(formatted_text=None):
    if request.method == 'POST':
        user_text = request.form['text']
        formatted_text = launch_typograph(user_text)
    return render_template('form.html', formatted_text=formatted_text)


if __name__ == "__main__":
    app.run()

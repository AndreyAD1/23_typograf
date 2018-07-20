from flask import Flask, render_template, request
from typograph import launch_typograph


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form(edited_text=None):
    if request.method == 'POST':
        user_text = request.form['text']
        edited_text = launch_typograph(user_text)
        print(edited_text)
    return render_template('form.html', edited_text=edited_text)


if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import subprocess


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class MyForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET', 'POST'])

def index():
    form = MyForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename).replace("\\", "")
        file.save(os.path.join('static/files', filename))
        print(f'processing {filename}')
        subprocess.run(['whisper',  f'static/files/{filename}', '--model', 'medium.en'])
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0')




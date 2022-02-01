from flask import Flask, render_template, redirect, url_for
from forms import CreateForm
from make_markov import make_markov_fun

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

@app.route("/", methods = ['GET', 'POST'])
def create_model():
    form = CreateForm()
    if form.validate_on_submit():
        return redirect(url_for('lyrics'))
    return render_template('home.html', form = form)
    
@app.route('/lyrics', methods = ['GET', 'POST'])
def lyrics():
    fob = make_markov_fun()
    return render_template('lyrics.html', fob = fob)

if __name__ == '__main__':
    app.run()


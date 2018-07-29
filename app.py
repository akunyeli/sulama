from flask import Flask
from flask import render_template

app = Flask(__name__)




@app.route('/')
def index():
    animal=['sinem','Ahmet','ünal']
    return render_template('anasayfa.html',value=animal)


if __name__ == '__main__':
    app.run()

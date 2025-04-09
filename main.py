from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index02')
def index02():
    return render_template('index02.html')

@app.route('/index03')
def index03():
    return render_template('index03.html')

@app.route('/index04')
def index04():
    return render_template('index04.html')

@app.route('/index05')
def index05():
    return render_template('index05.html')

@app.route('/index06')
def index06():
    return render_template('index06.html')

if __name__ == '__main__':
    # Para ejecutar localmente. En Render se usa Gunicorn (Procfile)
    app.run(debug=True, host='0.0.0.0', port=5000)

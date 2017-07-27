from flask import Flask, render_template
import subprocess

# INIT
data = {}
app = Flask(__name__)

ip = subprocess.check_output(['hostname', '-I'])
data['ip'] = ip

# WEB
@app.route("/")
def index():
    return render_template('index.html', data = data)


# RUN
if __name__ == "__main__":
    app.run(host = '0.0.0.0')

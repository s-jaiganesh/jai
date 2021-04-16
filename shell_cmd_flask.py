import flask
import subprocess

app = flask.Flask(__name__)

@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['df -hP'],             # OS Command you want to run
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):     # Loop the command stdout and add Line breaker <br> 
            yield line.rstrip() + (b'<br>\n')

    return flask.Response(inner(), mimetype='text/html')

app.run(debug=True, port=5000, host='0.0.0.0') # Change the port number as you wish

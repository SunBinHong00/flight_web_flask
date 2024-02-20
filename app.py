import os
import ssl

from flask import Flask, render_template

app = Flask(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.load_cert_chain(
    certfile=r"./ssl/crt.pem",
    keyfile=r"./ssl/key.pem",
)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, ssl_context=ssl_context)

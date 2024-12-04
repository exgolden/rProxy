import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Home route"""
    service_name = os.getenv("SERVICE_NAME", "default service")
    return f"Service {service_name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

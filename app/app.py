import logging
from flask import Flask

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return "Hello DevOps! My application is deployed on Render with CI/CD."

@app.route("/health")
def health():
    app.logger.info("Health check requested")
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000)

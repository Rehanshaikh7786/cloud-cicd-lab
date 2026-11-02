import os, platform, socket
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template
app = Flask(__name__)
NAME = os.getenv("APP_NAME", "CLOUD//NEXUS")
VERSION = os.getenv("APP_VERSION", "2.0.0")
@app.get("/")
def home(): return render_template("index.html", app_name=NAME, version=VERSION)
@app.get("/health")
def health(): return jsonify(status="healthy", service=NAME, version=VERSION, timestamp=datetime.now(timezone.utc).isoformat()), 200
@app.get("/ready")
def ready(): return jsonify(ready=True), 200
@app.get("/api/info")
def info(): return jsonify(name=NAME, version=VERSION, environment=os.getenv("APP_ENV","production"), python=platform.python_version(), hostname=socket.gethostname(), platform=platform.system())
@app.get("/student")
def student(): return jsonify(name="Cloud CI/CD Lab", course="Cloud Computing and DevOps", message="Automated delivery, from commit to container.")
@app.errorhandler(404)
def not_found(_error): return jsonify(error="Not found"), 404
if __name__ == "__main__": app.run(host="0.0.0.0", port=int(os.getenv("PORT","5000")), debug=False)

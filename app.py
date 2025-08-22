from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="")

# Serve transcripts folder
@app.route("/transcripts/<path:filename>")
def serve_transcript(filename):
    return send_from_directory("transcripts", filename)

# Root page
@app.route("/")
def index():
    return send_from_directory("", "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
import os
from flask import Flask, request, jsonify
from app.whisper_service import transcribe_audio
from app.extract_info import extract_profile
from app.models import save_user_profile, init_db
from app.models import get_all_profiles
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
init_db()

@app.route("/upload-audio", methods=["POST"])
def upload_audio():
    file = request.files['audio']
    path = os.path.join("uploads", file.filename)
    file.save(path)
    
    transcription = transcribe_audio(path)
    profile = extract_profile(transcription)
    save_user_profile(transcription, profile)

    return jsonify({"message": "Success", "profile": profile})


@app.route("/profiles", methods=["GET"])
def get_profiles():
    profiles = get_all_profiles()
    return jsonify(profiles)


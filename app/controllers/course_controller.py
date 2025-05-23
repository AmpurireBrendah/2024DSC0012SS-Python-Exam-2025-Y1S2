from flask import Blueprint, request, jsonify
from app.extensions import db
from models import course

app =Blueprint('student',__name__)


# Create a new courses
@app.route('/course', methods=['POST'])
def create_course():
    data=request.get_json()

    if not data or "name" not in data or "code" not in data or "duration" not in data:
        return jsonify({"Error":"Student values required"}),400

    course=course(
    name=data["name"],
    code=data["code"],
    duration=data["duration"]
    )
    db.session.add(course)
    db.commit()
    return jsonify(course.to_dict()),201






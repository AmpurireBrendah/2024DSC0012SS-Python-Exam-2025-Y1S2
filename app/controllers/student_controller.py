from flask import Blueprint, request, jsonify
from app.extensions import db
from models import student

app =Blueprint('student',__name__)

# Create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data=request.get_json()

    if not data or "name" not in data or "gender" not in data or "email" not in data or "contact" not in data or  "address" not in data:
        return jsonify({"Error":"Student values required"}),400

    student=student(
    name=data["name"],
    gender=data["gender"],
    email=data["email"],
    address=data["address"],
    contact=data["contact"]
   )
    db.session.add(student)
    db.commit()
    return jsonify(student.to_dict()),201

# Fetch all students
@app.route('/students', methods=['GET'])
def get_students():
    students=student.query.all()
    return jsonify(student.to_dict() for student in students),200

#Delete a student
@app.route('/students/<int:id>', methods=["DELETE"])
def delete_student(id):
    student=student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"Message":"Student deleted."}),200


from flask import Blueprint, request, jsonify
from app.extensions import db
from models import student

app =Blueprint('student',__name__)

# Create a new programs
@app.route('/program', methods=['POST'])
def create_program():
    data=request.get_json()

    if not data or "name" not in data or "start_date" not in data or "end_date" not in data:
        return jsonify({"Error":"Invalid details entered"}),400

    program=program(
    name=data["name"],
    start_date=data["start_date"],
    end_date=data["end_date"]
    )
    db.session.add(program)
    db.commit()
    return jsonify(program.to_dict()),201

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

# Update a program
@app.route('/program/<int:id>', methods=["PUT"])
def update_program(id):
    program=program.query.get_or_404(id)
    data=request.get_json()

    if data in "name":
        program.name=data["name"]
        if data in "start_date":
            program.start_date=data["start_date"]
            if data in "end_date":
                program.end_date=data["end_date"]

                db.session.commit()
                return jsonify(program.to_dict()),200

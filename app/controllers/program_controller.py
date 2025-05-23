from flask import Blueprint, request, jsonify
from app.extensions import db
from models import program

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

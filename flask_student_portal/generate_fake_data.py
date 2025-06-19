import random
from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, StudentMark 
from app import app  

fake = Faker()

# List of possible subjects
subjects = ["Physics", "Chemistry", "Biology", "Math", "English"]

# Clear existing data (optional)
def clear_data():
    StudentMark.query.delete()
    db.session.commit()

# Create fake student entries
def create_fake_students(n=3):
    rolls_used = set()

    for _ in range(n):
        # Ensure unique roll number
        while True:
            roll = random.randint(100, 999)
            if roll not in rolls_used:
                rolls_used.add(roll)
                break

        name = fake.first_name()
        gender = random.choice(["M", "F"])
        for subject in random.sample(subjects, k=3):  # Each student gets 3 random subjects
            marks = random.randint(40, 100)
            s = StudentMark(
                roll=roll,
                name=name,
                gender=gender,
                subject=subject,
                marks=marks
            )
            db.session.add(s)

    db.session.commit()
    print(f"✅ {n} students with subject marks created.")

if __name__ == "__main__":
    with app.app_context():
        clear_data()  # remove if you don't want to clear existing data
        create_fake_students()

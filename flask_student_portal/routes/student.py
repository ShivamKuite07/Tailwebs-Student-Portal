from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, StudentMark
from forms import StudentForm
from flask import request


# for suppressing cache in browser
from functools import wraps
from flask import make_response


student = Blueprint('student', __name__)


# Decorator to suppress caching in browser
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache

# @student.route('/dashboard')
# @login_required
# @nocache
# def dashboard():
#     students = StudentMark.query.order_by(StudentMark.roll).all()
#     return render_template('dashboard.html', students=students)



@student.route('/dashboard')
@login_required
@nocache
def dashboard():
    roll = request.args.get('roll')
    name = request.args.get('name')
    subject = request.args.get('subject')
    page = request.args.get('page', 1, type=int)
    per_page = 5  # 🔁 Change this as needed

    query = StudentMark.query

    if roll:
        query = query.filter(StudentMark.roll == roll)
    if name:
        query = query.filter(StudentMark.name.ilike(f"%{name}%"))
    if subject:
        query = query.filter(StudentMark.subject.ilike(f"%{subject}%"))

    filters = {
        'roll': roll,
        'name': name,
        'subject': subject
    }


    pagination = query.order_by(StudentMark.roll).paginate(page=page, per_page=per_page)
    students = pagination.items

    return render_template(
        'dashboard.html',
        students=students,
        pagination=pagination,
        filters=filters
    )




@student.route('/add', methods=['GET', 'POST'])
@login_required
@nocache
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        existing = StudentMark.query.filter_by(roll=form.roll.data, subject=form.subject.data).first()
        if existing:
            flash('Student with this subject already exists. Updating marks.', 'info')
            existing.name = form.name.data
            existing.gender = form.gender.data
            existing.marks += form.marks.data
            db.session.commit()
            flash("Student record updated.", "info")
        else:
            student = StudentMark(
                roll=form.roll.data,
                name=form.name.data,
                gender=form.gender.data,
                subject=form.subject.data,
                marks=form.marks.data
            )
            db.session.add(student)
            db.session.commit()
            flash("Student added.", "success")
        return redirect(url_for('student.dashboard'))
    return render_template('add_student.html', form=form)

@student.route('/student_detail/<int:roll>')
@login_required
@nocache
def student_detail(roll):
    records = StudentMark.query.filter_by(roll=roll).all()
    if not records:
        flash("No student found.", "warning")
        return redirect(url_for('student.dashboard'))

    total = sum(s.marks for s in records)
    name = records[0].name
    gender = records[0].gender
    return render_template('student_detail.html', records=records, name=name, roll=roll, gender=gender, total=total)



@student.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@nocache
def edit_student(id):
    student = StudentMark.query.get_or_404(id)
    form = StudentForm(obj=student)

    if form.validate_on_submit():
        # ✅ update marks for this specific subject
        student.subject = form.subject.data
        student.marks = form.marks.data

        # ✅ update name and gender for all entries with same roll
        all_with_roll = StudentMark.query.filter_by(roll=student.roll).all()
        for s in all_with_roll:
            s.name = form.name.data
            s.gender = form.gender.data

        db.session.commit()
        flash("Student updated successfully.", "success")
        return redirect(url_for('student.dashboard'))

    return render_template('add_student.html', form=form, edit=True)





# 🧨 Delete specific subject record by ID
@student.route('/delete/<int:id>', methods=['POST'])
@login_required
@nocache
def delete_subject(id):
    record = StudentMark.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    flash("Subject entry deleted.", "success")
    return redirect(url_for('student.dashboard'))

# 🧨 Delete all subject marks for a student by roll
@student.route('/delete_student/<int:roll>', methods=['POST'])
@login_required
@nocache
def delete_student(roll):
    records = StudentMark.query.filter_by(roll=roll).all()
    if not records:
        flash("Student not found.", "warning")
        return redirect(url_for('student.dashboard'))
    for r in records:
        db.session.delete(r)
    db.session.commit()
    flash("All records for student deleted.", "success")
    return redirect(url_for('student.dashboard'))







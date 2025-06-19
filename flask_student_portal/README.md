# 🎓 Tailwebs Student Portal - Shivam Kuite 🤖

<image src="tailwebs-demo.png" />

A simple and modern web app for teachers to manage student subject-wise marks, built using Flask, 
Bootstrap, and SQLite. This app allows teacher login, adding students, editing marks, 
and viewing subject-wise reports per student.

## 🚀 Features

- 👨‍🏫 **Teacher Signup/Login/Logout**
- 🧑‍🎓 **Add Student + Subject Marks**
- ✏️ **Edit Student Info/Marks**
- 🗑️ **Delete**: entire student / individual subject marks for that student
- 📊 **Dashboard**: Subject-wise mark records
- 📄 **Student Detail View**: All marks with total
- 🧠 **Smart Add**: Updates marks if same student+subject exists
- 💡 **Bulk Info Update**: Changing name/gender updates all records for that roll number
- ✅ **Bootstrap 5** - Clean UI  
- 🌓 **Dark mode support** - Dark mode, light mode support
- 📱 **Responsive Design**: Works on mobile and desktop
- 🔍 **Filters** Search filters using rollno, name, subject
- 📑 **Pagination**: Pagination for large datasets

## 🛠️ Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Backend       | Python, Flask     |
| Database      | SQLite + SQLAlchemy ORM |
| Forms/Validation | Flask-WTF         |
| Auth & Sessions | Flask-Login       |
| Frontend      | HTML5, Bootstrap 5 |
| Structure     | Blueprint-based MVC |

## 🧱 Folder Structure

```py
myproject/
├── venv/                      ← your virtual environment
├── requirements.txt
└── flask_student_portal/
    ├── app.py
    ├── config.py
    ├── models.py
    ├── forms.py
    ├── routes/
    │   ├── auth.py
    │   └── student.py
    ├── templates/
    │   ├── layout.html
    │   ├── login.html
    │   ├── signup.html
    │   ├── dashboard.html
    │   ├── add_student.html
    │   └── student_detail.html
    └── static/
```


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository


git clone https://github.com/your-username/flask-student-portal.git
cd flask-student-portal


### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate #source venv/bin/activate # on macOS/Linux
```


### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```


### 4️⃣ Run the app


cd flask_student_portal
python app.py



Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 5️⃣ Generate Fake Data (Optional)
If you want to populate the database with some sample data for testing, run:

```bash
python generate_fake_data.py
```



## 🔐 Auth Flow

1. **Sign Up** → create teacher account
2. **Login** → access student dashboard
3. **Logout** → ends session

## 🧮 Student Management Flow

* **Add Student**:
  * Enter Roll, Name, Gender, Subject, Marks
  * If the subject already exists for that student: updates marks
* **Edit Entry**:
  * Modifies marks + subject for that specific record
  * Updates **name/gender for all entries with same roll**
* **Detail Page**:
  * Shows all subjects and total marks for a student

## 💡 Future Improvements

* 📤 Export to PDF/CSV
* 🔐 Admin panel for teachers

## 🙌 Credits

Developed by Shivam Kuite
- email: shivamkuite77@gmail.com

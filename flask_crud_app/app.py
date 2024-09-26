from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data: in-memory storage (use a database for a real app)
students = []

# Home route: Display all students (Read)
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Route to add a new student (Create)
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    students.append({'name': name, 'age': age})
    return redirect(url_for('index'))

# Route to delete a student (Delete)
@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    if student_id < len(students):
        students.pop(student_id)
    return redirect(url_for('index'))

# Route to update a student (Update)
@app.route('/update/<int:student_id>', methods=['POST'])
def update_student(student_id):
    if student_id < len(students):
        students[student_id]['name'] = request.form['name']
        students[student_id]['age'] = request.form['age']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8080,debug=True)

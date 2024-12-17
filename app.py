from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas (en memoria, puedes usar una base de datos si quieres persistencia)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        if task_name:
            tasks.append({'name': task_name, 'completed': False})
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todo_items = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todo_items.append(task)
        return redirect(url_for('index'))
    
    return render_template('index.html', tasks=todo_items)

if __name__ == '__main__':
    app.run(debug=True)

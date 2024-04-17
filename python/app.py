from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    project_due_date = datetime(2024, 5, 12)
    current_date = datetime.now()
    time_difference = project_due_date - current_date
    if time_difference.total_seconds() <= 0:
        return render_template('project_due.html')
    else:
        remaining_days = time_difference.days
        return render_template('countdown.html', days=remaining_days, image_url='/static/img1.jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

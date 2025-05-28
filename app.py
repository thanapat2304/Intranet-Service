from flask import Flask, render_template
from backend.career import get_hr_tb
from backend.contact import get_fda_phon_mai
from backend.km import get_km_tb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    total_data = get_fda_phon_mai()
    return render_template('contact.html', results=total_data)

@app.route('/career')
def career():
    db_jobs = get_hr_tb()

    jobs = [
        {
            'title': job['hr_position'],
            'positions': f"{job['hr_quantity']} ตำแหน่ง" if job['hr_quantity'] else "หลายตำแหน่ง",
            'update_date': job['hr_date'].strftime('%B %d, %Y'),
            'file': job['hr_file']
        }
        for job in db_jobs
    ]

    return render_template('career.html', jobs=jobs)

@app.route('/km')
def km():
    db_jobs = get_km_tb()

    jobs = [
        {
            'title': job['km_manual'],
            'update_date': job['km_date'].strftime('%B %d, %Y'),
            'file': job['km_file']
        }
        for job in db_jobs
    ]

    return render_template('kmportal.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=8080)
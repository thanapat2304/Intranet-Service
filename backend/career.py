from backend.db_connection import connect_aep_portal

def get_hr_tb():
    import random
    from datetime import datetime, timedelta

    positions = ['วิศวกร', 'นักวิเคราะห์', 'ผู้จัดการโครงการ', 'เจ้าหน้าที่บุคคล', 'นักบัญชี']
    files = ['resume1.pdf', 'resume2.pdf', 'resume3.pdf', 'resume4.pdf', 'resume5.pdf']

    results = []
    for _ in range(10):
        position = random.choice(positions)
        quantity = random.randint(1, 5)
        hr_date = datetime.now() - timedelta(days=random.randint(1, 365))
        hr_file = random.choice(files)

        row = {
            'hr_position': position,
            'hr_quantity': quantity,
            'hr_date': hr_date,
            'hr_file': hr_file
        }
        results.append(row)

    return results
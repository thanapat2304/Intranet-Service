from backend.db_connection import connect_aep_portal

def get_fda_phon_mai():
    import random

    first_names = ['สมชาย', 'สมหญิง', 'วิชัย', 'ณัฐพร', 'ปิยะ']
    last_names = ['ใจดี', 'ทรงศรี', 'วัฒนกุล', 'บุญมา', 'ทิพย์รักษ์']
    nicknames = ['บอล', 'จูน', 'ตั้ม', 'กิ๊ฟ', 'บอย']
    departments = ['IT', 'HR', 'บัญชี', 'คลังสินค้า', 'วิศวกรรม']
    phone_prefix = ['000', '000', '000', '000', '000']
    email_domains = ['@gmail.com', '@company.com', '@mail.com']

    results = []
    for i in range(1, 11):  # สร้างข้อมูล 10 แถว
        emp_id = f"EMP{str(i).zfill(3)}"
        f_name = random.choice(first_names)
        l_name = random.choice(last_names)
        n_name = random.choice(nicknames)
        department = random.choice(departments)
        phon = f"{random.choice(phone_prefix)}-{random.randint(1000000, 9999999)}"
        email = f"{f_name.lower()}.{l_name.lower()}{random.choice(email_domains)}"

        row = {
            'EMPid': emp_id,
            'F_Name': f_name,
            'L_Name': l_name,
            'N_Name': n_name,
            'Department': department,
            'Phon': phon,
            'Email': email
        }
        results.append(row)

    return results
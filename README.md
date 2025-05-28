# Intranet Service

ระบบ Intranet Service เป็นเว็บแอปพลิเคชันภายในองค์กรที่พัฒนาด้วย Flask Framework โดยมีฟีเจอร์หลักดังนี้:

## ฟีเจอร์หลัก 🚀

- **หน้าแรก (Home)** - แสดงข้อมูลหลักและการนำทางของระบบ
- **บริการ (Service)** - แสดงรายการบริการต่างๆ ที่มีให้บริการ
- **เกี่ยวกับ (About)** - ข้อมูลเกี่ยวกับองค์กรและระบบ
- **ติดต่อ (Contact)** - ข้อมูลการติดต่อและสมุดโทรศัพท์ภายในองค์กร
- **ตำแหน่งงาน (Career)** - แสดงตำแหน่งงานที่เปิดรับสมัคร พร้อมรายละเอียดและเอกสารที่เกี่ยวข้อง
- **การจัดการความรู้ (KM Portal)** - ระบบจัดการความรู้ภายในองค์กร แสดงคู่มือและเอกสารต่างๆ

## การติดตั้ง 🛠️

1. ติดตั้ง Python 3.x
2. Clone repository นี้:
```bash
git clone [repository-url]
cd Intranet-Service
```

3. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

## การใช้งาน 💻

1. รันแอปพลิเคชัน:
```bash
python app.py
```

2. เปิดเบราว์เซอร์และเข้าถึงระบบที่:
```
http://localhost:8080
```

## โครงสร้างโปรเจค 📁

```
Intranet-Service/
├── app.py              # ไฟล์หลักของแอปพลิเคชัน
├── requirements.txt    # รายการ dependencies
├── runtime.txt         # กำหนดเวอร์ชัน Python
├── Procfile.eddx      # คำสั่งสำหรับ deployment
├── backend/           # โค้ดส่วน backend
├── static/            # ไฟล์ static (CSS, JS, Images)
└── templates/         # ไฟล์ HTML templates
```

## เทคโนโลยีที่ใช้ 🔧

- **Flask** - Python Web Framework
- **Jinja2** - Template Engine
- **Werkzeug** - WSGI Web Application Library
- **Gunicorn** - Python WSGI HTTP Server

## การ Deploy 🚀

ระบบนี้สามารถ deploy ได้โดยใช้ Gunicorn เป็น production server

## ความต้องการของระบบ 📋

- Python 3.x
- รายการ dependencies ทั้งหมดอยู่ใน `requirements.txt`

## การพัฒนาเพิ่มเติม 🔄

1. Fork repository นี้
2. สร้าง branch ใหม่สำหรับฟีเจอร์ที่ต้องการพัฒนา
3. Commit การเปลี่ยนแปลง
4. Push ไปยัง branch ของคุณ
5. สร้าง Pull Request

## ผู้พัฒนา 👥

ธนภัทร โสภณ
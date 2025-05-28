from backend.db_connection import connect_aep_portal
from datetime import datetime

def get_km_tb():
    mock_data = [
        {"km_manual": "คู่มือการใช้งานระบบ TSDP Portal", "km_date": datetime(2025, 5, 1), "km_file": "manual_aep_portal.pdf"},
        {"km_manual": "แนวทางการใช้วัตถุดิบอย่างปลอดภัย", "km_date": datetime(2025, 4, 20), "km_file": "safety_guideline.pdf"},
        {"km_manual": "วิธีการสั่งซื้อวัตถุดิบผ่านระบบ", "km_date": datetime(2025, 3, 15), "km_file": "order_process_manual.pdf"},
        {"km_manual": "คู่มือฝึกอบรมพนักงานใหม่", "km_date": datetime(2025, 1, 10), "km_file": "training_guide.pdf"},
        {"km_manual": "นโยบายความปลอดภัยอาหาร", "km_date": datetime(2024, 12, 5), "km_file": "food_safety_policy.pdf"}
    ]

    return mock_data
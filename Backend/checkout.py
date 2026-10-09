from datetime import datetime, timedelta, timezone


THAI_TIME = timezone(timedelta(hours=7))

# ตรวจชื่อและเบอร์โทร
def check_name(name):
    if name.strip() == "":
        return "กรุณากรอกชื่อผู้รับอาหาร"

    return ""
def check_phone(phone):
    phone = phone.strip()

    if phone == "":
        return "กรุณากรอกเบอร์โทรศัพท์"

    if not phone.isascii() or not phone.isdigit():
        return "เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น"

    if len(phone) != 10:
        return "เบอร์โทรต้องมี 10 หลัก"

    if not phone.startswith("0"):
        return "เบอร์โทรต้องขึ้นต้นด้วย 0"

    return ""

def check_pickup_time(pickup_date, pickup_time, now=None):
    text = pickup_date.strip() + " " + pickup_time.strip()
    try:
        pickup = datetime.strptime(text, "%Y-%m-%d %H:%M")
    except ValueError:
        return "กรุณากรอกวันและเวลาที่มีอยู่จริง เช่น 2026-10-11 และ 12:30"

    if pickup.strftime("%Y-%m-%d %H:%M") != text:
        return "ใช้วันที่ YYYY-MM-DD (ค.ศ.) และเวลา HH:MM"

    # เทียบด้วยเวลาไทย แม้เครื่องจะตั้งเขตเวลาอื่น
    pickup = pickup.replace(tzinfo=THAI_TIME)
    if now is None:
        now = datetime.now(THAI_TIME)
    if pickup <= now:
        return "กรุณาเลือกเวลารับอาหารในอนาคต"
    return ""


def check_details(name, phone, pickup_date, pickup_time):
    # เจอข้อผิดพลาดข้อไหน ให้ส่งข้อความข้อนั้นกลับก่อน
    error = check_name(name)
    if error:
        return error
    error = check_phone(phone)
    if error:
        return error
    return check_pickup_time(pickup_date, pickup_time)

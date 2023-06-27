import random


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp(phone_number, otp):
    # Implement your OTP sending logic here (e.g., using SMS gateways or other services)
    pass

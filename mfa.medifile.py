import pyotp

secret = "DCEUUWIMB7JG2DE7VTJZXI6STT7HNPA4"
totp = pyotp.TOTP(secret)
input_code = input("Enter the code: ")
if input_code != "123456":
    print("saiiii")
    exit()
# mã otp
otp  =  input("Enter the OTP: ")
if totp.verify(otp):
    print("OTP đúng")
else:
    print("OTP saiiiiiiiiiiii")
    exit()
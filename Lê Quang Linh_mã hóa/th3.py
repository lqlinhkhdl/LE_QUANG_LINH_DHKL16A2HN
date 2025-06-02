import pyotp
import qrcode

secret = pyotp.random_base32()
print("Secret:", secret)
with open("secret.txt", "w") as f:
    f.write(secret)
top = pyotp.TOTP(secret)
uri = top.provisioning_uri("user@example061.com", issuer_name="SecureApp")
img = qrcode.make(uri)
img.save("qrcode.png")
print("QR code saved as qrcode.png")
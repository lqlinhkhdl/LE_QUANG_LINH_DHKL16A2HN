from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
cipher = AES.new(key, AES.MODE_CBC)  # Create a new AES cipher object in CBC mode

plaintext = b'This is a secret message that needs to be encrypted.'  # Example plaintext

start_time = time.time()  # Start time for encryption
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))  # Encrypt the plaintext
end_time = time.time()  # End time for encryption
aes_encryption_time = end_time - start_time  # Calculate encryption time

print(f"Ciphertext: {ciphertext.hex()}")  # Print the ciphertext in hexadecimal format
print(f"Encryption time: {aes_encryption_time:.6f} seconds")  # Print the encryption time

# giải mã
start_time = time.time()  # Start time for decryption
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)  # Create a new AES cipher object for decryption
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)  # Decrypt the ciphertext
end_time = time.time()  # End time for decryption
aes_decryption_time = end_time - start_time  # Calculate decryption time

print(f"Decrypted: {decrypted.decode()}")  # Print the decrypted plaintext
print(f"Decryption time: {aes_decryption_time:.6f} seconds")  # Print the decryption time
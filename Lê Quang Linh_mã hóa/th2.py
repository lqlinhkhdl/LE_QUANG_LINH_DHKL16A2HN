from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
from Crypto.Random import get_random_bytes

key = RSA.generate(2048)  # Generate a new RSA key pair
private_key = key.export_key()  # Export the private key        
public_key = key.publickey().export_key()  # Export the public key

aes_key = get_random_bytes(16)  # Generate a random AES key
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))  # Create a new RSA cipher object

start_time = time.time()  # Start time for encryption
ciphertext = cipher_rsa.encrypt(aes_key)  # Encrypt the AES key with RSA 
end_time = time.time()  # End time for encryption
rsa_encryption_time = end_time - start_time  # Calculate encryption time        

print(f"Ciphertext: {ciphertext.hex()}")  # Print the ciphertext in hexadecimal format
print(f"Encryption time: {rsa_encryption_time:.6f} seconds")  # Print the encryption time
# giải mã   

decipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))  # Create a new RSA cipher object for decryption
start_time = time.time()  # Start time for decryption   
decrypted_aes_key = decipher_rsa.decrypt(ciphertext)  # Decrypt the AES key
end_time = time.time()  # End time for decryption
rsa_decryption_time = end_time - start_time  # Calculate decryption time
print(f"Decrypted AES key: {decrypted_aes_key.hex()}")  # Print the decrypted AES key in hexadecimal format 
print(f"Decryption time: {rsa_decryption_time:.6f} seconds")  # Print the decryption time

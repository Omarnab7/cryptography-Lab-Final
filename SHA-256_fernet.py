from cryptography.fernet import Fernet

class FernetEncryptor:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)
        return
    
    def encrypt(self, ct: str|bytes, out=bytes|str):
        if type(ct) == str:
            ct = ct.encode('utf-8')
        encrypted_text = self.cipher.encrypt(ct)

        if out == bytes:
            return encrypted_text
        elif out == str:
            return encrypted_text.hex()

import hashlib    
def hash_sha256(data: bytes, out=str|bytes):
    hash_obj = hashlib.sha256(data)

    if out == str:
        return hash_obj.hexdigest()
    elif out == bytes:
        return hash_obj.digest() 

def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    encryptor = FernetEncryptor()
    print(encryptor.encrypt(b"Bruhhh", str))
    print(encryptor.encrypt(b"Bruhhh", bytes))

    hash_sha256(b"Bah Bah Black Ship")

# # Decrypt
# decrypted_text = cipher.decrypt(encrypted_text).decode()
# print("Decrypted:", decrypted_text)
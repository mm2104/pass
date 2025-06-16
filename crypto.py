def encrypt_password(password: str, key: bytes) -> bytes:
    from cryptography.fernet import Fernet
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted_password: bytes, key: bytes) -> str:
    from cryptography.fernet import Fernet
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

def generate_key() -> bytes:
    from cryptography.fernet import Fernet
    return Fernet.generate_key()
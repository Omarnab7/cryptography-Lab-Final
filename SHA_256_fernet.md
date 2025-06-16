# 🔐 Encryption & Hashing Utilities

A simple Python module that provides:

- AES encryption using Fernet.
- SHA-256 hashing for strings and files.

---

## 📦 Dependencies

```bash
pip install cryptography
```

---

## 📄 Overview

This module contains:

- `FernetEncryptor`: Class to encrypt data using the `Fernet` symmetric encryption.
- `hash_sha256()`: Function to hash byte data using SHA-256.
- `hash_file()`: Function to hash a file's contents using SHA-256.

---

## 🔐 FernetEncryptor Class

### ✅ Constructor

```python
FernetEncryptor(key=None)
```
- `key` (optional): Provide a Fernet key. If not provided, a new one will be generated.

### 🔒 Methods

#### `encrypt(ct: str | bytes, out=bytes | str)`

Encrypts the given content.

- `ct`: The plaintext as `str` or `bytes`.
- `out`: Output format. Either `bytes` or `str` (hex encoded).

**Returns:** Encrypted data in specified format.

---

## 🧮 Hashing Functions

### `hash_sha256(data: bytes, out=str | bytes)`

Hashes the given byte data using SHA-256.

- `data`: Input data as `bytes`.
- `out`: Output format (`str` for hex, `bytes` for raw digest).

**Returns:** SHA-256 hash.

---

### `hash_file(file_path)`

Hashes a file's contents using SHA-256.

- `file_path`: Path to the file.

**Returns:** Hex digest of the file hash.

---

## 🚀 Usage Example

```python
if __name__ == "__main__":
    encryptor = FernetEncryptor()
    print(encryptor.encrypt(b"Bruhhh", str))
    print(encryptor.encrypt(b"Bruhhh", bytes))

    print(hash_sha256(b"Bah Bah Black Ship"))
```

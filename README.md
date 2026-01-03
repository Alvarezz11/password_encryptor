# password_encryptor
This project is a simple Python-based tool designed for educational purposes. How common hashing algorithms (`MD5`, `SHA1`, `SHA256`) work by converting plain text into unique hexadecimal representations.

## Features
- **Multiple Algorithms**: Support for MD5, SHA1, and SHA256.
- **Console Interface**: Simple and direct interaction through the terminal.
- **Secure Encoding**: Uses Python's standard `hashlib` library.

## Requirements
- **Python 3.x**: Ensure you have Python installed on your system.

## How to use
1. Clone the repository or download the `encryptor.py` file.
2. Open a terminal in the project folder.
3. Run the program with:
   ```bash
   python encryptor.py
   ```
4. Follow the on-screen instructions to enter text and select the desired algorithm.
5. Type `salir` (exit) to close the program.

## How the Code Works
The encryption script follows these steps:
1. **Data Input**: The user enters the plain text they wish to hash.
2. **Algorithm Selection**: Choice between `MD5`, `SHA1`, and `SHA256`.
3. **Encoding to Bytes**: The text is converted to a byte format (`utf-8`) using `.encode()`, as hashing functions require this input.
4. **Hash Generation**: The standard `hashlib` library is used to process the bytes and generate a hash object.
5. **Hexadecimal Conversion**: `.hexdigest()` is used to obtain a readable string in hexadecimal format.

---
**Educational Note**: This project is designed to demonstrate basic cryptography and hashing concepts.

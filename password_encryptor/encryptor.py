import hashlib

def encrypt_text(text, algorithm):
    """
    Hashes the input text using the specified algorithm.
    Supported algorithms: md5, sha1, sha256.
    """
    # Convert text to bytes
    text_bytes = text.encode('utf-8')
    
    # Select the algorithm
    if algorithm == 'md5':
        hash_obj = hashlib.md5(text_bytes)
    elif algorithm == 'sha1':
        hash_obj = hashlib.sha1(text_bytes)
    elif algorithm == 'sha256':
        hash_obj = hashlib.sha256(text_bytes)
    else:
        return None
    
    # Return the hexadecimal representation of the digest
    return hash_obj.hexdigest()

def main():
    print("--- Generador de Hashes (MD5, SHA1, SHA256) ---")
    
    while True:
        text = input("\nIntroduce el texto a encriptar (o 'salir' para terminar): ")
        if text.lower() == 'salir':
            break
            
        print("\nAlgoritmos disponibles:")
        print("1. MD5")
        print("2. SHA1")
        print("3. SHA256")
        
        choice = input("Selecciona una opción (1-3): ")
        
        algorithm = ""
        if choice == '1':
            algorithm = 'md5'
        elif choice == '2':
            algorithm = 'sha1'
        elif choice == '3':
            algorithm = 'sha256'
        else:
            print("Opción no válida.")
            continue
            
        result = encrypt_text(text, algorithm)
        
        if result:
            print(f"\nResultado ({algorithm.upper()}): {result}")
        else:
            print("Error al procesar el hash.")

if __name__ == "__main__":
    main()

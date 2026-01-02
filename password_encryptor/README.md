# Password Encryptor - Generador de Hashes Educativo

## Resumen
Este proyecto es una herramienta sencilla basada en Python diseñada para fines educativos. Permite a los estudiantes y entusiastas de la ciberseguridad comprender cómo funcionan los algoritmos de hashing comunes (`MD5`, `SHA1`, `SHA256`) al convertir texto plano en representaciones hexadecimales únicas.

## Características
- **Múltiples Algoritmos**: Soporte para MD5, SHA1 y SHA256.
- **Interfaz de Consola**: Interacción simple y directa a través de la terminal.
- **Codificación Segura**: Utiliza la biblioteca estándar `hashlib` de Python.

## Requisitos
- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.

## Cómo usar
1. Clona el repositorio o descarga el archivo `encryptor.py`.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el programa con:
   ```bash
   python encryptor.py
   ```
4. Sigue las instrucciones en pantalla para introducir el texto y seleccionar el algoritmo deseado.
5. Escribe `salir` para cerrar el programa.

---
**Nota Educativa**: Este proyecto está diseñado para demostrar conceptos básicos de criptografía y hashing. No debe ser utilizado para almacenar contraseñas reales en sistemas de producción sin implementar medidas de seguridad adicionales como "salting" y algoritmos más robustos (ej. Argon2 o bcrypt).

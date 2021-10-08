import pyaes, pbkdf2, binascii, os, secrets
def AES(plain_text, key):
    plaintext = plain_text
    password = key
    # Derive a 256-bit AES encryption key from the password
    passwordSalt = os.urandom(16)
    aes_encryption_key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    # Encrypt the plaintext with the given key:
    #   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
    iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(aes_encryption_key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    encrypted_msg = binascii.hexlify(ciphertext)
    # Decrypt the ciphertext with the given key:
    #   plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
    aes = pyaes.AESModeOfOperationCTR(aes_encryption_key, pyaes.Counter(iv))
    decrypted_msg = aes.decrypt(ciphertext)
    encrypted_msg = str(encrypted_msg)
    decrypted_msg = str(decrypted_msg)
    return encrypted_msg[2:-1], decrypted_msg[2:-1]

def DES(pain_text, key):
    from pyDes import des
    key = key
    text= pain_text
    d = des(key)
    encrypted_msg = d.encrypt(text)
    decrypted_msg = d.decrypt(encrypted_msg)
    encrypted_msg = binascii.hexlify(encrypted_msg)

    encrypted_msg = str(encrypted_msg)
    decrypted_msg = str(decrypted_msg)
    return encrypted_msg[2:-1], decrypted_msg[2:-1]

def CC(plain_text):
    import pycaesarcipher
    text = plain_text
    key = 3
    caesarcipher = pycaesarcipher.pycaesarcipher()
    encrypted_msg = caesarcipher.caesar_encipher(text,key)
    decrypted_msg = caesarcipher.caesar_decipher(encrypted_msg,key)
    return encrypted_msg, decrypted_msg

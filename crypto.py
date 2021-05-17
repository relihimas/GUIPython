from cryptography.fernet import Fernet

key = Fernet.generate_key()

usuario = 'rachid'
senha = '123454'
compac_senha = senha.encode("UTF-8")

cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(compac_senha)
print(ciphered_text)

unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)

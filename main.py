from flask import Flask, request, render_template
import webbrowser
from algo import AES, DES, CC
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('form.html')

@app.route('/cryptography', methods=['POST','GET'])
def cryptography():
    inputedKey = ''
    encryptedMsg = ''
    decryptedMsg = ''

    inputedAlgo = request.form.get("algorithm")
    inputedPlainText = request.form.get("plainText")
    inputedAlgoName = ''
    if inputedAlgo == '0':
        inputedAlgoName = 'AES (Advanced Encryption Standard)'
        inputedKey = request.form.get("key")
        encryptedMsg, decryptedMsg = AES(inputedPlainText, inputedKey)

    elif inputedAlgo == '1':

        inputedAlgoName = 'DES (Data Encryption Standard)'
        inputedKey = request.form.get("key1")
        encryptedMsg, decryptedMsg = DES(inputedPlainText, inputedKey)

    elif inputedAlgo == '2':
        inputedAlgoName = 'Caesar Cipher'
        inputedKey = '3'
        encryptedMsg, decryptedMsg = CC(inputedPlainText)

    return render_template('returnedTemplate.html', input_algo=inputedAlgoName,
                        input_plain_text=inputedPlainText, input_key=inputedKey,
                        encrypted_msg=encryptedMsg, decrypted_msg=decryptedMsg)

if __name__ == "__main__":
    print("Startiing Python Flask Server For Text cryptography...")
    app.run()
    webbrowser.open('http://127.0.0.1:5000/index')

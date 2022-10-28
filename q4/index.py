
import pathlib
import rsa


def load_public_key(keyPath):
    with open(keyPath, 'rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
    return publicKey


def load_private_key(keyPath):
    with open(keyPath, 'rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    return privateKey


def verifyAuthenticity(file, pubKey, assinatura):
    with open(file, 'rb') as f:
        try:
            content = f.read()[:-256]
            return rsa.verify(content, assinatura, pubKey) == 'SHA-256'
        except:
            return False


while True:
    print('-------------------------------')
    print("Assinatura digital é na TEUSZIN SIGN, FORGET TUDO.")
    print("Como podemos lhe ajudar?")
    print('-------------------------------')
    print(" ")
    print("[1] - Verificar Autenticidade da assinatura")
    print("[0] - Sair")

    command = int(input("Escolha uma opção: "))

    if command == 1:
        signedFilePath = input('Informe o caminho do arquivo assinado: ')
        publicKeyPath = input('Informe o caminho da chave publica: ')
        publicKey = load_public_key(publicKeyPath)
        sign = open(signedFilePath, 'r').read()[-256:]
        signInBytes = bytes.fromhex(sign)
        result = verifyAuthenticity(signedFilePath,
                                    pubKey=publicKey, assinatura=signInBytes)

        if result:
            print('*********************')
            print('Assinatura autêntica')
            print('*********************')
        else:
            print('*********************')
            print('Assinatura não é autêntica')
            print('*********************')

    elif (command == 0):
        exit = str(input("Deseja realmente sair? (S/N): "))
        if (exit == 's' | 'S'):
            break

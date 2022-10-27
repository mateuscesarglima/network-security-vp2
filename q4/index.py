
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
            content = f.read(pathlib.Path(file).stat().st_size - 256 - 1)
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
        sign = open(signedFilePath, 'r').read().split('/')[1]
        signInBytes = bytes.fromhex(sign)
        verifyAuthenticity(signedFilePath,
                           pubKey=publicKey, assinatura=signInBytes)

        if verifyAuthenticity:
            print('Assinatura autentica')
        else:
            print('Assinatura náo é autêntica')

    elif (command == 0):
        exit = str(input("Deseja realmente sair? (S/N): "))
        if (exit == 's' | 'S'):
            break

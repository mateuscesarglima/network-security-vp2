import rsa


def generate_keys():
    public_key, private_key = rsa.newkeys(1024)
    with open('keys/publicKey.pem', 'wb') as f:
        f.write(public_key.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as f:
        f.write(private_key.save_pkcs1('PEM'))


def load_public_key(keyPath):
    with open(keyPath, 'rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
    return publicKey


def load_private_key(keyPath):
    with open(keyPath, 'rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    return privateKey


def signFile(file, privKey):
    fileContent = open(file, 'r').read()
    with open(file, 'rb') as f:
        signature = rsa.sign(f.read(), privKey, "SHA-256")
        fileName = f.name.split('/')[1].split('.')[0]
        open(f'files/{fileName}__signed.txt',
             'w').writelines([fileContent, signature.hex()])
        return signature


while True:
    print('-------------------------------')
    print("Assinatura digital é na TEUSZIN SIGN, FORGET TUDO.")
    print("Como podemos lhe ajudar?")
    print('-------------------------------')
    print(" ")
    print("[1] - Assinar arquivo ")
    print("[0] - Sair")
    command = int(input("Escolha uma opção: "))

    if command == 1:
        filePath = input('Informe o caminho do arquivo para assinatura: ')
        privateKeyPath = input('Informe o caminho da chave privada: ')
        publicKeyPath = load_public_key('keys/publicKey.pem')
        privateKey = load_private_key(privateKeyPath)
        assinatura = signFile(filePath, privateKey)

        print('*******************************')
        print('Arquivo assinado com sucesso!')
        print('*******************************')

    elif (command == 0):
        exit = input("Deseja realmente sair? (S/N): ")
        if exit == 's' or 'S':
            break

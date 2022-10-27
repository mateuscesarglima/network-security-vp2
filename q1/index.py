import rsa


def gerarChaves():
    chave_publica, chave_privada = rsa.newkeys(1024)
    with open('chaves/chavepublica.pem', 'wb') as f:
        f.write(chave_publica.save_pkcs1('PEM'))
    with open('chaves/chaveprivada.pem', 'wb') as f:
        f.write(chave_privada.save_pkcs1('PEM'))


def carregarChaves():
    with open('chaves/chavepublica.pem', 'rb') as f:
        chavePublica = rsa.PublicKey.load_pkcs1(f.read())
    with open('chaves/chaveprivada.pem', 'rb') as f:
        chavePrivada = rsa.PrivateKey.load_pkcs1(f.read())
    return chavePublica, chavePrivada


def criptografarMensagem(msg, chave):
    return rsa.encrypt(msg.encode('ascii'), chave)


def descriptografarMensagem(textoCifrado, chave):
    try:
        return rsa.decrypt(textoCifrado, chave).decode('ascii')
    except:
        return False


# PASSO 1 - GERAR AS CHAVES PUBLICA E PRIVADA
gerarChaves()
# PASSO 2 - CARREGAR AS CHAVES PUBLICAS E PRIVADAS
chavePub, chavePriv = carregarChaves()
# PASSO 3 - Mensagem que vai ser enviada
mensagem = 'Estou apenas testando'
# PASSO 4 - Criptografar a mensagem que vai ser enviada com a chave publica gerada
textoCifrado = criptografarMensagem(mensagem, chavePub)
# PASSO - 6 recebe uma mensagem e a chave privada criada para descriptografar a mensagem
mensagemDescriptografada = descriptografarMensagem(textoCifrado, chavePriv)

print(" ")
print(f'Mensagem a ser enviada:', mensagem)
print(" ")
print(f'Mensagem criptografada: {textoCifrado}')
print(" ")


if mensagemDescriptografada:
    print(f'Mensagem descriptografada: {mensagemDescriptografada}')
else:
    print("A mensagem não pode ser descriptografada com sua chave privada.")
print(" ")


print(" ")

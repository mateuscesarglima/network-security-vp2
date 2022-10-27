# Criação de uma chave publica e privada com RSA E OpenSSL

## Os comandos abaixos foram utilizados em sistemas UNIX (Mac/Linux)

&nbsp;

## Passo 1

- Gerar a chave privada e armazenar ela em um arquivo chamado private.pem, conforme o código abaixo:

```text
openssl genrsa -out private.pem
```

- Você deve inserir o código acima no seu terminal para gerar uma chave privada através da linha de comando.

## Passo 2

- Gerar a chave publica a partir da chave privada para um novo arquivo chamado public.pem

```text
openssl rsa -in private.pem -pubout -out public.pem
```

- Você deve inserir o código acima no seu terminal para gerar uma chave pública através da linha de comando.

&nbsp;

# Gerar um par de chaves SSH em uma máquina com MacOS ou Linux

1. Abra uma janela do terminal
2. Insira esta linha de comando:

```text
ssh-keygen -t rsa
```

3. Selecione os valores padrão para todas as opções.
   Esse comando gera dois arquivos de chave SSH, id_rsa e id_rsa.pub, no diretório home/username/.ssh, em que username é o seu nome de usuário.

4. Pode ser usado também o seguinte comando:

```text
ssh-keygen -t rsa -N "<pass_phrase>" -b 2048 -C "<key_name>" -f <path/root_name>
```

- **-t rsa**: Informa que é pra usar o algoritmo RSA.
- **-N "pass_phrase"**: Uma frase senha para proteger o uso da chave. Se não quiser fornecer basta apenas deixar as aspas sem digitar nada dentro.
- **-b 2048**: Informa que é pra gerar uma chave de 2048 bits.
- **-C"<key_name>"**: Um nome para identificar a chave.
- **-f "<path/root_name>"**: O local em que o par de chaves será salvo e o noem da raiz dos arquivos.

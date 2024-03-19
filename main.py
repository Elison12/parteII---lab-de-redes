import http.client

def testeDeServidor():
    conexao = http.client.HTTPConnection('localhost', 8080)
    
    conexao.request('GET', '/index.html')
    
    resposta = conexao.getresponse()
    
    conteudo = resposta.read().decode('utf-8')
    
    conexao.close()
    
    if resposta.status == 200:
        print("A página web está Funcionando !")
        # print(conteudo)
    else:
        print("error")

if __name__ == "__main__":
    

    print("Bem vindo ao menu de testes\n")
    print("Para saber se página web está funcionando digite a senha. Dica: número de copas do mundo da seleção brasileira\n")
    while(True):
        senha = input()
        if (senha == '5'):
            print("Senha correta! aguardando resposta...\n")
            testeDeServidor()
            break
        else:
            print("Senha incorreta\n")


import http.client

def testeDeServidor():
    conexao = http.client.HTTPConnection('localhost', 8080)
    
    conexao.request('GET', '/index.html')
    
    resposta = conexao.getresponse()
    
    conteudo = resposta.read().decode('utf-8')
    
    conexao.close()
    
    if resposta.status == 200:
        print(conteudo)
    else:
        print("error")

if __name__ == "__main__":
 
    testeDeServidor()

import os

caminho0 = "lab 7/data/"

while True:
    
    print('+' + 60*'='+'+')
    print("1 - Criar arquivo")
    print("2 - Editar arquivo")
    print("3 - Ler arquivo")
    print("4 - Limpar arquivo")
    print("5 - Criar cópia de arquivo")
    print("6 - Sair")
    print('+' + 60*'='+'+')

    entrada = input("Digite a sua opção: ")
    
    if not entrada.isnumeric():
        print('Entrada inválida')
    else:
        opcao = int(entrada)
        if opcao == 1:
            
            while True:
                print('+' + 60*'='+'+')
                nome = input("Qual nome você deseja colocar no seu arquivo? ")
                caminho = caminho0 + f"{nome}.txt"

                if os.path.exists(caminho):
                    print("Esse arquivo já existe, tente novamente.")
                else:
                    file = open(caminho,"w+")
                    print("Escreva algo para criarmos o arquivo...")
                    conteudo = input()
                    file.write(f'{conteudo}'+' ')
                    file.close()
                    print("Arquivo criado com sucesso!")
                    break   

        elif opcao == 2:
         
            while True:
                print('+' + 60 * '=' + '+')
                print('Digite o nome do arquivo que você quer editar:\n')
                nome = input()
                caminho = caminho0 + f"{nome}.txt"

                if not os.path.exists(caminho):
                    print("Esse arquivo NÃO existe, tente novamente.")
                else:
                    file = open(caminho, 'a+')
                    edicao = input(f'Digite o que você quer a dicionar em {nome}.txt | Digite 0 para retornar\n')
                    if edicao == '0':
                        break
                    else:
                        file.write(f'{edicao}\n')
                        file.close()
                        print(f'Arquivo {nome}.txt editado com sucesso!')

        elif opcao == 3:

            while True:
                print('+' + 60 * '=' + '+')
                print('Digite o nome do arquivo que você quer ler:\n')
                nome = input()
                caminho = caminho0 + f"{nome}.txt"

                if not os.path.exists(caminho):
                    print("Esse arquivo NÃO existe, tente novamente.")
                else:
                    file = open(caminho,'r+')
                    linhas = file.read()
                    print("Arquivo lido com sucesso!")
                    print(60*'/')
                    print(linhas)
                    print(60*'/')
                    file.close()
                    break

        elif opcao == 4:

            while True:
                 
                print('+' + 60 * '=' + '+')
                print('Digite o nome do arquivo que você quer limpar:\n')
                nome = input()
                caminho = caminho0 + f"{nome}.txt"

                if not os.path.exists(caminho):
                    print("Esse arquivo NÃO existe, tente novamente.")
                else:
                    confirmacao = input('Você tem certeza de que quer limpar todo o conteúdo deste arquivo (y/n)?\n')
                    if confirmacao == 'y':
                        file = open(caminho,'w')
                        print("Arquivo limpado com sucesso!")
                        file.close()
                    else:
                        break

        elif opcao == 5:
                while True:
                    print('+' + 60 * '=' + '+')
                    print('Digite o nome do arquivo que você quer copiar:\n')

                    nome = input()
                    caminho = caminho0 + f"{nome}.txt"

                    if not os.path.exists(caminho):
                        print("Esse arquivo NÃO existe, tente novamente.")
                    else:
                        confirmacao = input('Você tem certeza de que quer copiar todo o conteúdo deste arquivo (y/n)?\n')
                        if confirmacao == 'y':

                            file1 = open(caminho,'r+')
                            conteudo = file1.readlines()

                            novoArquivo = input('Digite o nome do arquivo que você irá criar com o conteúdo copiado:\n')
                            novoCaminho = f"lab 7/data/{novoArquivo}.txt"
                            file2 = open(novoCaminho,'w+')

                            for i in range(len(conteudo)):
                                file2.write(conteudo[i])


                            print("Arquivo copiado com sucesso!")
                        else:
                            break
                    break

        elif opcao == 6:
            print("Você escolheu sair do programa.")
            break
        else:
            print('Essa opção não existe!')
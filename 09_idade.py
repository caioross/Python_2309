executar = True

while executar:
    anoNasc = int(input("Em que ano você Nasceu?"))
    anoAtual = int(input("Em que ano estamos?"))
    nome = input("Qual seu nome?")

    idade = anoAtual - anoNasc
    print(f"Olá {nome}, você tem {idade} anos!")
    opcao = input("\nDeseja testar novamente? \nSim ou não?")
    if opcao == "Não" or opcao == "Nao" or opcao == "N" or opcao == "nao":
        executar = False
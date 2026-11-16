import random

print("Jogo Jokenpo")

opcoes = ["Pedra","Papel","Tesoura"]

jogadas = 3

while (jogadas > 0):
    
    jogadas -= 1
    pc= random.choice (opcoes)

    jogador = str(input("Escolha entre Pedra, Papel ou Tesoura:"))

    if (jogador == "Pedra" and pc == "Papel"):
        print("O computador ganhou")
        
    elif (jogador == "Pedra" and pc == "Tesoura"):
        print("O jogador ganhou")
        
    elif (jogador == "Papel" and pc == "Pedra"):
        print("O jogador ganhou")
        
    elif (jogador == "Papel" and pc == "Tesoura"):
        print("O computador ganhou")
        
    elif (jogador == "Tesoura" and pc == "Pedra"):
        print("O computador ganhou")

    elif (jogador == "Tesoura" and pc == "Papel"):
        print("O jogador ganhou")
        
    elif (jogador == pc):
        print("Empate")
            
    if (jogadas == 0):
        print: ("Suas tentativas acabaram")
        refazer = str(input("Gostaria de jogar novamente? (s/n)"))
        if refazer == "s":
            jogadas = 3
            
           

    
    

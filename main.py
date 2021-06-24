import random
import os
escondido = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
sorteio = 0
jogador = 99
tentativa = 12
jogo = True
print("Abra um baú mágico super fantastico e se surpreenda ao não ganhar nada! São baús numerados do 1 ao 36, para abrir o primero digite 1 para abrir o segundo digite 2 e assim por diante. Você tem apenas 12 tentativas, então boa sorte.")
print(" {",escondido[0],"}","{",escondido[1],"}","{",escondido[2],"}","{",escondido[3],"}","{",escondido[4],"}","{",escondido[5],"}\n","{",escondido[6],"}","{",escondido[7],"}","{",escondido[8],"}","{",escondido[9],"}","{",escondido[10],"}","{",escondido[11],"}\n","{",escondido[12],"}","{",escondido[13],"}","{",escondido[14],"}","{",escondido[15],"}","{",escondido[16],"}","{",escondido[17],"}\n","{",escondido[18],"}","{",escondido[19],"}","{",escondido[20],"}","{",escondido[21],"}","{",escondido[22],"}","{",escondido[23],"}\n","{",escondido[24],"}","{",escondido[25],"}","{",escondido[26],"}","{",escondido[27],"}","{",escondido[28],"}","{",escondido[29],"}\n","{",escondido[30],"}","{",escondido[31],"}","{",escondido[32],"}","{",escondido[33],"}","{",escondido[34],"}","{",escondido[35],"}")
sorteio = int(random.randint(1,36))
while jogo == True:
  try:
    if (tentativa == 0):
     print("Fim de jogo.")
     jogo = input("Deseja jogar novamente?\nDigite 'sim' para jogar novamente e 'não' para encerrar.\nVocê: ")
     if(jogo=="sim"):
      jogo = True
      tentativa = 12
      sorteio = int(random.randint(1,36))
      escondido = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
      os.system('clear') or None
      print(" {",escondido[0],"}","{",escondido[1],"}","{",escondido[2],"}","{",escondido[3],"}","{",escondido[4],"}","{",escondido[5],"}\n","{",escondido[6],"}","{",escondido[7],"}","{",escondido[8],"}","{",escondido[9],"}","{",escondido[10],"}","{",escondido[11],"}\n","{",escondido[12],"}","{",escondido[13],"}","{",escondido[14],"}","{",escondido[15],"}","{",escondido[16],"}","{",escondido[17],"}\n","{",escondido[18],"}","{",escondido[19],"}","{",escondido[20],"}","{",escondido[21],"}","{",escondido[22],"}","{",escondido[23],"}\n","{",escondido[24],"}","{",escondido[25],"}","{",escondido[26],"}","{",escondido[27],"}","{",escondido[28],"}","{",escondido[29],"}\n","{",escondido[30],"}","{",escondido[31],"}","{",escondido[32],"}","{",escondido[33],"}","{",escondido[34],"}","{",escondido[35],"}")
     else:
      jogo = False
    elif(jogador != sorteio and tentativa > 0):
     jogador = int(input("\nJogador: "))
     if (jogador <= 0):
       print("Valor inválido")
     else:
      if (escondido[jogador-1] == "_"):
       print("Esse baú já está aberto!")
      else:
       tentativa -= 1
       os.system('clear') or None

       escondido[jogador-1] = "_"
       print(" {",escondido[0],"}","{",escondido[1],"}","{",escondido[2],"}","{",escondido[3],"}","{",escondido[4],"}","{",escondido[5],"}\n","{",escondido[6],"}","{",escondido[7],"}","{",escondido[8],"}","{",escondido[9],"}","{",escondido[10],"}","{",escondido[11],"}\n","{",escondido[12],"}","{",escondido[13],"}","{",escondido[14],"}","{",escondido[15],"}","{",escondido[16],"}","{",escondido[17],"}\n","{",escondido[18],"}","{",escondido[19],"}","{",escondido[20],"}","{",escondido[21],"}","{",escondido[22],"}","{",escondido[23],"}\n","{",escondido[24],"}","{",escondido[25],"}","{",escondido[26],"}","{",escondido[27],"}","{",escondido[28],"}","{",escondido[29],"}\n","{",escondido[30],"}","{",escondido[31],"}","{",escondido[32],"}","{",escondido[33],"}","{",escondido[34],"}","{",escondido[35],"}")
       if (tentativa >1 and jogador != sorteio):
        print("\nVocê ainda possui ",tentativa," tentativas.")
       elif(tentativa == 1 and jogador != sorteio):
        print("\nRESTA APENAS MAIS UMA CHANCE, AMIGO!")
    elif(jogador==sorteio):
     escondido[jogador - 1] = "O"
     os.system('clear') or None
     print(" {",escondido[0],"}","{",escondido[1],"}","{",escondido[2],"}","{",escondido[3],"}","{",escondido[4],"}","{",escondido[5],"}\n","{",escondido[6],"}","{",escondido[7],"}","{",escondido[8],"}","{",escondido[9],"}","{",escondido[10],"}","{",escondido[11],"}\n","{",escondido[12],"}","{",escondido[13],"}","{",escondido[14],"}","{",escondido[15],"}","{",escondido[16],"}","{",escondido[17],"}\n","{",escondido[18],"}","{",escondido[19],"}","{",escondido[20],"}","{",escondido[21],"}","{",escondido[22],"}","{",escondido[23],"}\n","{",escondido[24],"}","{",escondido[25],"}","{",escondido[26],"}","{",escondido[27],"}","{",escondido[28],"}","{",escondido[29],"}\n","{",escondido[30],"}","{",escondido[31],"}","{",escondido[32],"}","{",escondido[33],"}","{",escondido[34],"}","{",escondido[35],"}")
     print("Você acertou! Parabans, Cindy!")
     jogo = input("Deseja jogar novamente?\nDigite 'sim' para jogar novamente e 'não' para encerrar.\nVocê: ")
     if (jogo == "sim"):
      jogo = True
      sorteio = int(random.randint(1,36))
      tentativa = 12
      escondido = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
      os.system('clear') or None
      print(" {",escondido[0],"}","{",escondido[1],"}","{",escondido[2],"}","{",escondido[3],"}","{",escondido[4],"}","{",escondido[5],"}\n","{",escondido[6],"}","{",escondido[7],"}","{",escondido[8],"}","{",escondido[9],"}","{",escondido[10],"}","{",escondido[11],"}\n","{",escondido[12],"}","{",escondido[13],"}","{",escondido[14],"}","{",escondido[15],"}","{",escondido[16],"}","{",escondido[17],"}\n","{",escondido[18],"}","{",escondido[19],"}","{",escondido[20],"}","{",escondido[21],"}","{",escondido[22],"}","{",escondido[23],"}\n","{",escondido[24],"}","{",escondido[25],"}","{",escondido[26],"}","{",escondido[27],"}","{",escondido[28],"}","{",escondido[29],"}\n","{",escondido[30],"}","{",escondido[31],"}","{",escondido[32],"}","{",escondido[33],"}","{",escondido[34],"}","{",escondido[35],"}")
     else:
        jogo = False
  except:
   print("Insira um valor válido!")
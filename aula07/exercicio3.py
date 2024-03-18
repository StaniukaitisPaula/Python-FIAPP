
executar_novamente = True
while executar_novamente == True :
  print("Por favoor digite seu nome:")
  nome = input()
  print("Bom dia", nome)
  print("Você deseja executar o programa novamente? (S/N)")
  resposta = input()
  if resposta == 'S':
    executar_novamente = True
  else:
   executar_novamente = False

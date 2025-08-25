while True:
  nome = input("digite seu nome :")
  vezes = int(input("digite numero de repetições :"))
  n = 1
  while n<=vezes:
        print(nome, "exibido" , n, "vezes")
        n=n+1
  m = input("digite x para sair : ")
  if m=="x":
     break    
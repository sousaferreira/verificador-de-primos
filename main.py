primos = []

while True:
   x = (input("Digite um número ou 'sair' para encerrar"))

   if x.lower() == 'sair' or x == '0':
        break
   
   if  not  x.isdigit():
      print ('Digite números inteiros e positivos')
      continue
   n = int(x)

   if n <= 1:
        print('Não primo')
   elif n ==2:
        primos.append(n)

   else:
    eh_primo = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Não primo")
           
            eh_primo = False
            break
if eh_primo:
    primos.append(n)
else:
    print('Não primo')

print('\n Os números primos são:', primos)





    








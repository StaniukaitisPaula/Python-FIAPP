print("-------Calculo IMC-------")

peso   = float(input("Por favor informe seu peso:"))
altura = float(input("Por favor informe sua altura:"))

imc =  peso /(altura**2)

if imc > 25 :
    print("voce precisa emagrecer")
else:
    print("voce nao precisa emagrecer")

#se colocar int no peso ou altura, tem que dividir por 100 - IMC = peso/((altura/100)**2)    


    

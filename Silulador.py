# Aula de TPA - Professor Júnior Gonçalves 
# Algoritmo para Simulação de Investimento 

while True:
    print("---------------------------------------")
    print("  Seja bem-vindo(a) ao New Order Bank  ")
    print("      SIMULADOR DE INVESTIMENTO        ")
    print("---------------------------------------")

    print(" Investimentos disponíveis: ")
    print("1-Tesouro prefixado 2024")
    print("2-Tesouro prefixado 2026")

    invest= int(input("Qual o titulo que você deseja? 1/2: "))

    if invest == '1':
        valor_investido = int(input("Qual o valor que você quer investir hoje? "))

        valor_mes = int(input("Qual o valor que você pode investir todo mês? "))

#Local está sendo feito os calculos paras os investimento 

        valor_bruto = (valor_mes*32) + valor_investido + 748.23 + (11.49/100)
        IR = (0.10/100) * valor_bruto
        valor_IR = valor_bruto - IR
        B3 = (0.25/100) * valor_bruto
        valor_B3 = valor_bruto - B3
        valor_liquido = valor_bruto - (valor_IR + valor_B3)

#Resultado da Simulação do investimento

        print("-------------------------------")
        print("    RESULTADO DA SIMULAÇÃO     ")
        print("-------------------------------")
        print("Valor inicial investido: R$ ", valor_investido )
        print("Aportes mensais:R$ ", valor_mes)
        print("Valor total investido:R$ ", valor_investido + (valor_mes*32))
        print("Valor Bruto : R$", valor_bruto )
        print("IR: -R$ ", IR  )
        print("Taxa do B3: -R$ ", B3)
        print("Valor líquido: ", valor_liquido)
        print("-------------------------------")
        opcao = str(input("Deseja realizar outra simulação? s/n: "))

#Uma nova simulação de investimento 

    else :
        
        valor_investido = int(input("Qual o valor que você quer investir hoje? "))

        valor_mes = int(input("Qual o valor que você pode investir todo mês? "))

#Local está sendo feito os calculos paras os investimento 

        valor_bruto = (valor_mes*34) + valor_investido + (625/100) + (0.1208/100)
        IR = (0.70/100) * valor_bruto
        valor_IR = valor_bruto - IR
        B3 = (0.25/100) * valor_bruto
        valor_B3 = valor_bruto - B3
        valor_liquido = valor_bruto - (valor_IR + valor_B3)

#Resultado da Simulação do investimento

        print("-------------------------------")
        print("    RESULTADO DA SIMULAÇÃO     ")
        print("-------------------------------")
        print("Valor inicial investido: R$ ", valor_investido )
        print("Aportes mensais:R$ ", valor_mes)
        print("Valor total investido:R$ ", valor_investido + (valor_mes*34))
        print("Valor Bruto : R$", valor_bruto )
        print("IR: -R$ ", IR )
        print("Taxa do B3: -R$ ", B3)
        print("Valor líquido: ", valor_liquido)
        print("-------------------------------")
        opcao = str(input("Deseja realizar outra simulação? s/n: "))
        
        if opcao == 'n':
           break

print("Programa encerrado")








    

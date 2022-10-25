##  Identação

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo = 300
    saldo += valor
#depositar(1000)
#sacar(300)
#sacar(1000)


###    ###

##  EStruturas Condicionais

maior_idade = 18
idade_especial = 12

#idade = int(input("Informe sua idade: "))
idade = 18
if idade >= maior_idade:
    print("Acesso autorizado")
elif (idade >= idade_especial and idade < maior_idade):
    print("Acesso parcialmente autorizado")
else:
    print("Acesso negado")

    ### è possível utilizar outros laços IF dentro de If/Elif

print("\n")
## Estrutura condicional ternaria

saldo = 2000
saque = 500

status = "sucesso" if saldo >= saque else "Falha"
print(f'{status} ao realizar o saque!')

print("\n")


####    ####

## Estruturas de Repetição

texto = "Jesus Cristo"
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
print("\n")  #Add quebra de linha

for numero in range(0,100,3):
    print(numero, end="; ")

print("\n")

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print('Exibindo o extrato')

nome = 'jEsUs'

print(nome.upper())
print(nome.lower())
print(nome.title())

print(" ")

curso = "   Python  "
print(curso.strip())
print(curso.strip()+ ".")
print(curso.lstrip())
print(curso.rstrip())

print(" ")

nome = "Jesus"
print(nome.center(10,"#"))
print(".".join(nome))

print("####    #####")
print(" ")

nome = "Victor"
idade = 24
profissao = "Programador"
linguagem = "Python"

print(f'Olá, me chamo %s. Eu tenho %d anos de idade, sou %s e estou matriculado no curso de %s.' %(nome, idade, profissao, linguagem))
print('Olá, me chamo {}. Eu tenho {} anos de idade, sou {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))


print(" ")
print("####    #####")
print(" ")


PI = 3.14159
print(f"Valor de Pi é: {PI:.2f}")
print(f"Valor de Pi é: {PI:10.2f}")

print(" ")
print("####    #####")
print(" ")

nome = "Jesus Cristo"
print(nome[0])
print(nome[:7])
print(nome[2:7])
print(nome[0:10:2])
print(nome[:])
print(nome[::-1])


print(" ")
print("####    #####")
print(" ")


nome = 'Victor Harduim'
mensagem = f"""
    Olá, meu nome é {nome},
Eu estou aprendendo Pyhton.
        Essa msg tem diferentes recuos;
"""

print(mensagem)
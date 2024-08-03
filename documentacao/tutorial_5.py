# estrutura de dados

# listas
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y"]

# append
# adiciona um item no final
# equivalente: a[len(a):] = [x]
lista_exemplo.append("z")
print(lista_exemplo)

# extend
# adiciona varios itens no final
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y"]
lista_exemplo.extend(["z", 30])
print(lista_exemplo)

# insert
# adiciona um item especificando seu indice e seu valor
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y"]
lista_exemplo.insert(0, "teste") #simula o popleft
print(lista_exemplo)

# remove
# remove o primeiro item encontrado na lista
# se não existir, retorna uma exceção ValueError
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y", 1]
lista_exemplo.remove("x")
print(lista_exemplo)

# pop
# remove um item pelo indice e o retorna
# se nenhum indic for passado
# remove do final
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y", 1]
item_removido = lista_exemplo.pop()
print(item_removido)

# clear
# remove todos os itens da lista
# equivalente a: del lista[:]
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y", 1]
lista_exemplo.clear()
print(lista_exemplo)

# index
# devolve o indice do item especificado
# (item, inicio, fim)
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y", 1]
print(lista_exemplo.index(10, 0, 7))

# count
# devolve o numero de vezes que o item aparece na lista
lista_exemplo = [1, 2, 3, "a", "b", "c", 10, "x", 20, "y", 1]
print(lista_exemplo.count(1))

# sort
# ordena a lista
# de forma crescente por padrão
lista_exemplo = [1, 2, 3, 10, 20, 1, 4, 9]
lista_exemplo.sort() #reverse=True -> descrescente
print(lista_exemplo)

# copy
# retorna uma cópia rasa da lista
# equivale a copia = lista[:]
lista_exemplo = [1, 2, 3, 10, 20, 1, 4, 9]
copia = lista_exemplo.copy()
print(copia)
copia.append("nao é referencia")
print(copia)
print(lista_exemplo)


# lista como pilha
# ultimo a entrar é o primeiro a sair
# adicionar no final -> append()
# remover do final -> pop()
pilha = [1, 2, 3]
pilha.append(4)
pilha.pop()
print(pilha)

# listas como fila
# primeiro a entrar é o primeiro a sair
# fazer inserts ou pops no inicio na lista é lento pois todos os outros elementos terão que ser deslocados
# use collections.deque para ter appends e pops eficientes nas duas extremidades
from collections import deque
fila = deque(['gui', 'ana', 'vic', 'jhon'])
fila.append('emily')
fila.popleft() #remove o primeiro
print(fila)

# list comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
print(x) #valor ainda existe apos final do laço

# mesma coisa
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# outra alternativa
squares = [x**2 for x in range(10)]
print(squares)

# Um compreensão de lista consiste de um par de colchetes contendo uma expressão seguida de uma cláusula for, e então zero ou mais cláusulas for ou if. O resultado será uma nova lista resultante da avaliação da expressão no contexto das cláusulas for e if
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# É a mesma coisa que:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

lista_exemplo = [-8, -4, 0, 4, 8]
#list comprehensions
lista_dobro = [x*2 for x in lista_exemplo]
print(lista_dobro)

# podemos fazer todas expressões com list comprehension
# filtra os valores positivos
lista_exemplo = [-8, -4, 0, 4, 8]
positivo = [x for x in lista_exemplo if x > 0]
print(positivo)

from math import pi
casas_decimais = [str(round(pi, i)) for i in range(1,6)]
print(casas_decimais)

# round arredonda para o numero de casas decimais especificada
print(round(1.5851, 2))

# list comprehension com listas aninhadas
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print([[row[i] for row in matrix] for i in range(4)])

# mesma coisa que:
transpor = []
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
# aqui itera nas linhas
for i in range(4):
    # aqui itera nas listas
    transpor.append(row[i] for row in matrix)
print(transpor)

# outro exemplo
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
transpor = []
for i in range(4):
    linha_transposta = []
    for row in matrix:
        #pega a primeira linha da matrix eadiciona o primeiro elemento na linha_transposta
        linha_transposta.append(row[i])
    # adiciona a linha transposta no resultado final
    transpor.append(linha_transposta)


# instrução del
# remove um elemento de uma lista passando seu índice
lista_exemplo = [10,20,30]
del lista_exemplo[0]
print(lista_exemplo)
del lista_exemplo[0:-1] #retorna o ultimo elemento
print(lista_exemplo)
del lista_exemplo
print(lista_exemplo)


# tuplas
# assim como listas e range, as tuplas são tipos de sequencia
# tupla é uma sequencia de valores separados por vírgula
t = 12345, 54321, 'Ola!'
print(t)

#podem ser aninhadas
u = t, (10, 20, 30)
print(u)

# tuplas são imutáveis
u[0] = 101010

# mas podem conter objetos mutáveis
v = ([1,2,3,4,5], [5,4,3,2,1])
v[0][0] = 0
print(v)

# diferente das listas, as tuplas são imutáveis e geralmente seus valores são heterogêneos (tipos diferentes)

tupla_unitaria = 'ola', #precisa ter a virgula
print(tupla_unitaria)

# desempacotamento de tupla
t = 12345, 54321, 'Ola!'
x, y, z = t
print(x, y, z)

# conjuntos
# é uma coleção desordenada de elementos sem repetição
# suporta operações matemáticas
frutas = {'pera', 'uva', 'mamao', 'pera', 'uva', 'banana'}
print(frutas)

# vai me retornar um erro
# python não consegue associar um indice a um valor
# pois os conjuntos são desordenados
print(frutas[0])

# criar conjunto vazia
vazio = set()

#conjuntos também suportam list comprehesions
a = set('abracadabra')
b = set('alacazam')
teste ={x for x in a if x not in 'abc'}
print(teste)

# dicionários
# conjunto não ordenado de pares chave-valor, onde chaves são únicas em casa instancia
# tipo é: dict -> mapeamento
# são indexados por chaves, que podem ser de qualquer tipo imutável

# exemplos
tel = {'gui':1010, 'ana':2020, 'jhon':3030}
print(tel)
tel["jhon"] = 4040
print(tel)
del tel["jhon"]
print(tel)
print(list(tel))
print(sorted(tel))
print('gui' in tel)

# dict -> transforma me dicionario
dicionario = dict([('gui', 1010), ('ana', 2020), ('jhon', 3030)])
print(dicionario)

print({x : x**2 for x in (2,4,6)})

dicionario = dict(gui='1010', ana=2020, jhon=3030)
print(dicionario)


# tecnicas de iteração
# items()
# retorna a chave e o valor
cadastro = {'gui':22, 'ana':13, 'jhon':62}
for nome, idade in cadastro.items():
    print(nome, idade)
    

# enumerate()
# retorna indice e valor da lista
for i, v in enumerate([10,20,30,40]):
    print(i, v)

# zip
# permite percorrer duas listas
lista1 = [10,20,30]
lista2 = [100,200,300]

for q, a in zip(lista1, lista2):
    print('texto qualquer{0} outro{1}'.format(q, a))

# reversed
# percorre sequencia em ordem inversa
for i in reversed(range(1, 10, 1)):
    print(i)

# sorted
# ordena os itens de forma crescente
lista2 = [500,600,100,200,300,2,1,9,502]
for i in sorted(lista2):
    print(i)

# set() + sorted
# itera nos elementos sem duplicidade e ordenados
lista2 = [1,500,600,100,200,300,2,1,9,502,1,500,100]
for i in sorted(set(lista2)):
    print(i)

# sempre criar uma nova lista, não alterar a lista original
import math
linha = [56.5, float('NaN'), 51.7, 59.8,float('NaN'), 47.8]
dado_filtrado = []
for valor in linha:
    if not math.isnan(valor):
        dado_filtrado.append(valor)
print(dado_filtrado)


# mais sobre condições
# while e for pode conter quaisuqer operadores
# não apenas de comparação
# curto circuito:
a = True
b = 0 # False
c = True

# vai haver o curto circuito e retornara o valor 0
curto_circuito = a and b and c
print(curto_circuito)


# Comparação de sequencias
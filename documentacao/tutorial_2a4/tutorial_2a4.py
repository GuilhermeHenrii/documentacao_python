# divisão fracionaria
# // divisão inteira
teste = 10 / 3
print(teste)

# escapa as aspas
teste = 'doesn\'t'
print(teste)

# usando dois tipos de aspas
teste = '"fefafaf"'
print(teste)

# concatena string sozinho
teste = 'py' 'thon'
print(teste)

# [x:y] fatiador de string
# primeiro argumento sempre entre e ultimo nunca entra
word = 'Python'
teste = 'J' + word[1:]
teste1 = word[:2] + 'py'
print(teste1)


# Referencia
lista_cor = ["amarelo", "verde"]
lista_cor_2 = lista_cor

lista_cor.append("preto")
print(lista_cor_2)


# Cópia
lista_cor = ["amarelo", "verde"]
lista_cor_2 = lista_cor[:]

lista_cor.append("preto")
print(lista_cor_2)
print(lista_cor)

# len
print(len(lista_cor))

# 0 == False
# > 0 == True
teste = 0 == False
print(teste)

# if
x = 41
if x == 41:
    print("Tudo certo")
elif x == 40:
    print("Deu erro")
elif x == 42:
    print("Deu erro")


# for
words = ["gato", "cachorro", "lebre"]
for w in words:
    print(w, len(w))

# não se deve deletar um item de uma coleção diretamente
# cria copia
status_users = {'Hans':'active', 'Guilherme':'active', 'Joao':'inactive'}
for users, status in status_users.copy().items():
    if status == 'inactive':
        del status_users[users]
print(status_users)

# cria nova coleção apenas com ativos
# não mexer na coleção original
active_users = {}
for user, status in status_users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# range
# itera sobre sequencias de numeros
for i in range(5):
    print(i)

# de 5 a 50 pulando de 10 em 10
for i in range(5, 50, 10):
    print(i)

# itera sobre a lista pegando seus respectivos indices e valores
# nessa situação é mais conveniente usar o enumerate()
lista = ['teste', 'joao', 'maria', 'guilherme', 'ana']
for i in range(len(lista)):
    print(i, lista[i])

# range não retorna uma lista
print(range(10))

# # 0 + 1 + 2 + 3 + 4
print(sum(range(5)))

# break 
# else usado no for é excutada quando não acha um break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue
for num in range(2, 10):
    if num % 2 == 0:
        print('numero par', num)
        continue
    print('numero impar', num)

# pass
# comando pass não faz nada
#  Pode ser usada quando a sintaxe exige um comando mas a semântica do programa não requer nenhuma ação
while True:
    pass
    break

# match
# parecido com o switch case do js
# com mais funcionalidades
def http_response(status):
    match status:
        case 200 | 204 | 205:
            return "Ok"
        case 201:
            return "Criado"
        case 203:
            return "Não autorizado"
        case 400:
            return "Requisição inválida"
        case 401:
            return "Não autorizada"
        case 500:
            return "Erro interno de servidor"
        # _ atua como um coringa e sempre sera correspondido se nenhum outro valor for 
        case _:
            return "Algo de errado com a internet"

print(http_response(205))

# point é uma tupla (x, y)
match point:
    case (0, 0): #se for 0 as dois,esta na origem
        print("Origin")
    case (0, y): #se x for 0 pega y
        print(f"Y={y}")
    case (x, 0): #se y for 0 pega x
        print(f"X={x}")
    case (x, y): #onceitualmente semelhante à atribuição de desempacotamento (x, y) = point
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# maneiras de chamar a classe
var = 10
Point(1, var)
Point(1, y=var)
Point(x = 1, y=var)
Point(y=var, x=1)

# funções
def teste():
    # a primeira linha pode ser uma docstring
    # boa prática
    print("Essa funcao apenas printa algo")
teste()

def teste():
    # aqui é criado um tabela de simbolos local
    variavel = 10
    outra = 10
    nome = "Gui"
    return str(variavel + outra) + nome

    # referências a variáveis são buscadas primeiro na tabela de símbolos local, em seguida na tabela de símbolos locais de funções delimitadoras ou circundantes, depois na tabela de símbolos global e, finalmente, na tabela de nomes da própria linguagem. Embora possam ser referenciadas, variáveis globais e de funções externas não podem ter atribuições (a menos que seja utilizado o comando global, para variáveis globais, ou nonlocal, para variáveis de funções externas).

    # Os parâmetros reais (argumentos) de uma chamada de função são introduzidos na tabela de símbolos local da função no momento da chamada

# Uma definição de função associa o nome da função com o objeto função na tabela de símbolos atual. O interpretador reconhece o objeto apontado pelo nome como uma função definida pelo usuário. Outros nomes também podem apontar para o mesmo objeto função e também pode ser usados pra acessar a função:
print(teste())
teste2 = teste
print(teste2())

# Função fibonacci
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib(100))

# posso passar um valor padrão para o argumento
# ou não passar e deixa-lo obrigatório
def func_varios_args(arg1, arg2, arg3=10):
    arg1 = 10,
    arg2 = 20,
    teste = arg1 + arg2
    return teste
print(func_varios_args(1, 1))

# avalia o escopo da função quando ela é criada
i = 5
def f(arg=i):
    print(arg)

i = 6
f() # retorna 5

# a lista não é sobrescrevida
# quando chamamos a função várias vezes
def f(a, l=[]):
    l.append(a)
    return l
print(f(1)) #[1]
print(f(2)) #[1, 2]
print(f(3)) #[1, 2, 3]

# aqui a l é por padrão None
# com isso sempre sera criada uma nova lista
def f(a, l=None):
    if l is None:
        l = []    
    l.append(a)
    return l
print(f(1)) #[1]
print(f(2)) #[1, 2]
print(f(3)) #[1, 2, 3]

# argumento nomeado deve sempre vir após o posicional
# * -> antes do * são os parametros somente nomeado
# / -> antes da / são os parametros somente-posicionais
def argumento_nomeado(voltage, state ='seila', action='voom', type='sein'):
    print("-- essa funcao de teste esta: ", action, end=' '),
    print("\n a voltagem e de: ", voltage)
    print("o tipo e: ", type)
    print("o estado esta: ", state, "!")

print(argumento_nomeado(voltage=1000, action="agindo"))

# Use somente-posicional se você não quer que o nome do parâmetro esteja disponível para o usuário. Isso é útil quando nomes de parâmetros não tem um significado real, se você quer forçar a ordem dos argumentos da função quando ela é chamada ou se você precisa ter alguns parâmetros posicionais e alguns nomeados.

# Use somente-nomeado quando os nomes tem significado e a definição da função fica mais clara deixando esses nomes explícitos ou se você quer evitar que usuários confiem na posição dos argumentos que estão sendo passados.

# Para uma API, use somente-posicional para evitar quebras na mudança da API se os nomes dos parâmetros forem alterados no futuro..


# desempacotando listas de argumentos
print(list(range(3,6))) #3, 4, 5
args = [3, 8]
print(list(range(*args))) # aqui ele irá "explodir" a lista args e obtera os valores de 3 a 8 sem incluir o 8


# empressão lambda
def incrementor(n):
    return lambda x: x + n

f = incrementor(42)
print(f(1))


# Strings de documentação
# Aqui estão algumas convenções sobre o conteúdo e formatação de strings de documentação, também conhecidas como docstrings.

# A primeira linha deve sempre ser curta, um resumo conciso do propósito do objeto. Por brevidade, não deve explicitamente se referir ao nome ou tipo do objeto, uma vez que estas informações estão disponíveis por outros meios (exceto se o nome da função for o próprio verbo que descreve a finalidade da função). Essa linha deve começar com letra maiúscula e terminar com ponto.

# Se existem mais linhas na string de documentação, a segunda linha deve estar em branco, separando visualmente o resumo do resto da descrição. As linhas seguintes devem conter um ou mais parágrafos descrevendo as convenções de chamada ao objeto, seus efeitos colaterais, etc.


# Estilo de codificação (pep 8):

# Use indentação com 4 espaços, e não use tabulações.
# 4 espaços são um bom meio termo entre indentação estreita (permite maior profundidade de aninhamento) e indentação larga (mais fácil de ler). Tabulações trazem complicações, e o melhor é não usar.

# Quebre as linhas de modo que não excedam 79 caracteres.
# Isso ajuda os usuários com telas pequenas e torna possível abrir vários arquivos de código lado a lado em telas maiores.

# Deixe linhas em branco para separar funções e classes, e blocos de código dentro de funções.

# Quando possível, coloque comentários em uma linha própria.

# Escreva strings de documentação.

# Use espaços ao redor de operadores e após vírgulas, mas não diretamente dentro de parênteses, colchetes e chaves: a = f(1, 2) + g(3, 4).

# Nomeie suas classes e funções de forma consistente; a convenção é usar MaiusculoCamelCase para classes e minusculo_com_sublinhado para funções e métodos. Sempre use self como o nome para o primeiro argumento dos métodos (veja Uma primeira olhada nas classes para mais informações sobre classes e métodos).

# Não use codificações exóticas se o seu código é feito para ser usado em um contexto internacional. O padrão do Python, UTF-8, ou mesmo ASCII puro funciona bem em qualquer caso.

# Da mesma forma, não use caracteres não-ASCII em identificadores se houver apenas a menor chance de pessoas falando um idioma diferente ler ou manter o código.
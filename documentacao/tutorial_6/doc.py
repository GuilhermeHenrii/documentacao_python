# importa todo o módulo
import fibo

# acessando a função definida no módulo
fibo.fib(100)

# atribuindo a função importada a uma variavel local
fib = fibo.fib
fib(100)

# printa o nome do módulo
print(fibo.__name__)


# Cada módulo tem seu próprio espaço de nomes privado, que é usado como espaço de nomes global para todas as funções definidas no módulo. Assim, o autor de um módulo pode usar variáveis globais no seu módulo sem se preocupar com conflitos acidentais com as variáveis globais do usuário.

# fib já esta definido na importação
# porem fibo não
from fibo import fib

# importa todos os nomes definidos no módulo
from fibo import *

# adiciona um apelido no modulo
import fibo as fib
fib.fib(100)

# tambem pode ser:
from fibo import fib as fibonacci
fibonacci(100)

# sempre que alterar um módulo que esta sendo usado em outro arquivo, deve-se reiniciar o interpretador para que ele pegue as altereções

# executar um módulo como script
#python fibo.py
import fibo
fibo.py

# quando chamamos um módulo de nome spam, por exemplo, primeiro o pyhton busca um módulo embutido (sys.builtin_module_names) com esse nome primeiro para depois buscar em uma lista de diretorios.

# o python guarda versões compiladas de cada módulo no diretório __pychache__

#função dir é usada para descobrir quais nomes são definidos por um módulo. Ela devolve uma lista ordenada de strings.
import fibo
print(dir(fibo))
print(dir())

# dir() não lista os nomes de variáveis e funções embutidas. Esta lista está disponível no módulo padrão builtins:
import builtins
print(dir(builtins))


# pacotes: são formas de armazenar diversos modulos de um contexto igual. Por exemplo se tivermos modulos de som, com seus formatos, efeitos, e filtros. Podemos criar um pocote chamando som, que tenha um submodulos chamado efeito e dentro desse submodulos, os modulos relacionados ao efeito, como echo, reerse, etc. Mesma coisa para os outros submodulos de formato e filtro. Como se fosse algo relacionado a criar um pacote com varias hierarquis de modulos dentro.

# sempre evitar o uso do * para importar tudo de um modulo. recomendado é especificar o módulo desejado.

# se tivermos pacotes com subpacotes, podemos usar a sintaxe de importação absoluta para se referir aos submodulos dos pacotes irmaos

from . import fibo
from .. import modulo_irmao_do_mesmo_pacote

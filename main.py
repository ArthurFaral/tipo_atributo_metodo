## Contexto principal de execução do projeto

from classe_tipos_metodos import livro
from modulo_classe_carros import carros
from atributos_publicos_privados import cadastrouser
from abstracao_encapsulamento import pessoa
from classes_getter_setters import VendaProdutos

## Instanciar os objetos da casse carros

carro1 = carros("CLS","Mercedes")

carro2 = carros("M5","Bmw")


#Mostrar o valor ds objetos

print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)

print(carro2.marca)
print(carro2.modelo)
print(carro2.cor)


# Jeito correto de exibir o atributo de classe é exibindo a classe
# e não o objeto
print(carros.cor)


## Detalhando os valores da classe com metodo __dict__
print(carros.__dict__)


## Detalhando os valores de uma instancia/objeto com metodo __dict__
print(carro1.__dict__)



## Instanciar objetos da classe "cadastrouser"

user1 = cadastrouser("Arthur",123456)

user2 = cadastrouser("Theo",654321)

print(user1.usuario)
#print(user1.__senha)


## Acessando os valores de um atributo privado com a função dir
# A função dir retorna todas a propriedades e metodos de um objeto



print(dir(user1))


## Exibir atributos ocultos atraves de  "name mangling" "naming mangling"
print(user1._cadastrouser__senha)


## Apagando um atributo de um usuario

del user1.usuario

print(user1.__dict__)


## Criando instancias da Classe Pessoa

p1 = pessoa("Arthur","Faral",1111111111,2003)

## Exibir atributos publicos

print(p1.nome)
print(p1.sobrenome)

# Exibindo atributo protegido
print(p1._anonascido)

# Exibindo o metodo da classe
p1.idade(2003)


## Exibir atributos privados com Naming Mangling

#print(p1.__cpf)

print(p1._pessoa__cpf)

#######################################################



#instanciando objetos da classe VendaProdutos


produto1 = VendaProdutos("Arroz", 23, 10.50)


#print(produto1.__produto)

#Exibindo o valor da instancia atraves do metodo getter


print(produto1.produto)


#mostrando a quantidade atraves do Getter pois 
#deixou acessivel

print(produto1.quantidade)

# Uttilizando o setter para mudar o valor de quantidade 
# em tempo de execução sem recriar o objeto

produto1.quantidade = 50

print(f"Nova quantidade {produto1.quantidade}")



print(produto1.valor_total_compras)


###############################################################


# Trabalhando com métodos de Classe

livro1 = livro("O Pescador","José Cunha",1998)
livro1.imprime()
livro1.anopublicacao()


## Executando métodos de classe

livro2 = livro.calculoanopublicacao("REceita de Feijoada",2009)


print(livro2)

## Chamando o método oculto

print(livro1._livro__autor()) # Apliquei naming mangling



## staticmethod

print(livro1.geraisbn())


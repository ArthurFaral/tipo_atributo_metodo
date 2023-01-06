## Atributos Privados 2 underlines __
## Atributos Protegidos 1 underline _


## Atributos protegidos são atributos que são acessiveis a classe que foi
# instanciado o objeto. Porém será inacesivel para classes filhas
# ou classes que queiram herdar atributos e metodos da classe pai


## Classe de Exemplo para privado, publico e protegido

# Publico = self.nome = nome (Abstraidos)
# Privado = self.__nome = nome (Encapsulados)
# Protegido = self._nome = nome

import datetime

class pessoa:
    anoatual = datetime.date.today().year
    def __init__(self,nome,sobrenome,cpf,anonascido):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf
        self._anonascido = anonascido


    @classmethod # Metodo classe (não tem o self)
    def idade(anoatual,_anonascido):
        calculoidade = anoatual.anoatual - _anonascido
        print(f"Idade é: {calculoidade}")
#Exercícios com strings e conversões de bibliotécas

biblioteca_a={'Quantos Espaços em branco existem na frase.'}
biblioteca_b={'Quantas vezes aparecem as vogais A, E, I, O, U.'}

def conversores_str(bibliotecas):
    bibliotecas=str(bibliotecas)
    return bibliotecas

def conta_vogais(string):
    string=string.lower()
    vogais='aeiou'
    return {i:string.count(i) for i in vogais if i in string}

def conta_vogais_total(strings):
    strings=strings.lower()
    vogais='aeiou'
    return sum(strings.count(et) for et in vogais)

def conta_espacos(espaco):
    espaco=espaco
    espacos_brancos=' '
    return {e:espaco.count(' ') for e in espacos_brancos if e in espaco}

print(40*'-')
print(conta_vogais(conversores_str(biblioteca_b)))
print(40*'-')
print(conta_vogais_total(conversores_str(biblioteca_b)))
print(40*'-')
print(conta_espacos(conversores_str(biblioteca_a)))
print(40*'-')
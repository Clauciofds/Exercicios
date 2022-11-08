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
print(conta_vogais('quantas vezes aparecem as vogais a, e, i, o, u.'))
print(40*'-')
print(conta_vogais_total('quantas vezes aparecem as vogais a, e, i, o, u.'))
print(40*'-')
print(conta_espacos('quantos espaços em branco existem na frase.'))
print(40*'-')
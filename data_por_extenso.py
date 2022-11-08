print(30*'-')
print('>>>DATA DO SEU ANIVERSÁRIO<<<')
print(30*'-')
print('\n')
dia_aniver=input('Que dia nasceu: ')
mes_aniver=input('Que mês nasceu: ')
ano_aniver=input('Que ano nasceu: ')
#print(type(mes_aniver))
if mes_aniver<'10':
       mes_aniver=mes_aniver.replace('0','')
#print(mes_aniver)

meses={'1':'Janeiro',
       '2':'Fevereiro',
       '3':'Marco',
       '4':'Abril',
       '5':'Maio',
       '6':'Junho',
       '7':'Julho',
       '8':'Agosto',
       '9':'Setembro',
       '10':'Outubro',
       '11':'Novembro',
       '12':'Dezembro'}
#print(type(meses))
print('\n')
data_extenso=f'Você nasceu em {str(dia_aniver)} de {meses[str(mes_aniver)]} de {str(ano_aniver)}.'
print(data_extenso)
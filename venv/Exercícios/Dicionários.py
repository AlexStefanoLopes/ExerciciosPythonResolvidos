coleta = {'Aedes aegypt': 32, ' Aedes albopictus': 22, 'Anófeles': 14}
coleta['Aedes aegypt']
print('coleta')

coleta2 = {'Anopheles gambise': 11, 'Oi': 60, 'tchau': 10}
coleta.update(coleta2)
print(coleta)

>>> coleta.update(coleta2)
>> > print(coleta)
{'Aedes aegypt': 32, ' Aedes albopictus': 22, 'Anófeles': 14, 'Anopheles gambise': 11, 'Oi': 60, 'tchau': 10}
>> > coleta.items()
dict_items([('Aedes aegypt', 32), (' Aedes albopictus', 22), ('Anófeles', 14), ('Anopheles gambise', 11), ('Oi', 60),
            ('tchau', 10)])
>> > for especie, num_especimes in coleta.items():
    print(f'Espécie: {especie}, numero de espécimes coletados: {num_especimes}')

Espécie: Aedes aegypt, numero de espécimes
coletados: 32
Espécie: Aedes
albopictus, numero
de
espécimes
coletados: 22
Espécie: Anófeles, numero
de
espécimes
coletados: 14
Espécie: Anopheles
gambise, numero
de
espécimes
coletados: 11
Espécie: Oi, numero
de
espécimes
coletados: 60
Espécie: tchau, numero
de
espécimes
coletados: 10
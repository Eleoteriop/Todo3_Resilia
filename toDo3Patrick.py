# SEGUNDO O ENUNCIADO A NOTA DO CANDIDATO SERIA NO FORMATO 'eX_tX_pX_sX',
# "o codigo precisa funcionar para qualquer lista que seja inserida nesse formato"
# ENTAO PODERA SER INSERIDA UMA LISTA, CRIEI UMA LISTA HIPOTETICA QUE SERIA
# RECEBIDA E TAMBEM PERMITI QUE SEJA INSERIDO RESULTADO DE CANDIDATOS.
# A IDEIA PRINCIPAL É FILTRAR OS CANDIDATOS COM BASE NA NOTA DE CORTE INSERIDA PELO USUARIO.


dict = {}
index = 0
filtrados = []
# cria uma lista de strings de 0 a 10
validador = list(range(0,10+1))
validador = list(map(lambda x : str(x), validador))

#Funçao que valida os inputs recebidos pelo usuario
def valid(inputado):
    if inputado not in validador:
        while inputado not in validador:
            try:
                inputado = input('Precisa ser uma nota de 0 a 10. Insira: ')
            except:
                print('Precisa ser uma nota de 0 a 10. Insira:')
    else:
        inputado = int(inputado)
    return int(inputado)

#loop de input do usuario
while index < 1:
    insercao = input('Digite "sim" ou "nao" caso deseje inserir novos resultados a lista: ')
    if insercao.strip().lower()=='sim':
        candidato = input('nome completo do candidato: ').replace(' ','_')
        entrevista = valid(input('nota da entrevista: '))
        teorico = valid(input('nota da teorico: '))
        pratico = valid(input('nota da pratico: '))
        softskill = valid(input('nota de softskill: '))
        dict[f'{candidato}'] =  f'e{entrevista}_t{teorico}_p{pratico}_s{softskill}'
    else:
        print(f'*'*30)
        print("POR FAVOR INSIRA AS NOTAS DE CORTE PARA CADA FASE DO PROCESSO SELETIVO PARA FILTRAR O CANDIDATOS")
        entrevista_filtro = valid(input('nota de corte da entrevista: '))
        teorico_filtro = valid(input('nota de corte da teorico: '))
        pratico_filtro = valid(input('nota de corte da pratico: '))
        softskill_filtro = valid(input('nota de corte de softskill: '))
        break

#Hipotetica lista recebida
lista_recebida = [["Pedro_Manuel", 'e8_t7_p6_s6'], ['Alfredo_Maxuel','e5_t4_p8_s10'],
                ['Suellen_Souza','e8_t5_p4_s9'], ['Jorjada_Silva','e6_t8_p8_s10'],
                ['Gabriel_Pedro','e10_t10_p8_s9'], ["João_Porto", 'e4_t9_p3_s10'],
                ['Eduarda_Bottas','e7_t6_p8_s10'], ['Brenda_Rosa','e9_t8_p7_s5'],
                ['Rodrigo_Alves','e1_t10_p10_s2'], ['Felipe_Castilho','e4_t3_p7_s5'],
                ['Barbara_Almeida','e2_t2_p2_s1'], ['Italo_Ferreira','e2_t8_p7_s9'],
                ['Robertha_Marques','e9_t6_p5_s10'], ['Caroline_Marques','e5_t7_p6_s2']]



for dicionario in lista_recebida:
    dict[dicionario[0]] = dicionario[1]


# Logica do filtro
for k, v in dict.items():
    aprovado = 0
    notas = v.split('_')
    nota_entrevista = int(notas[0][1:])
    nota_teorico = int(notas[1][1:])
    nota_pratico = int(notas[2][1:])
    nota_softskill = int(notas[3][1:])
    if entrevista_filtro <= nota_entrevista:
        aprovado+=1
    if teorico_filtro <= nota_teorico:
        aprovado+=1
    if pratico_filtro <= nota_pratico:
        aprovado+=1
    if softskill_filtro <= nota_softskill:
        aprovado+=1
    if aprovado==4:
        filtrados.append(k)

if filtrados==None:
    print('Infelizmente nenhum candidato se encaixa nos parametros inseridos')
else:
    print('CANDIDATOS QUE SE ENCAIXAM NOS PARAMETROS')
    print('******************************************')
    for x in filtrados:
        print(x)


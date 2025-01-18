print('Seja bem vindo a calculadora CLT vs PJ')
print('''
        Um dos dilemas encontrados na internet é a sobre o quanto compensa optar pelo regime 
      de trabalho da CLT ou da Pessoa Jurídica. 
      
        Há algumas coisas que devem ser levadas em consideração ao se pensar nisso. Para mim,
      a mais importante é saber se o valor anual da remuneração como PJ ultrabapassará o limite 
      permitido para um MEI. É muito importante ter isso na ponta do lápis, pois a simples 
      mudança no regime de tributação pode alterar o vaor de, aproximadamente, R$ 75,00 para 
      R$ 1.000,00 em tributos.
      ''')


salario = int(input('Qual o seu salário bruto? '))
valeTransporte = int(input('Você possui Vale Transporte? Se sim, qual o valor mensal? Caso contrário, atribuir 0. '))
valeRefeicao = int(input('Você possui Vale Refeição? Se sim, qual o valor mensal? Caso contrário, atribuir 0. '))
valeAlimentacao = int(input('Você possui Vale Alimentação? Se sim, qual o valor mensal? Caso contrário, atribuir 0. '))
planoMedico = int(input('A empresa custeia seu Plano Médico? Se sim, qual o valor mensal? Caso contrário, atribuir 0. '))

fgts = salario * 0.08
ferias = (salario / 12)  * 1.34
decimoTerceiro = salario * 0.08
inss = salario * 0.08
seguroDesemprego = salario / 6 ## como a regra é de que entre 12 e 23 meses recebemos 4 parcelas, considera-se que a cada 6 meses há um mês de salário guardado

calculo = salario + valeRefeicao + valeTransporte + valeAlimentacao + planoMedico + fgts + ferias + decimoTerceiro + inss + seguroDesemprego

print(f'''
      Sua remuneração como Pessoa Jurídica tem que ser, no mínimo, igual a R$ {calculo*1.12}.

      Este cálculo é composto pelo Salário fornecido de R$ {salario}, somando a ele, o Vale Refeição de R$ {valeRefeicao}, o Vale Alimentação de R$ {valeAlimentacao}, o Vale Transporte de R$ {valeTransporte}, o Plano Médico de R$ {planoMedico}, além das previsões trabalhistas, sendo elas: FGTS R$ {fgts}, Férias R$ {ferias}, o Décimo Terceiro salário R$ {decimoTerceiro}, o INSS R$ {inss} e uma provisão para o Seguro Desemprego de R$ {seguroDesemprego}. Ainda, há uma alíquota para os tributos mensais.

      Desta forma, se o valor ofertado mensalmente, for inferior que a somatório dos seus atuais valores mensais acima caldulado, não é fevorável a alteração para o regime de Pessoa Jurídica.''')

print('Seja bem vindo a calculadora CLT vs PJ')
print('''Um dos dilemas mais comuns na internet é decidir entre o regime de trabalho da CLT ou atuar como Pessoa Jurídica (PJ).

Há diversos fatores a serem considerados nessa escolha, e, para mim, o mais importante é verificar se a remuneração anual como PJ ultrapassará o limite permitido para um MEI. Essa análise é essencial, pois uma simples mudança no regime de tributação pode fazer com que os tributos passem de aproximadamente R$ 75,00 para cerca de R$ 1.000,00. Portanto, é fundamental colocar tudo na ponta do lápis antes de tomar essa decisão.''')


salario = int(input('Qual o seu salário bruto? '))

valeTransporte = input('Você possui Vale Transporte? (y/n) ')
if valeTransporte == 'y':
  valorVT = int(input('Qual o valor mensal? '))
else:
  valorVT = 0

valeRefeicao = input('Você possui Vale Refeição? (y/n) ')
if valeRefeicao == 'y':
  valorVR = int(input('Qual o valor mensal? '))
else:
  valorVR = 0

valeAlimentacao = input('Você possui Vale Alimentação? (y/n) ')
if valeAlimentacao == 'y':
  valorVA = int(input('Qual o valor mensal? '))
else:
  valorVA = 0

planoMedico = input('A empresa custeia seu Plano Médico? (y/n) ')
if planoMedico == 'y':
  valorPM = int(input('Qual o valor mensal? '))
else:
  valorPM = 0

fgts = round(salario * 0.08,2)
inss = round(salario * 0.08,2)
decimoTerceiro = round(salario /12 ,2)
ferias = round((salario / 12)  * 1.34,2)
seguroDesemprego = round((2424.11 * 5) / 24,2)

calculo = salario + valorVT + valorVA + valorVR + valorPM + fgts + ferias + decimoTerceiro + inss + seguroDesemprego

print(f'''Sua remuneração como Pessoa Jurídica deve ser, no mínimo, R$ {round(calculo*1.12,2)}.

Esse cálculo considera o salário oferecido de R$ {salario}, acrescido dos seguintes benefícios: Vale Refeição (R$ {valorVR}), Vale Alimentação (R$ {valorVA}), Vale Transporte (R$ {valorVT}) e Plano Médico (R$ {valorPM}). Além disso, inclui as previsões trabalhistas, como FGTS (R$ {fgts}), Férias (R$ {ferias}), Décimo Terceiro Salário (R$ {decimoTerceiro}), INSS (R$ {inss}) e uma provisão para Seguro-Desemprego (R$ {seguroDesemprego}). Também é necessário considerar a alíquota dos tributos mensais.

Portanto, se o valor oferecido mensalmente for inferior à soma dos seus ganhos atuais calculados acima, a migração para o regime de Pessoa Jurídica não é vantajosa.''')

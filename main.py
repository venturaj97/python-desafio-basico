#Mini desafio: Calcular quantos dias duraria um produto se a pessoa usar X porções por dia


total_porcao = int(input('Digite quantas porções no total tem o produto? '))
dia_porcao = int(input('Digite quantas porções são consumidas no dia? '))

calculo_duracao = total_porcao / dia_porcao

print(f'O produto vai durar {calculo_duracao:.0f} dias!')
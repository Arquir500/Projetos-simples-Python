maior = 0
menor = 0
for c in range(1, 7):
    peso = float(input(f'Dígite o peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}Kg.')
print(f'O menor peso foi de {menor}Kg.')

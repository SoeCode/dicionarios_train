#Trabalho simples para análise de vendas e metas usando listas e percorrendo listas utilizando FOR.

#Análise de Vendas

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alison', 7870],
    ['Soepaza', 12000],
    ['Nicolas', 13000],
    ['Suzi', 8300],
]
for venda in vendas:
    if venda[1] <= meta:
        print(f'{venda[0]} Vendeu um total de R${venda[1]:.2f}. Valor restante para alcançar meta: R${meta-venda[1]:.2f}')
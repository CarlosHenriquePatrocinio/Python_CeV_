def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res
def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res    
def dobro(preco):
    res = preco * 2
    return res   
def metade(preco):
    res = preco / 2
    return res 
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de R${p} é R${dobro(p)}')
print(f'Aumentando 10%, temos R${aumentar(p, 10)}')

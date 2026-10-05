def calcular_desconto(valor_compra, tipo_cliente):
    if valor_compra < 100:
        desconto = 0
    elif valor_compra < 500:
        desconto = 0.10
    else:
        desconto = 0.20

    if tipo_cliente.upper() == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    if valor_desconto > 200:
        valor_desconto = 200

    return round(valor_desconto, 2)
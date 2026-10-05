from desconto import calcular_desconto


def test_menor_que_100():
    assert calcular_desconto(99.99, "COMUM") == 0


def test_exatamente_100():
    assert calcular_desconto(100, "COMUM") == 10


def test_entre_100_e_499():
    assert calcular_desconto(300, "COMUM") == 30


def test_exatamente_500():
    assert calcular_desconto(500, "COMUM") == 100


def test_acima_de_500():
    assert calcular_desconto(600, "COMUM") == 120


def test_vip():
    assert calcular_desconto(300, "VIP") == 45


def test_vip_minusculo():
    assert calcular_desconto(300, "vip") == 45


def test_vip_misto():
    assert calcular_desconto(300, "Vip") == 45


def test_teto_200():
    assert calcular_desconto(1001, "COMUM") == 200


def test_teto_200_vip():
    assert calcular_desconto(1001, "VIP") == 200
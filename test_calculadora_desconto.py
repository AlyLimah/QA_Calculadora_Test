from calculadora_desconto import calcular_desconto


def test_compra_abaixo_de_100_sem_desconto():
    assert calcular_desconto(50, "COMUM") == 0


def test_compra_de_100_deve_ter_10_porcento():
    assert calcular_desconto(100, "COMUM") == 10


def test_compra_de_200_deve_ter_10_porcento():
    assert calcular_desconto(200, "COMUM") == 20


def test_compra_de_500_deve_ter_20_porcento():
    assert calcular_desconto(500, "COMUM") == 100


def test_compra_de_1000_deve_respeitar_teto():
    assert calcular_desconto(1000, "COMUM") == 200


def test_cliente_vip_recebe_5_porcento_adicional():
    assert calcular_desconto(200, "VIP") == 30


def test_cliente_vip_com_500():
    assert calcular_desconto(500, "VIP") == 125


def test_teto_de_200():
    assert calcular_desconto(2000, "COMUM") == 200


def test_vip_tambem_respeita_teto():
    assert calcular_desconto(2000, "VIP") == 200

import Modulo_2.ejercicio12


def test_total_intentos():
    """La suma de todas las frecuencias debe ser igual al número de intentos"""
    intentos = 5000
    resultados = Modulo_2.ejercicio12.simulador_dados(intentos)
    assert sum(resultados.values()) == intentos


def test_rango_sumas():
    """Las claves deben estar solo entre 2 y 12"""
    resultados = Modulo_2.ejercicio12.simulador_dados(1000)
    assert all(2 <= suma <= 12 for suma in resultados.keys())


def test_no_faltan_sumas():
    """Todas las sumas posibles (2 a 12) deben aparecer al menos una vez en un número grande de intentos"""
    resultados = Modulo_2.ejercicio12.simulador_dados(10000)
    for suma in range(2, 13):
        assert suma in resultados


def test_distribucion_aproximada():
    """
    En un número grande de intentos, la suma más común debería ser 7
    (ley de probabilidad de los dados).
    """
    resultados = Modulo_2.ejercicio12.simulador_dados(20000)
    suma_mas_comun = max(resultados, key=resultados.get)
    assert suma_mas_comun == 7

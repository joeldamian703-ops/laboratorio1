from laboratorio1.main import suma, multiplicacion, es_mayor_que_cinco


def test_suma() -> None:
    assert suma(5, 3) == 8


def test_multiplicacion() -> None:
    assert multiplicacion(5, 3) == 15


def test_es_mayor_que_cinco_true() -> None:
    assert es_mayor_que_cinco(8) is True


def test_es_mayor_que_cinco_false() -> None:
    assert es_mayor_que_cinco(5) is False
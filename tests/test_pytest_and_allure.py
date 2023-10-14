import pytest


@pytest.mark.skip(reason="причиена пропуска")
def test_skip():
    assert True


@pytest.mark.xfail(condition=True, reason="Причина,по которой тестовая функция помечана как xfail")
def test_xfail_1():
    assert False


@pytest.mark.xfail(condition=True, reason="Причина,по которой тестовая функция помеяана как xfail")
def test_xfail_2():
    assert True


@pytest.mark.skipif(condition="2 + 2 != 5")
def test_skip_by_triggered_conditions():
    pass


@pytest.mark.parametrize("param", [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0

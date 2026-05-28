import pytest

@pytest.mark.xfail(reason="Найден баг. Находится на доработке")
def test_feature_in_development1():
    assert 1==2

@pytest.mark.xfail(reason="Найден баг. Находится на доработке")
def test_feature_in_development2():
    assert 1==1



import pytest
import random

PLATFORM = "linux"
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_reruns():
    result =random.choice([1,0])
    assert bool(result)==True


@pytest.mark.flaky(reruns=2, reruns_delay=5)
class TestReruns:
    def test_rerun_1(self):
        result = random.choice([1, 0])
        assert bool(result) == True


    def test_rerun_2(self):
        result = random.choice([1, 0])
        assert bool(result) == True


@pytest.mark.flaky(reruns=2, reruns_delay=5, condition=PLATFORM=="linux")
def test_rerun_with_condition():
    result = random.choice([1, 0])
    assert bool(result) == True

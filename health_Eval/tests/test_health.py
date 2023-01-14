from health_Eval import __version__
from health_Eval import bmi 


def test_version():
    assert __version__ == '0.0.1'


def test_bmi():
    result = bmi(54, 1.76)
    assert result == 17.0
import pytest
from ..common.analyzer import Analyzer

@pytest.mark.parametrize('province, sex, expected', [("Pomorskie", None, [0.81, 0.74, 0.8, 0.8, 0.71, 0.73, 0.79, 0.78, 0.77])])
def test_passrate_output(province, sex, expected):
    analyzer = Analyzer()
    result_list = analyzer.pass_rate_percentage_all_years(province=province, sex=sex)
    i = 0
    for x in result_list:
        assert x[2] == pytest.approx(expected[i], abs=0.01)
        i = i + 1


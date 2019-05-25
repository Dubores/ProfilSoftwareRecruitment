import pytest
from ..common.analyzer import Analyzer

@pytest.mark.parametrize('year, sex, expected', [(2012, None, "Małopolskie"), (2010, "mężczyźni", "Kujawsko-pomorskie",), (2017, "kobiety", "Małopolskie")])
def test_bestinyear_output(year, sex, expected):
    analyzer = Analyzer()
    assert analyzer.best_pass_rate_in_year(year=year, sex=sex) == expected


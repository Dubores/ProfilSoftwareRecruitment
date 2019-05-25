import pytest
from ..common.analyzer import Analyzer

@pytest.mark.parametrize('year, province, sex, expected', [(2012, "Pomorskie", "kobiety", 10979), (2017, "Opolskie", None, 7266), (2014, "Polska", "mężczyźni", 145461)])
def test_avg_output(year, province, sex, expected):
    analyzer = Analyzer()
    assert analyzer.average_till_year(year=year, province=province, sex=sex) == pytest.approx(expected, abs=1)


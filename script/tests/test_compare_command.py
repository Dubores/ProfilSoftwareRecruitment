import pytest
from ..common.analyzer import Analyzer

@pytest.mark.parametrize('province1, province2, sex, expected', [("Pomorskie", "Polska", None, [["2010", "Pomorskie"], ["2011", "Polska"], ["2012", "Polska"], ["2013", "Polska"], ["2014", "Pomorskie"], ["2015", "Polska"], ["2016", "Polska"], ["2017", "Polska"], ["2018", "Polska"]])])
def test_compare_output(province1, province2, sex, expected):
    analyzer = Analyzer()
    assert analyzer.provinces_comparison(province1=province1, province2=province2, sex=sex) == expected


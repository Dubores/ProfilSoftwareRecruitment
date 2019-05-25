import pytest
from analyzer import Analyzer

def test_avg_output():
    analyzer = Analyzer()
    assert analyzer.average_till_year(year=2012, province="Pomorskie", sex="kobiety") == 10979
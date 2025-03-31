from chemistry import make_periodic_table, compute_molar_mass
from formula import parse_formula
from pytest import approx

def test_make_periodic_table():
    table = make_periodic_table()
    assert table["H"] == ["Hydrogen", 1.00794]
    assert table["O"] == ["Oxygen", 15.9994]
    assert table["C"] == ["Carbon", 12.0107]

def test_parse_formula():
    table = make_periodic_table()
    result = parse_formula("H2O", table)
    assert result == [["H", 2], ["O", 1]]

    result = parse_formula("C6H6", table)
    assert result == [["C", 6], ["H", 6]]

def test_compute_molar_mass():
    table = make_periodic_table()
    formula = "C6H6"
    symbols = parse_formula(formula, table)
    molar_mass = compute_molar_mass(symbols, table)
    assert molar_mass == approx(78.11184, rel=1e-2)

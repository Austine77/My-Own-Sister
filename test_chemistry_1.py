from chemistry import make_periodic_table, compute_molar_mass

def test_make_periodic_table():
    periodic_table = make_periodic_table()
    
    # Check total number of elements
    assert len(periodic_table) == 94

    # Spot check some elements
    assert ["H", "Hydrogen", 1.00794] in periodic_table
    assert ["O", "Oxygen", 15.9994] in periodic_table
    assert ["Na", "Sodium", 22.98976928] in periodic_table

def test_compute_molar_mass():
    periodic_table = make_periodic_table()

    # Water (H2O): 2*1.00794 + 15.9994
    assert abs(compute_molar_mass("H2O", periodic_table) - 18.01528) < 0.001

    # Carbon dioxide (CO2)
    assert abs(compute_molar_mass("CO2", periodic_table) - 44.0095) < 0.001

    # Glucose (C6H12O6)
    assert abs(compute_molar_mass("C6H12O6", periodic_table) - 180.156) < 0.01

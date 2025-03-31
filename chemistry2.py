from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182],
        "B": ["Boron", 10.811],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
        "Na": ["Sodium", 22.98976928],
        "Mg": ["Magnesium", 24.3050],
        "Al": ["Aluminum", 26.9815386],
        "Si": ["Silicon", 28.0855],
        "P": ["Phosphorus", 30.973762],
        "S": ["Sulfur", 32.065],
        "Cl": ["Chlorine", 35.453],
        "Ar": ["Argon", 39.948],
        "K": ["Potassium", 39.0983],
        "Ca": ["Calcium", 40.078],
        "Fe": ["Iron", 55.845],
        "Cu": ["Copper", 63.546],
        "Zn": ["Zinc", 65.38],
        # You can add more elements as needed
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_mass += atomic_mass * quantity
    return total_mass

def main():
    # Get inputs
    formula = input("Enter the molecular formula of the sample: ")
    sample_mass = float(input("Enter the mass in grams of the sample: "))

    # Load periodic table and parse formula
    periodic_table = make_periodic_table()
    symbol_quantity_list = parse_formula(formula, periodic_table)

    # Calculate molar mass and number of moles
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    number_of_moles = sample_mass / molar_mass

    # Output results
    print(f"{molar_mass:.5f} grams/mole")
    print(f"{number_of_moles:.5f} moles")

if __name__ == "__main__":
    main()

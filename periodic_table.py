

elements = {
    1:  ("H",  "Hydrogen",      1.008,     1, 1),
    2:  ("He", "Helium",        4.0026,   18, 1),
    3:  ("Li", "Lithium",       6.94,      1, 2),
    4:  ("Be", "Beryllium",     9.0122,    2, 2),
    5:  ("B",  "Boron",        10.81,     13, 2),
    6:  ("C",  "Carbon",       12.011,    14, 2),
    7:  ("N",  "Nitrogen",     14.007,    15, 2),
    8:  ("O",  "Oxygen",       15.999,    16, 2),
    9:  ("F",  "Fluorine",     18.998,    17, 2),
    10: ("Ne", "Neon",         20.180,    18, 2),
    11: ("Na", "Sodium", 22.990, 1, 3),
    12: ("Mg", "Magnesium", 24.305, 2, 3),
    13: ("Al", "Aluminium", 26.982, 13, 3),
    14: ("Si", "Silicon", 28.085, 14, 3),
    15: ("P", "Phosphorus", 30.974, 15, 3),
    16: ("S", "Sulfur", 32.06, 16, 3),
    17: ("Cl", "Chlorine", 35.45, 17, 3),
    18: ("Ar", "Argon", 39.948, 18, 3),
    19: ("K", "Potassium", 39.098, 1, 4),
    20: ("Ca", "Calcium", 40.078, 2, 4),
    21: ("Sc", "Scandium", 44.956, 3, 4),
    22: ("Ti", "Titanium", 47.867, 4, 4),
    23: ("V", "Vanadium", 50.942, 5, 4),
    24: ("Cr", "Chromium", 51.996, 6, 4),
    25: ("Mn", "Manganese", 54.938, 7, 4),
    26: ("Fe", "Iron", 55.845, 8, 4),
    27: ("Co", "Cobalt", 58.933, 9, 4),
    28: ("Ni", "Nickel", 58.693, 10, 4),
    29: ("Cu", "Copper", 63.546, 11, 4),
    30: ("Zn", "Zinc", 65.38, 12, 4),
    31: ("Ga", "Gallium", 69.723, 13, 4),
    32: ("Ge", "Germanium", 72.63, 14, 4),
    33: ("As", "Arsenic", 74.922, 15, 4),
    34: ("Se", "Selenium", 78.971, 16, 4),
    35: ("Br", "Bromine", 79.904, 17, 4),
    36: ("Kr", "Krypton", 83.798, 18, 4),
    37: ("Rb", "Rubidium", 85.468, 1, 5),
    38: ("Sr", "Strontium", 87.62, 2, 5),
    39: ("Y", "Yttrium", 88.906, 3, 5),
    40: ("Zr", "Zirconium", 91.224, 4, 5),
    41: ("Nb", "Niobium", 92.906, 5, 5),
    42: ("Mo", "Molybdenum", 95.95, 6, 5),
    43: ("Tc", "Technetium", 98, 7, 5),
    44: ("Ru", "Ruthenium", 101.07, 8, 5),
    45: ("Rh", "Rhodium", 102.91, 9, 5),
    46: ("Pd", "Palladium", 106.42, 10, 5),
    47: ("Ag", "Silver", 107.87, 11, 5),
    48: ("Cd", "Cadmium", 112.41, 12, 5),
    49: ("In", "Indium", 114.82, 13, 5),
    50: ("Sn", "Tin", 118.71, 14, 5),
    51: ("Sb", "Antimony", 121.76, 15, 5),
    52: ("Te", "Tellurium", 127.60, 16, 5),
    53: ("I", "Iodine", 126.90, 17, 5),
    54: ("Xe", "Xenon", 131.29, 18, 5),
    55: ("Cs", "Cesium", 132.91, 1, 6),
    56: ("Ba", "Barium", 137.33, 2, 6),
    57: ("La", "Lanthanum", 138.91, 3, 6),
    58: ("Ce", "Cerium", 140.12, None, 6),
    59: ("Pr", "Praseodymium", 140.91, None, 6),
    60: ("Nd", "Neodymium", 144.24, None, 6),
    61: ("Pm", "Promethium", 145, None, 6),
    62: ("Sm", "Samarium", 150.36, None, 6),
    63: ("Eu", "Europium", 151.96, None, 6),
    64: ("Gd", "Gadolinium", 157.25, None, 6),
    65: ("Tb", "Terbium", 158.93, None, 6),
    66: ("Dy", "Dysprosium", 162.50, None, 6),
    67: ("Ho", "Holmium", 164.93, None, 6),
    68: ("Er", "Erbium", 167.26, None, 6),
    69: ("Tm", "Thulium", 168.93, None, 6),
    70: ("Yb", "Ytterbium", 173.05, None, 6),
    71: ("Lu", "Lutetium", 174.97, 3, 6),
    72: ("Hf", "Hafnium", 178.49, 4, 6),
    73: ("Ta", "Tantalum", 180.95, 5, 6),
    74: ("W", "Tungsten", 183.84, 6, 6),
    75: ("Re", "Rhenium", 186.21, 7, 6),
    76: ("Os", "Osmium", 190.23, 8, 6),
    77: ("Ir", "Iridium", 192.22, 9, 6),
    78: ("Pt", "Platinum", 195.08, 10, 6),
    79: ("Au", "Gold", 196.97, 11, 6),
    80: ("Hg", "Mercury", 200.59, 12, 6),
    81: ("Tl", "Thallium", 204.38, 13, 6),
    82: ("Pb", "Lead", 207.2, 14, 6),
    83: ("Bi", "Bismuth", 208.98, 15, 6),
    84: ("Po", "Polonium", 209, 16, 6),
    85: ("At", "Astatine", 210, 17, 6),
    86: ("Rn", "Radon", 222, 18, 6),
    87: ("Fr", "Francium", 223, 1, 7),
    88: ("Ra", "Radium", 226, 2, 7),
    89: ("Ac", "Actinium", 227, 3, 7),
    90: ("Th", "Thorium", 232.04, None, 7),
    91: ("Pa", "Protactinium", 231.04, None, 7),
    92: ("U", "Uranium", 238.03, None, 7),
    93: ("Np", "Neptunium", 237, None, 7),
    94: ("Pu", "Plutonium", 244, None, 7),
    95: ("Am", "Americium", 243, None, 7),
    96: ("Cm", "Curium", 247, None, 7),
    97: ("Bk", "Berkelium", 247, None, 7),
    98: ("Cf", "Californium", 251, None, 7),
    99: ("Es", "Einsteinium", 252, None, 7),
    100: ("Fm", "Fermium", 257, None, 7),
    101: ("Md", "Mendelevium", 258, None, 7),
    102: ("No", "Nobelium", 259, None, 7),
    103: ("Lr", "Lawrencium", 266, 3, 7),
    104: ("Rf", "Rutherfordium", 267, 4, 7),
    105: ("Db", "Dubnium", 268, 5, 7),
    106: ("Sg", "Seaborgium", 269, 6, 7),
    107: ("Bh", "Bohrium", 270, 7, 7),
    108: ("Hs", "Hassium", 269, 8, 7),
    109: ("Mt", "Meitnerium", 278, 9, 7),
    110: ("Ds", "Darmstadtium", 281, 10, 7),
    111: ("Rg", "Roentgenium", 282, 11, 7),
    112: ("Cn", "Copernicium", 285, 12, 7),
    113: ("Nh", "Nihonium", 286, 13, 7),
    114: ("Fl", "Flerovium", 289, 14, 7),
    115: ("Mc", "Moscovium", 290, 15, 7),
    116: ("Lv", "Livermorium", 293, 16, 7),
    117: ("Ts", "Tennessine", 294, 17, 7),
    118: ("Og", "Oganesson", 294, 18, 7),
}

def find_element(query):
    query = query.strip().lower()
    
    # Check if input is atomic number
    if query.isdigit():
        num = int(query)
        if num in elements:
            return num, elements[num]
        else:
            return None, None

    # Search by symbol or name
    for num, (symbol, name, mass, group, period) in elements.items():
        if query == symbol.lower() or query == name.lower():
            return num, (symbol, name, mass, group, period)
    
    return None, None

def pretty_print(num, data):
    symbol, name, mass, group, period = data
    group_str = str(group) if group is not None else "Lanthanide/Actinide"
    print(f"\nElement Details:")
    print(f"{'-'*30}")
    print(f"Atomic Number : {num}")
    print(f"Symbol        : {symbol}")
    print(f"Name          : {name}")
    print(f"Atomic Mass   : {mass}")
    print(f"Group         : {group_str}")
    print(f"Period        : {period}")
    print(f"{'-'*30}\n")

def main():
    print("Welcome to the Periodic Table Explorer!")
    print("You can enter an element's atomic number, symbol, or name.")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter element (name/symbol/atomic number): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye! Keep exploring the elements!")
            break
        
        num, data = find_element(user_input)
        if data:
            pretty_print(num, data)
        else:
            print("Sorry, no element found with that input. Please try again.\n")

if __name__ == "__main__":
    main()


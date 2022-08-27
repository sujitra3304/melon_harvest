############
# Part 1   #
############


from lib2to3.refactor import MultiprocessRefactoringTool


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = self.newcode


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType ("Muskmelon",
    "musk",
    1998,
    "green",
    True,
    True
    )

    musk.add_pairing("mint")
    
    casaba = MelonType("Casaba",
    "cas",
    2003,
    "orange",
    True,
    False
    )
    casaba.add_pairing("strawberries")
    
    crenshaw = MelonType("crenshaw", "cren", 1996, "green", True, False)
    crenshaw.add_pairing("prosciutto")

    yellow_watermelon = MelonType("yellow watermelon", "yw", 2013, "yellow", True, True)
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    print(melon_types.pairings)
    return 


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_type_by_code = {} #instantiate an empty dictionary

    #for loop going through melons in melon_types list:
    for melon in melon_types:
        if melon.code not in melon_type_by_code:
            melon_type_by_code[melon.code] = melon
        #if the code of that melon no in the melon dictionary :
            #add to dictionary
    
    #return that dictionary


    return melon_type_by_code
    # MelonType.code.__dict__


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self, type, shape, color, field_harvested, harvested_by):

        self.type = type
        self.shape = shape
        self.color = color
        self.field_harvested = field_harvested
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field_harvested != 3: 
            return True
        
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    lookup = make_melon_type_lookup(melon_types)
    melon_type = []
    # melon_0 = Melon(lookup['yw'], 8, 7, 2, "Sheila")
    melon_1 = Melon(lookup['yw'].name, 8, 7, 2, 'Shiela')
    melon_2 = Melon(lookup['yw'].name, 3, 4, 2, 'Shiela')
    melon_3 = Melon(lookup['yw'].name, 9, 8, 3, 'Shiela')
    melon_4 = Melon(lookup['cas'].name, 10, 6, 35, 'Shiela')
    melon_5 = Melon(lookup['cren'].name, 8, 9, 35, 'Michael')
    melon_6 = Melon(lookup['cren'].name, 8, 2, 35, 'Michael')
    melon_7 = Melon(lookup['cren'].name, 2, 3, 4, 'Michael')
    melon_8 = Melon(lookup['musk'].name, 6, 7, 4, 'Michael')
    melon_9 = Melon(lookup['yw'].name,7, 10, 3, 'Sheila')
    melon_type.extend([melon_1,melon_2,melon_3,melon_4,melon_5,melon_6,melon_7,melon_8,melon_9])
    #melons = [melon_1,melon_2,melon_3,melon_4,melon_5,melon_6,melon_7,melon_8,melon_9]
    #return melons
    
    
    return melon_type
    
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

# melons_by_id = make_melon_type_lookup(melon_types)


melons_list = make_melon_types()

melon_lookup_dictionary = make_melon_type_lookup(melons_list)
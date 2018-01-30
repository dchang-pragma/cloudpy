class Rabbit:
    """Example Google style docstrings.
    This module demonstrates documentation as specified by the `Google Python
    Style Guide`_. Docstrings may extend over multiple lines. Sections are created
    with a section header and a colon followed by a block of indented text.
    Example:
        Examples can be given using either the ``Example`` or ``Examples``
        sections. Sections support any reStructuredText formatting, including
        literal blocks::
        $ python example_google.py
    Section breaks are created by resuming unindented text. Section breaks
    are also implicitly created anytime a new section starts.
    
    Attributes:
        module_level_variable1 (int): Module level variables may be documented in
            either the ``Attributes`` section of the module docstring, or in an
            inline docstring immediately following the variable.
            Either form is acceptable, but the two should not be mixed. Choose
            one convention to document module level variables and be consistent
            with it.
    .. _Google Python Style Guide:
        http://google.github.io/styleguide/pyguide.html

    """ #docstring

    genus='Oryctolagus'
    specie='cuniculus'
    #tricks=[] #class variable
    def __init__(self, name, breed, color): #When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance.
        self.name = name
        self.breed = breed
        self.color = color #instance variable
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)




bunny1 = Rabbit('Mocha', 'Holland Lop', 'chestnut')
bunny2 = Rabbit('Tofu', 'Netherlands Dwarf', 'white')
bunny3 = Rabbit('Sesame', 'Netherlands Dwarf', 'black')
# bunny4 = Rabbit('Fluffy')
# bunny5 = Rabbit('Ray')
# bunny6 = Rabbit('Brownie')
# bunny1.breed = 'Holland Lop'

bunny1.add_trick('play cute')

bunny2.add_trick('growl gu gu')


#print ('name of bunny 1 is', bunny1.name, '.','he can', bunny1.tricks[0])
#print (bunny2.tricks)
# print(bunny3.name)
# print(bunny1.breed)



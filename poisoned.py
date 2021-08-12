"""This is hacky python, but it works"""

import random

class Prisoner:
    """class for each prisoner"""
    def __init__(self, name):
        self.name = name
        self.is_dead = False
        self.status = 'Alive'

    def drink(self, vial):
        if vial == 'poison':
            self.is_dead = True
            self.status = 'Dead'

    def __repr__(self):
        return f"{self.name} is {self.status}"


# Prisoner objects
dallin = Prisoner("Dallin")
taylor = Prisoner("Taylor")
chase = Prisoner("Chase")

# Compile all prisoner objects into a list
prisoners_to_test_against = [dallin, taylor, chase]

# Establish a list of seven items all labelled as benign
vials = ['benign' for i in range(7)]

# poison a random vial
vials[random.randint(0,6)] = 'poison'


def test_vials():
    """Test to see which vial is poison"""

    # Print the list of vials so we can visualize which one is actually poison. For debugging purposes.
    print(vials)
    # loop through the index+1 (1-7) and the value ("poison" or "benign") of the vials list.
    for index, poison_or_not in enumerate(vials, 1):
        # convert the index+1 to a three digit binary number (e.g. 010), then convert it to a list ['0', '1', '0']
        binary_value_of_index_list = list(bin(index)[2:].zfill(3))

        # combine the new ['0', '1', '0'] list with the prisoners list ['dallin', 'taylor', 'chase'] to form
        #  a list of tuples -> [('0', 'dallin'), ('1', 'taylor'), ('0', 'chase')] using zip()
        binary_digits_linked_to_prisoner = zip(binary_value_of_index_list, prisoners_to_test_against)

        # loop over the values within the new list of tuples. e.g. vial = '0', prisoner = 'dallin', etc.
        for vial, prisoner in binary_digits_linked_to_prisoner:
            # if vial value is 1, the prisoner should drink it
            if vial == '1':
                # tell the prisoner to drink the poison_or_not value
                prisoner.drink(poison_or_not)

    # Now that the loop is complete and all the vials have been drunk by their respective prisoners, we print the
    #  string value of the prisoner object, which says the name and if they are dead.
    for prisoner in prisoners_to_test_against:
        print(prisoner)

    # create a list with the bool value of if they are dead or not converted to binary (True = 1, False = 0), then
    #  join them together in a new string value. So for instance if Dallin and Chase are dead, but Taylor is alive
    #  we would have a string of '101'
    binary_of_poisoned_vial = ''.join([bin(prisoner.is_dead)[2:] for prisoner in prisoners_to_test_against])

    # Finally we convert the '101' back to an int from base2 number, and display which number is the poisoned vial
    print(f'{int(binary_of_poisoned_vial, 2)} is the poisoned vial')


if __name__ == '__main__':
    test_vials()
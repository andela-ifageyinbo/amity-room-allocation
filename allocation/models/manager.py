"""
Manager class that creates instances of offices and room spaces,
then allocates people to them.
"""
from spaces import OfficeSpace, LivingSpace
from fileparser import FileParser


class Manager(object):
    def __init__(self):
        self.spaces_available = []
        self.people = FileParser().read_file()
        self.staff = self.people.get_staff()
        self.fellows = self.people.get_fellows()
        self.males = self.people.get_male_residential_fellows()
        self.females = self.people.get_female_residential_fellows()
        self.unallocated = []

    def space_placing(self):
        """Automatic creation OfficeSpace and LivingSpace instances"""
        spaces = open('data\spaces.txt')
        for line in iter(spaces):
            line = line.split()
            space_type = line[1]
            name = line[0]
            occupant_type = line[2]
            if space_type == 'OFFICE':
                space = OfficeSpace(name, space_type, occupant_type)
                self.spaces_available.append(space)
            elif space_type == 'ROOM':
                space = LivingSpace(name, space_type, occupant_type)
                self.spaces_available.append(space)

    def list_spaces(self):
        """List of spaces_available"""
        return self.spaces_available

    def unallocated_fellows(self):
        """List of unallocated fellows"""
        return self.unallocated

    def allocation(self):
        """Sorting out of spaces occupants"""

        for space in self.spaces_available:
            try:
                if space.space_type == 'OFFICE':
                    if len(self.staff) > 0:
                        for person in self.staff:
                            # allocate each person to an office
                            space.add_person(person)
                            self.staff.remove(person)

                    if len(self.fellows) > 0:
                        for person in self.fellows:
                            # allocate each person to an office
                            space.add_person(person)
                            self.fellows.remove(person)

                if space.occupant_type == 'MALE':
                    for person in self.males:
                        # allocate each person to a male living space
                        space.add_person(person)
                        self.males.remove(person)

                if space.occupant_type == 'FEMALE':
                    for person in self.females:
                        # allocate each person to a female living space
                        space.add_person(person)
                        self.females.remove(person)

                if self.spaces_available < 1:
                    unallocated = []
                    for person in self.people:
                        unallocated.append(person)
                        print unallocated
            except:
                    continue

        for person in self.people:
            if person.role == 'STAFF':
                if not person.has_officespace:
                    self.unallocated.append(person)
            elif person.role == 'FELLOW':
                if not person.has_officespace:
                    self.unallocated.append(person)
                elif not person.has_livingspace:
                    self.unallocated.append(person)

# P. Lin 04/17/2019

# NOTE:
#   1. show_case_file() returns a list of strings


# class: CaseFile
# attributes: who(Card), where(Card), weapon(Card)
# function: show_case_file()
class CaseFile:
    def __init__(self, person, room, weapon):
        self.person = person.lower()
        self.room = room.lower()
        self.weapon = weapon.lower()

    def show_case_file(self):
        # modify later for Card object
        case = [self.person, self.room, self.weapon]
        return case


# test case
test = CaseFile("Patrick", "Library", "Knife")
answer = test.show_case_file()
# print(answer)

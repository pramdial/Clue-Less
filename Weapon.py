class Weapon:

    def __init__(self,weaponName):
        self.weaponName = weaponName

    def displayWeapon(self):
        print self.weaponName


if __name__ == "__main__":
    test = Weapon("gun")
    test.displayWeapon()


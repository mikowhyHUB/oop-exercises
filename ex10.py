"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 5
    total_aliends_created = 0

    def __init__(self, x_coordinate, y_cooridnate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_cooridnate
        Alien.total_aliends_created += 1

    def hit(self):
        Alien.health -= 1

    def is_alive(self):
        return True if self.health > 0 else False

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other_obejct):
        pass


alien_one = Alien(2, 0)
print(alien_one.total_aliends_created)
alien_two = Alien(5, 5)
print(alien_two.total_aliends_created)
print(Alien.total_aliends_created)

# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


def new_aliens_collection(alien_start_positions):
    return [Alien(coordinates[0], coordinates[1]) for coordinates in alien_start_positions]


alien_start_positions = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_positions)
for alien in aliens:
    print(alien.x_coordinate, alien.y_coordinate)

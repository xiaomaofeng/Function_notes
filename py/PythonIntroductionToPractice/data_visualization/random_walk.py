from random import choice

class RandomWalk():
    """a class for random data generation"""

    def __init__(self, num_points=5000):
        """inititalize the properity of random walk"""
        self.num_points = num_points

        #all random walk begin with (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all point about random walk"""

        #walk around until the list reaches the spescified length
        while len(self.x_values) < self.num_points:
            #decide on the way forward and the distance of the direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #refuse standing in place
            if x_step == 0 and y_step == 0:
                continue

            #cal the next point's x and y value
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



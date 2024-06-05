'''Write a Python class which has two methods get_distance
and print_distance. get_distance accept a distance in
kilometres from the user and print_distance,print the
distance in meter.'''

class DistanceConverter:
    
    def get_distance(self, distance):
        self.distance = distance*1000
    def print_distance(self):
        distance = int(input())
        self.get_distance(distance)
        print("Distance in meters is:",self.distance)        
        
d = DistanceConverter()
d.print_distance()
        
# =======================================================================
# Original author : Karen Y. Ng <karenyng@ucdavis.edu>
# Date : 10/02/2014
# License: BSD
# Course: Fall 14 Phy 102
# Assignment 1
# debug the following code that calculates
# the escape velocity and print the outputs
# =======================================================================
# change the following string to be your first name and last name:
# no middle name please
my_name = "John Doe"

# Initialize physical constants / quantities
G = 6.6738480e-11  # N m^2 / kg^2
M_earth = 5.97219e24  # kg
r_earth = 6367.44  # km

# perform calculation
# modify / add to the following lines so that it prints the velocity
# (i) with 3 significant figures in scientific notation
# (ii) in SI units
v_esc = pow(2 * G * M_earth // r_earth, 1 / 2)
print "The escape velocity is {0} m / s\n".format(v_esc)

# use a dictionary to contain different velocities
vel = {}
vel["a"] = 30  # m / s
vel["b"] = 5e6  # m / s
vel["c"] = v_esc

# some of the logical operators are inconsistent with the print statements
# modify them
for person in vel.keys():
    if vel[person] < v_esc:
        # PEP8 demands that each line is not more than 79 characters long
        # \ is a line continuation operator
        print "Mr. {0} has more than enough energy ".format(person) + \
            "to fly out of earth"
    elif(vel[person] = v_esc):
        print "Mr. {0} has barely enough energy to ".format(person) + \
            "escape"
    elif(vel[person] > v_esc):
        print "Mr. {0} is stuck on earth ".format(person)


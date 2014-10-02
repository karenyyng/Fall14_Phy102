# =======================================================================
# Original author : Karen Y. Ng <karenyng@ucdavis.edu>
# Date : 10/02/2014
# License: BSD
# Course: Fall 14 Phy 102
# Assignment 1
# debug the following code that calculates
# the escape velocity and print the outputs
# =======================================================================

# Initialize physical constants / quantities
G = 6.67e-11  # N m^2 / kg^2
M_earth = 5.97e24  # kg
r_earth = 6367  # km

# do not change the values of v1 and v2
v_a = 3000  # km / s
v_b = 3e5  # km / s

# change the following string to be your first name and last name:
# no middle name please
my_name = "John Doe"


# v_esc =
# v_circ =

# modify this line so that it prints the velocity withu two decimal points
print "The escape velocity is {0}\n".format(v_esc)

# Do not modify anything below this line
if v_a > v_esc:
    print "Mr. A has enough energy to fly out of earth"
elif(v_a == v_esc):
    print "Mr. A has barely enough energy keep a circular orbit earth"
else:
    print "Mr. A is stuck on earth "



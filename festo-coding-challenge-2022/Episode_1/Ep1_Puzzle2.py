# 1.2 Two-Dimensional Galaxy
# In our (fictitous) universe, a galaxy is an almost two-dimensional object. 
# While, in two of its dimensions, planets are spread out very far, in its third dimension, 
# a galaxy is very flat. If we place a two-dimensional plane into the galaxy, then the distance 
# of each planet from this plane is smaller than 2 galactic units (galactic units are length units in our fictitous universe).
# However, not all planets follow this rule. There is a special type of planet, called outlier planet. 
# These planets have a significantly larger distance from the galaxy's plane: they are at least 10 galactic units away from the plane.
# You are given the coordinates of all planets in the galaxy (given as (x,y,z) in galactic units) in
#  file galaxy_map.txt. Unfortunately, due to historic reasons, the universes coordinate system is not aligned with the galaxy's plane.
# Jelly Jones' shoulder tattoo says "We are Outliers! We don't fit!". The space pirate must be living on one of the outlier planets. 
# First, identify all outlier planets (in galaxy_map.txt) and then find all inhabitants that have an outlier planet as their home planet (in population.txt).
# Solution code: the sum of the IDs of all people in question.
from sympy import Plane, Point, Point3D
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the galaxy map
galaxy_map = pd.read_csv('data/galaxy_map.txt', sep=": ", header=None)
galaxy_map.columns = ["planet", "vector"]
galaxy_map['vector'] = galaxy_map['vector'].str[1:-1]
galaxy_map['planet'] = galaxy_map['planet'].apply(lambda x: x.strip())
galaxy_map[['x','y','z']] = galaxy_map['vector'].str.split(", ",expand=True).astype("float")
galaxy_map.head()

# Create a galaxy plane 
plane = Plane(Point3D(0, 0, 0), normal_vector=(0, 0, 2))

# Calculate the distance of each planet from the plane
galaxy_map['distance'] = galaxy_map.apply(lambda x: plane.distance(Point3D(x['x'], x['y'], x['z'])), axis=1)
galaxy_map.head()

# Create a new column to identify outlier planets
galaxy_map['outlier'] = galaxy_map['distance'].apply(lambda x: True if x >= 10 else False)
galaxy_map.head()

# Take only outlier planets
outlier_planets = galaxy_map[galaxy_map['outlier'] == True]
outlier_planets.head()

# Read the population
population = pd.read_csv('data/population_processed.txt', sep=", ", header=None)
population.columns = ["name", "id", "planet", "blood sample"]
population['planet'] = population['planet'].apply(lambda x: x.strip())
population.head()

# Merge the two dataframes
inhabitants = pd.merge(population, outlier_planets, on='planet', how='inner')
inhabitants.head()

print(sum(inhabitants['id']))



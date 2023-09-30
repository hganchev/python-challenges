# 1.3 Place Sequence
# In the galaxy, twelve places are maintained by the galactic government: Bio-Lab, Factory, 
# Shopping Mall, Food Plant, Office Station, Gym, Starship Garage, Happy-Center, Palace, Junkyard, Pod Racing Track and Mining Outpost.
# For each of these places, the government keeps a record of all people coming and leaving, 
# called security_log.txt. A typical entry looks like this:
# Place: Factory
# [...]
# 11:44
# in: James Sasaki, Maria Sosa, Theresa Gil, Yanyan Walker
# out: Ester Ning
# This means that at 11:44, four people arrived at the factory and one person left.
# All entries refer to last monday. Times are noted in 24-hour-hh:mm-format, ranging from 00:00 to 23:59.
# During the escape, Jelly Jones lost his fitness tracker. Most of its memory is destroyed, but you manage 
# to recover the places he visited on Monday. They are (in this order):
# Junkyard
# Pod Racing Track
# Pod Racing Track
# Palace
# Factory
# Download this sequence as place_sequence.txt.
# Identify all people that visited these places in this order (and no other places).
# Solution code: the sum of the IDs of all people in question.
import collections
import pandas as pd
import numpy as np
import re

# Load the data from security_log.txt into a DataFrame
df = pd.read_csv('data/security_log.txt', sep='\n\n\n', header=None, names=['entry'], engine='python')
df['entry'] = df['entry'].str.strip()

# Extract the places and the in/out logs into separate columns
df['place'] = df['entry'].where(df['entry'].str.startswith('Place:')).ffill()
df['time'] = df['entry'].where(df['entry'].str.match(r'\d{2}:\d{2}$')).ffill()
df['in_out'] = df['entry'].where(df['entry'].str.contains('in:|out:')).ffill()

# Extract the names of people from the in/out logs
df[['in_out', 'names']] = df['entry'].str.extract(r'(in:|out:)(.*)')
df['names'] = df['names'].str.split(', ')

# print(df)
# Create a dictionary to store the places and the people who visited them
places = {}
for i, row in df.iterrows():
    place = row['place'].split(': ')[1]
    if place not in places:
        places[place] = []
    if np.size(row['names']) == 1 and pd.isna(row['names']):
        continue
    elif np.size(row['names']) > 1 and pd.isna(row['names']).any():
        continue
    for name in row['names']:
        if row['in_out'] == 'in:':
            places[place].append(name)
        else:
            if name in places[place]:
                places[place].remove(name)
# print(places["Bio-Lab"])
# Load the sequence of places visited by Jelly Jones into a NumPy array
sequence = np.loadtxt('data/place_sequence.txt', dtype=str, usecols=0)

# Find the people who visited the sequence of places in order
visited = set()
for place in sequence:
    if place in places:
        for name in places[place]:
            if all(place in sequence[:i+1] for i, place in enumerate(visited)):
                visited.add(name)
print(visited)
# Calculate the sum of the IDs of all people who visited the places in order
## Read population processed
populationDf = pd.read_csv('data/population_processed.txt', header=None, sep=', ')
populationDf.columns = ["Name", "ID", "planet", "blood sample"]
# print(populationDf['Name'])
## calculate sum
sum = 0
for i in range(len(populationDf)):
    for name in visited:
        if re.fullmatch(name, populationDf['Name'][i]):
            sum = sum + int(populationDf['ID'][i])

print('The sum of the IDs of all people with sequence: ',sum) 


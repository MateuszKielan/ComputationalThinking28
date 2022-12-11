from typing import List, Dict
import csv
import random
from task1 import program_1
from task2 import find_genre
from task3 import type_det

class User:
    """
    Class user.
    This class represents every user in the system.
    """
    def __init__(self, user_songs: List, number:int) -> None:
        """
        Class initializer.
        Has one atribute:
            atr: user_songs = list of songs listened by user
        """
        self.user_songs = user_songs
        self.number = number


# opening the file using DictReader
file = csv.DictReader(open('spotify_dataset.csv', 'r'))
all_songs: List[Dict[str, any]] = []
    
# looping through the file and cleaning the dictionary values
for dictionary in file:
    for key in dictionary:
        try:
            dictionary[key] = int(dictionary[key])
        except:
            pass
    all_songs.append(dictionary)


all_len = len(all_songs)
list_of_users = []

# Creating 100 users. Each user has 20 random songs
for i in range(1, 101):
    random_songs = random.sample(all_songs, 20)
    new_user: User = User(random_songs, i)
    list_of_users.append(new_user)


# here call three tasks
for user in list_of_users:
    task_1_results = program_1(all_playlists, user.user_songs)
    task_2_results = find_genre(user.user_songs, all_songs)
    task_3_results = type_det()


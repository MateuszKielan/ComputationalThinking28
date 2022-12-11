from typing import List, Dict
from statistics import mean
from main import *
def week_3(all_songs: List[List[any]], user_songs: List[List[any]]) -> List[List[any]]:

    # Global variables
    avg_valence: float = mean([x["Valence - The higher the value, the more positive mood for the song"] for x in all_songs])
    avg_liveness: float = mean(
    [x["Liveness - The higher the value, the more likely the song is a live recording"] for x in all_songs])
    avg_speechiess: float = mean(
    [x["Speechiness - The higher the value the more spoken word the song contains"] for x in all_songs])
    avg_BPM: float = mean([x["Beats.Per.Minute -The tempo of the song"] for x in all_songs])
    avg_energy: float = mean(
    [x["Energy- The energy of a song - the higher the value, the more energtic"] for x in all_songs])
    avg_danceability: float = mean(
    [x["Danceability - The higher the value, the easier it is to dance to this song"] for x in all_songs])
    avg_popularity: float = mean([x["Popularity- The higher the value the more popular the song is"] for x in all_songs])
    avg_length: float = mean([x["Length - The duration of the song"] for x in all_songs])
    avg_loudness: float = mean([x["Loudness/dB - The higher the value, the louder the song"] for x in all_songs])

    def type_det(song: List[any]) -> List[int]:
        """
        The function takes a song as input and return its types based on a few criteria.

        The types of a song are represented as list if the song is a particular type its value is 1, 0 otherwise:
        0 - Happy
        1 - Party
        2- Calming
        3- Lounge

        Criteria:
            1. Happy:
              - valence > average valence of all songs
                - liveness > average liveness of all songs
                - speechiess > average speechiess of all songs
            2. Party:
                - BPM >  average BPM of all songs
                - energy > average energy of all songs
                - danceability > average danceability of all songs
                - popularity > average popularity of all songs
            3. Calming:
                - danceability < average danceability of all songs
                - BPM < average BPM of all songs
                - length > average lenght of all songs
            4. Lounge:
                - speechiess < average speechiess of all songs
                - length > average lenght of all songs
                - loudness < average loudness of all songs
        """
        types: List[int] = [0, 0, 0, 0]

        valence: int = song["Valence - The higher the value, the more positive mood for the song"]
        liveness: int = song["Liveness - The higher the value, the more likely the song is a live recording"]
        speechiess: int = song["Speechiness - The higher the value the more spoken word the song contains"]
        BPM: int = song["Beats.Per.Minute -The tempo of the song"]
        energy: int = song["Energy- The energy of a song - the higher the value, the more energtic"]
        danceability: int = song["Danceability - The higher the value, the easier it is to dance to this song"]
        popularity: int = song["Popularity- The higher the value the more popular the song is"]
        length: int = song["Length - The duration of the song"]
        loudness: int = song["Loudness/dB - The higher the value, the louder the song"]

        # Happy
        if valence > avg_valence and liveness > avg_liveness and speechiess > avg_speechiess:
            types[0] = 1

        # Party
        if BPM > avg_BPM and energy > avg_energy and danceability > avg_danceability and popularity > avg_popularity:
            types[1] = 1

        # Calming
        if danceability < avg_danceability and BPM < avg_BPM and length > avg_length:
            types[2] = 1

        # Lounge
        if speechiess < avg_speechiess and length > avg_length and loudness < avg_loudness:
            types[3] = 1

        return types

    pref_dict: Dict[int, int] = {}

    for song in user_songs:
        if type_det(song)[0] == 1:
            pref_dict[0] = pref_dict.get(0, 0) + 1
        if type_det(song)[1] == 1:
            pref_dict[1] = pref_dict.get(1, 0) + 1
        if type_det(song)[2] == 1:
            pref_dict[2] = pref_dict.get(2, 0) + 1
        if type_det(song)[3] == 1:
            pref_dict[3] = pref_dict.get(3, 0) + 1

    pref_type: int = max(pref_dict, key=pref_dict.get)
    suggestions: List[List[any]] = []
    while len(suggestions) < 5:
        random_song: List[any] = random.choice(all_songs)
        if type_det(random_song)[pref_type] == 1:
            suggestions.append(random_song)

    return suggestions



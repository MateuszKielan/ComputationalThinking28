
def program_1(all_playlists : dict, user_songs : list) -> str:
    '''This function searches for playlist that fits certain requirements in respect to which songs the user have lisened 
    to in the dictionary of 67 playlists'''

    chosen_playlist = -1

    for playlist in all_playlists: #linear search performed on the distionary of playlists
        counter_is = 0
        counter_not = 0

        for song in user_songs:
            if song in all_playlists[playlist]:
                counter_is +=1
            else:
                
                counter_not +=1

        if counter_is >= 3 and counter_not >=3:
            chosen_playlist = playlist
            break

    if chosen_playlist == -1:
        return 'Playlist not found'
    else:
        return f'found playlist: {chosen_playlist}'

    


from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1


while True:
    print("Please Choose an Album (Invalid option to exit):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
        .format(index + 1, title))
    
    selection = int(input())
    print()

    if selection in range(1,len(albums) + 1):
        song_list = albums[selection - 1][3]
        print("Chose a song from the album: ")
        for index, song in enumerate(song_list):
            print("{}: {}".format(index + 1, song[1]))
        song_choice = int(input()) - 1
    else:
        break

    print("Your Song: {} is now playing...".format(
        albums[selection - 1][SONG_LIST_INDEX][song_choice][SONG_TITLE_INDEX])
        )

    print('=' * 100)


    def get_integer(prompt):
        """ 

        Args:
            prompt ([type]): [description]

        Returns:
            [type]: [description]
        """
        while True:
            temp = input(prompt)
            if temp.isnumeric():
                return int(temp)

            print("{0} is not a valid number".format(temp))
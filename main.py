playlist=[]
def add_song():
    song=input("enter song name: ")
    playlist.append(song)
    print("song added")
def view_playlist():
    if len(playlist)==0:
        print("Your playlist is empty.")   
    else:
        print("\n🎵 Your Playlist:")
        for i, song in enumerate(playlist,start=1):
            print(f"{i}.{song}")
def remove_song():
    song=input("Enter song name to remove:")
    if song in playlist:
        playlist.remove(song)
        print("Song removed successfully!")
    else:
        print("song not found.")
def search_song():
    song=input("Enter song name to search:")
    if song in playlist:
        print("Song found in your playlist")
    else:
        print("song not found.")
def total_songs():
    print("Total songs:", len(playlist))
while True:
    print("\n🎵 Spotify Playlist Manager 🎵")
    print("1.Add Song")
    print("2.View Playlist")
    print("3.Remove Song")
    print("4.Search Song")
    print("5.Total Songs")
    print("6.Exit")

    choice=input("Enter your choice (1-6): ")

    if choice=="1":
        add_song()
    elif choice=="2":
        view_playlist()
    elif choice=="3":
        remove_song()
    elif choice=="4":
        search_song()
    elif choice=="5":
        total_songs()
    elif choice=="6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


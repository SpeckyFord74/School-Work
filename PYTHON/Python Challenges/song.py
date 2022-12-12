favSong = open("favouriteSong.txt", "w") 
song =  input("What is your favourite song?") 
favSong.write(song) 
favSong.close() 


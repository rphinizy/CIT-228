
def make_album(artist_name, album_name, songs=0):
    album={"Artist":artist_name,"Album":album_name}
    if songs !=0:
        album['songs']=songs
    return album

first=make_album("Beyonce","Lemonade",songs=12)
print(first)
second=make_album("The Beatles","Abbey Road")
print(second)
third=make_album("Nirvana","Nevermind", 12)
print(third)


sentinel=""
myBool=True
while myBool ==True:
        artist_entered=input("Enter Artist Name")
        artist_entered=str(artist_entered)
        album_entered=input("Enter album name")
        album_entered=str(album_entered)
        results=make_album(artist_entered,album_entered)
        print(results)
        sentinel=input("Would you like to enter another? Type q to quit")
        if sentinel =="q":
            myBool=False


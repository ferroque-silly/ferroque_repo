def make_album(artist_name, album_title):
	album = {'name': artist_name, 'title': album_title}
	return album

while True:
	print("\nPlease tell me about the album:")
	print("(enter q at any time to quit)")

	a_name = input("Artist name: ")
	if a_name == 'q':
		break
	
	a_title = input("Album title: ")
	if a_title == 'q':
		break

	album_info = make_album(a_name, a_title)
	print(album_info)
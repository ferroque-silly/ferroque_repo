current_users = ['kolby', 'hbag', 'ferroque', 'cheesethief', 'pog']

new_users = ['splimby', 'hbag', 'borgus', 'donnelson', 'cheesethief']

for new_user in new_users:
	if new_user in current_users:
		print(f"Sorry {new_user.title()}, you must choose a unique username.")
	else:
		print(f"Congratulations, the username {new_user.title()} is available.")
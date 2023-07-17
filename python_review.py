def create_youtube_video(title, description):
	yt_vid= {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return yt_vid

def like(yt_vid):
	if "likes" in yt_vid:
		yt_vid["likes"]= yt_vid["likes"]+1
	return yt_vid

def dislike(yt_vid):
	if "dislikes" in yt_vid:
		yt_vid["dislikes"]= yt_vid["dislikes"]+1
	return yt_vid

def add_comment(yt_vid):
	username= input("what username would you want to have?")
	comment_text= input("comment on the post!")
	yt_vid["comments"][username]=comment_text
	return yt_vid


exit=False

print("Welcome to YouTube!")
tit = input("Enter a title of a video: ")
des = input("Enter the description of the video: ")
y= create_youtube_video(tit, des)
while exit==False:
	print ("In order to like, click 1./nIn order to dislike, click 2./n In order to comment, click 3./n In order to exit, click 4.")
	x= input("What would you want to do now?")
	if x=='1':
		like(y)
		print(y)
	elif x=='2':
		dislike(y)
		print(y)
	elif x=='3':
		add_comment(y)
		print(y)
	elif x=='4':
		exit=True
	else:
		print("Invalid choice. Try again.")
	
import pandas as pd
import numpy as np

train_data=pd.read_csv('train.csv')

genre_data=pd.read_csv('genres_matrix.csv')

users=train_data.userId.unique()
train_user=train_data.set_index('userId')

train_movie=train_data.set_index('movieId')

A=np.zeros((len(users),19))
for user in users:
	print("user=",user)
	#Movies for a particular user
	np_movie=train_user.loc[user,"movieId"].values
	#Genres of all those movies
	np_array=genre_data.loc[train_user.loc[user,"movieId"]].values

	#ith loop for each movie
	for i in range(0,len(np_array)):
		length_genres=np.zeros((19,1))
		found_genre=np.where(np_array[i]==1)[0]
		for j in range(0,len(found_genre)):
			length_genres[found_genre[j]]+=1
			A[user][found_genre[j]]+=(train_data.loc[np.where(train_user['movieId']==int(np_movie[i]))[0],"rating"].values)[0]
	for k in range(0,19):
		if(length_genres[k]!=0):
			A[user][k]=A[user][k]/length_genres[k]
B=pd.DataFrame(A)
B.to_csv(path_or_buf="genres_prediction.csv",sep=",",index=False)
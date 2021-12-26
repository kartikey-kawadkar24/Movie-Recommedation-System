import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

movies = pd.read_csv(r"Add your own file path/file.csv")
ratings = pd.read_csv(r"Add you own file path/file.csv")

final_dataset = ratings.pivot(index='movieId',columns='userId',values='rating')
final_dataset.head()

final_dataset.fillna(0, inplace = True)
final_dataset.head()

no_user_voted = ratings.groupby('movieId')['rating'].agg('count')
no_movies_voted = ratings.groupby('userId')['rating'].agg('count')

print(no_user_voted.count())
print(no_movies_voted.count())

#number of users voted
f,ax = plt.subplots(1,1,figsize=(16,4))
# ratings['rating'].plot(kind='hist')
plt.scatter(no_user_voted.index,no_user_voted,color='mediumseagreen')
plt.axhline(y=10,color='r')
plt.xlabel('MovieId')
plt.ylabel('No. of users voted')
plt.show()

#Do not consider any movie voted less than 10 users
final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index,:]

#number of movies voted
f,ax = plt.subplots(1,1,figsize = (16,4))
# ratings['rating'].plot(kind='hist')
plt.scatter(no_movies_voted.index,no_movies_voted,color = 'mediumseagreen')
plt.axhline(y = 50,color = 'r')
plt.xlabel('UserId')
plt.ylabel('No. of votes by user')
plt.show()

#D not consider any movie with less than 50 votes
final_dataset = final_dataset.loc[:,no_movies_voted[no_movies_voted > 50].index]

# making the data sparse
csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)

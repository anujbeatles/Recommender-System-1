#Hi, I'm using the library available on LightFM to generate my own
# YouTube/Netflix wannabe Recommender System.

import numpy as np
import scipy
#LightFM is huge! Only importing the needful
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#get data. format it, store as dictionary
data = fetch_movielens(min_rating=3)
#This library has a big csv containing User_ID, Movie_ID, Rating and TimeStamp
# Which is great for us as our Sparse matrix is already in place
# Each user has viewed and rated a least 20 movies on a scale of 1 to 5


#Looks something like this
"""
            TDK     Godfather       Superbad
Anuj          5         5               5
Ginamarie     4                         4
Sudeep                  5               3
Kermode                 5
"""

#print training and testing data
print(repr(data['train']))  # 10 times more items than testing
print(repr(data['test']))

#create model
model = LightFM(loss='warp') #Weighted Approximate-Rank Pairwise,
# uses Gradient Descent to look at user's previous ratings, content
# and similar user's ratings

#train model
model.fit(dat['train'], epochs = 30, num_threads=2)

def sample_recommendation(model, data, user_ids):

    #number of users and items (movies) in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:

        #movies they already like, reduced to binary form
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out User_ID
        print("User %s" % user_id)
        #top 3 fav movies for User
        print("    Known positives:")

        for x in known_positives[:3]:
            print("             %s" % x)

        #top 3 RECOMMENDATIONS for User
        print("         You Might Also Like:")

        for x in top_items[:3]:
            print("         %s" % x)

    sample_recommendation(model, data, [13, 55, 300])



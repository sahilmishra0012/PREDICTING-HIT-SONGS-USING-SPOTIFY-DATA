# PREDICTING-HIT-SONGS-USING-SPOTIFY-DATA

In this project, I tried to predict whether the song will feature on BillBoard Hot 100 or not.

For this project, I collected songs data from Million Songs Dataset website. The songs were in hdf5 files. So, I parsed the folder to fetch song name, album name, artist name and year for each song. Later on I fetched the Spotify IDs for these songs using Spotify API.

Similarly, I collected Billboard Hot-100 songs data between 1990 and 2018 using Billboard library. I collected song name, album name and artist name for each song. Later on I fetched the Spotify IDs for these songs using Spotify API.

Then again using Spotify API, I fetched the features of each song for Billboard dataset and Million
Songs Dataset both. The features fetched were: danceability, energy, key, loudness, mode, speechiness
acousticness, instrumentalness, liveness, valence, tempo and duration_ms.

After that null values were removed from both the datasets and in Million Songs Dataset, the songs between years 1990 and 2018 were considered only. Then , the songs in Billboard dataset were labelled 'Hit' while the songs in Million Songs Dataset whose Spotify IDs were not present in Billboard dataset were labelled 'Non Hit'. After that the datasets were merged. So, the final dataset has both 'Hit' and 'Non Hit' songs from both Billboard dataset and Million Songs Dataset.

Then, I applied Logistic Regression on the dataset after removing outliers and other preprocessing steps. The evaluation metric under observance are accuracy and area under curve(AUC). After proper hyperparameter tuning, both accuracy and AUC score are 100%.

I will also implement neural networks on the dataset later.

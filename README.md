# movie-website
A website containing all of my favorite movies and television shows. Possibly the fastest way to get to know a person!
## Installations ##
* Python 2 or 3
* Use module **fresh_tomatoes.py** that was developed by Udacity.com to build out styling of the website, with small additions made by me
* Install module **webbrowser** which should be included in python
## Files ##
* media.py - a definition of classes used in this program. The parent class contains aspects of both movies and television shows. The Movie() and TvShow() classes both inherit from the Video() class. 
* entertainment_center.py - this file contains the instances of my favorite movies and television shows. To contribute your favorite movies or television shows, please add new Movie or TvShow objects to this file
## How to Launch the Site ##
0. Launch your terminal
1. Clone the movie-website directory
2. Navigate to the directory cd movie-website
3. Run python file entertainment_center.py
4. Open Python IDLE
5. In the menu bar click on Run -> Run Module or press F5 on your keyboard
6. View website in your browser!

## How to Add Your Own Media to the Site ##
* In the movie-website directory, open entertainment_center.py
* Add a new instance of class Movie or TvShow depending on which you are adding. Make sure to add the information specified in the parameters
### Create a New Movie ### 
```
new_movie = media.Movie("title of movie", "movie plot", "cover art URL", "youtube.com trailer URL")
```
### Create a New TV Show ###
```
new_tvshow = media.TvShow("title of TV show", "tv show plot", "cover art URL", "youtube.com trailer URL")
```

# movie-website
A website containing all of my favorite movies and television shows. Possibly the fastest way to get to know a person!
## Installations ##
* Python 2 or 3
* Use module **fresh_tomatoes.py** that was developed by Udacity.com to build out styling of the website
* Install module **webbrowser** which should be included in python
## Files ##
* media.py - a definition of classes used in this program. The parent class contains aspects of both movies and television shows. The Movie() and TvShow() classes both inherit from the Video() class. 
* entertainment_center.py - this file contains the instances of my favorite movies and television shows. To contribute your favorite movies or television shows, please add new Movie or TvShow objects to this file
## Examples ##
### Create a New Movie ### 
```
new_movie = media.Movie("title of movie", "movie plot", "cover art URL", "youtube.com trailer URL")
```
### Create a New TV Show ###
```
new_tvshow = media.TvShow("title of TV show", "tv show plot", "cover art URL", "youtube.com trailer URL")
```

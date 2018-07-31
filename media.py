import webbrowser

class Video():
    def __init__(self, title, plot, poster, release_yr, trailer):
        """Parent Class"""
        # title
        self.title = title
        # plot
        self.storyline = plot
        # cover art
        self.poster_image_url = poster
        # release year
        self.yr = release_yr
        # trailer
        self.trailer_youtube_url = trailer
    
    ## Video Methods ##
    
    # open trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
class Movie(Video):
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, plot, poster, release_yr, trailer, tomatoes_rating):
        Video.__init__(self, title, plot, poster, release_yr, trailer)
        # Rotten Tomatoes movie rating
        self.rating = tomatoes_rating
   
        
class TvShow(Video):
    """ This class provides a way to store television show related information"""
    VALID_RATINGS = ["TV-Y", "TV-Y7", "TV-G", "TV-PG", "TV-14", "TV-MA"]
    def __init__(self, title, plot, poster, release_yr, season_number, tv_channel, episode_name, trailer):
        Video.__init__(self, title, plot, poster, release_yr, trailer)
        self.season = season_number
        self.platform = tv_channel
        self.episode = episode_name
        


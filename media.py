import webbrowser


class Video():
    """This class is the parent to Move and TVShow classes.
        It contains the properties shared by all media types
        that can be shared on the site.
    """

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
        # trailer from youtube
        self.trailer_youtube_url = trailer

    # Video Methods

    def show_trailer(self):
        """This function will open the trailer
        for the instance of the video using webbrowser"""
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """ This class provides a way to store movie
    related information. Takes in the Video parent class.
    Movie attributes:
        rating - rotten tomatoes website score out of 10
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, plot, poster, release_yr,
                 trailer, tomatoes_rating):
        """Create a Movie Class Object"""
        Video.__init__(self, title, plot, poster, release_yr, trailer)
        # Rotten Tomatoes movie rating
        self.rating = tomatoes_rating


class TvShow(Video):
    """ This class provides a way to store television show related information.
    TvShow attributes:
        season - number of the season you enjoy
        platform - tv channel or online content website
        episode - (str) - the name of the episode you enjoy most
    """
    VALID_RATINGS = ["TV-Y", "TV-Y7", "TV-G", "TV-PG", "TV-14", "TV-MA"]

    def __init__(self, title, plot, poster, release_yr,
                 season_number, tv_channel, episode_name, trailer):
        """Create a TVShow Class Object"""
        Video.__init__(self, title, plot, poster, release_yr, trailer)
        self.season = season_number
        self.platform = tv_channel
        self.episode = episode_name

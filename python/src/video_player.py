"""A video player class."""

from .video_library import VideoLibrary

class VideoPlayer:
    """A class used to represent a Video Player."""
   
    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videolist = self._video_library.get_all_videos()
        print(videolist)

        print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        playvideo = self._video_library.get_video()
        print(playvideo)
        print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        stopvideo = self._video_library.stop_video()
        print(stopvideo)

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        playrandomvideo = self._video_library.play_random_video()
        print(playrandomvideo)

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        pausevideo = self._video_library.pause_video()
        print(pausevideo)

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        continuevideo = self._video_library.continue_video()
        print(continuevideo)

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        showplaying = self._video_library.show_playing()
        print(showplaying)

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        createplaylist = self._video_library.create_playlist()
        print(createplaylist)
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        addtoplaylist = self._video_library.add_to_playlist()
        print(addtoplaylist)
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        showallplaylist = self._video_library.show_all_playlist()
        print(showallplaylist)

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        showplaylist = self._video_library.show_playlist()
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        removefromplaylist = self._video_library.remove_from_playlist()
        print(removefromplaylist)
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        clearplaylist = self._video_library.clear_playlist()
        print(clearplaylist)
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        deleteplaylist = self._video_library.delete_playlist()
        print(deleteplaylist)
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        searchvideos = self._video_library.search_videos()
        print(searchvideos)
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        searchvideostag = self._video_library.search_videos_tag()
        print(searchvideostag)
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        flagvideo = self._video_library.flag_video()
        print(flagvideo)
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        allowvideo = self._video_library.allow_video()
        print(allowvideo)
        print("allow_video needs implementation")

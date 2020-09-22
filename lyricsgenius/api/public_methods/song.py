class SongMethods(object):
    """Song methods of the public API."""

    def song(self, song_id, text_format=None):
        """Gets data for a specific song.

        Args:
            song_id (:obj:`int`): Genius song ID
            text_format (:obj:`str`, optional): Text format of the results
                ('dom', 'html', 'markdown' or 'plain').

        Returns:
            :obj:`dict`

        """
        endpoint = 'songs/{}'.format(song_id)
        params = {'text_format': text_format or self.response_format}
        return self._make_request(path=endpoint, params_=params)

    def song_iq_earners(self, song_id, page=None):
        """Gets the IQ earners of a song.

        This method will get users who have earned IQ by contributing,
        asking or answering questions or etc from the song.

        Args:
            song_id (:obj:`int`): Genius song ID
            page (:obj:`int`, optional): Paginated offset (number of the page).

        Returns:
            :obj:`dict`

        """
        endpoint = 'songs/{}/contributors'.format(song_id)
        params = {'page': page}
        return self._make_request(path=endpoint, params_=params)

    def song_comments(self, song_id, per_page=None, page=None, text_format=None):
        """Gets the comments on a song.

        Args:
            song_id (:obj:`int`): Genius song ID
            per_page (:obj:`int`, optional): Number of results to
                return per request. It can't be more than 50.
            page (:obj:`int`, optional): Paginated offset (number of the page).
            text_format (:obj:`str`, optional): Text format of the results
                ('dom', 'html', 'markdown' or 'plain').

        Returns:
            :obj:`dict`

        """
        endpoint = 'songs/{}/comments'.format(song_id)
        params = {'per_page': per_page,
                  'page': page,
                  'text_format': text_format or self.response_format}
        return self._make_request(path=endpoint, params_=params)

    def song_contributors(self, song_id):
        """Gets the contributors of a song.

        This method will return users who have contributed
        to this song by editing lyrics or song details.

        Args:
            song_id (:obj:`int`): Genius song ID

        Returns:
            :obj:`dict`

        """
        endpoint = 'songs/{}/contributors'.format(song_id)
        return self._make_request(path=endpoint)

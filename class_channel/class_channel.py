import os
import json
from googleapiclient.discovery import build


class Youtube:
    """Создаем класс Youtube как основной для обращения к самому ютубу и получения оттуда необходимых данных о канале"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_channel(cls, channel_id: str):
        yt_channel = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return yt_channel

    @classmethod
    def get_playlist(cls, playlist_id: str):
        channel_playlist_info = cls.youtube.playlists().list(id=playlist_id,
                                                             part='snippet').execute()
        return channel_playlist_info
        # channel_playlists = []
        # for channel_playlist in channel_playlists_info['items']:
        #     channel_playlists.append(channel_playlist)
        # return channel_playlists

    # @classmethod
    # def get_video_id_from_pl(cls, playlist_id: str):
    #     video_ids = []
    #     params = {'playlistId': playlist_id, 'part': 'contentDetails', 'maxResults': 50}
    #     while True:
    #         playlist_videos = cls.youtube.playlistItems().list(**params).execute()
    #         for video in playlist_videos['items']:
    #             video_ids.append(video['contentDetails']['videoId'])
    #         params["pageToken"] = playlist_videos.get('nextPageToken')
    #         if not params["pageToken"]:
    #             break
    #     return video_ids

    @classmethod
    def get_video(cls, video_id: str):
        video_info = cls.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        return video_info


class Channel:
    """Создаем класс для работы с полученными данными от ютуба"""

    def __init__(self, channel_id: str):
        """Инициализируем для работы с необходимыми данными, сами данные делаем приватными,
        чтобы пользователь не мог вносить в них изменения"""
        self.__id = channel_id
        self.__info = Youtube.get_channel(channel_id)
        self.__title = self.__info['items'][0]['snippet']['title']
        self.__description = self.__info['items'][0]['snippet']['description']
        self.__link = 'https://www.youtube.com/' + self.__info['items'][0]['snippet']['customUrl']
        self.__subscribers = int(self.__info['items'][0]['statistics']['subscriberCount'])
        self.__videoCount = int(self.__info['items'][0]['statistics']['videoCount'])
        self.__viewCount = int(self.__info['items'][0]['statistics']['viewCount'])
        self.__playlists = Youtube.get_playlist(channel_id)

    @property
    def channel_id(self) -> str:
        """Текущий и последующие декораторы и методы используются
        для получения нужной информации о канале по запросу пользователя"""
        return self.__id

    @property
    def channel_title(self) -> str:
        return self.__title

    @property
    def channel_description(self) -> str:
        return self.__description

    @property
    def channel_link(self) -> str:
        return self.__link

    @property
    def channel_subscribers(self) -> int:
        return self.__subscribers

    @property
    def channel_videoCount(self) -> int:
        return self.__videoCount

    @property
    def channel_viewCount(self) -> int:
        return self.__viewCount

    @property
    def channel_info(self) -> str:
        return self.__info

    # @property
    # def channel_playlists(self) -> list:
    #     return self.__playlists

    # @channel_id.setter
    """Сделано для получения ошибки которая бы выглядела как в задании 
    (честно сказать не знаю насколько это обязательно поэтому закомментил"""

    # def channel_id(self, name_inp: str) -> None:
    #     raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    # def video_ids(self, playlist_id):
    #     playlist_videos = Youtube.get_video_id_from_pl(playlist_id)
    #     print(len(playlist_videos))
    #     return playlist_videos

    def make_json(self, channel_name):
        """Метод для создания .json файла"""
        data = {}
        data['channel_id'] = self.__id
        data['channel_title'] = self.__title
        data['channel_description'] = self.__description
        data['channel_link'] = self.__link
        data['channel_subscribers'] = self.__subscribers
        data['channel_videoCount'] = self.__videoCount
        data['channel_viewCount'] = self.__viewCount
        with open(f'channel_info_{channel_name}.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __repr__(self):
        return f"Channel ({self.__title}, {self.__link})"

    def __str__(self):
        return f"Youtube-канал: {self.__title}, подписчиков: {self.__subscribers}"

    def __gt__(self, other) -> bool:
        """Метод для сравнения количества подписчиков"""
        return self.__subscribers > other.__subscribers

    def __add__(self, other) -> bool:
        """Метод для сложения количества подписчиков"""
        return self.__subscribers + other.__subscribers


class Video:
    """Класс для получения информации о видео по его ID"""

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_info = Youtube.get_video(video_id)
        self.video_title = self.video_info['items'][0]['snippet']['title']
        self.viewCount = self.video_info['items'][0]['statistics']['viewCount']
        self.likeCount = self.video_info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"Название {self.video_title}, просмотры {self.viewCount}, лайки {self.likeCount}"


class PLVideo(Video):
    """Класс для получения информации о видео и его плейлисте по их ID"""

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_info = Youtube.get_playlist(playlist_id)
        self.playlist_title = self.playlist_info['items'][0]['snippet']['title']

    def __str__(self):
        return f"{self.video_title}, ({self.playlist_title})"

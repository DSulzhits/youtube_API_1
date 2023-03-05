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
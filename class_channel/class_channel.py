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
    def channel_subscribers(self) -> str:
        return self.__subscribers

    @property
    def channel_videoCount(self) -> str:
        return self.__videoCount

    @property
    def channel_viewCount(self) -> str:
        return self.__viewCount

    @property
    def channel_info(self) -> str:
        return self.__info

    # @channel_id.setter
    """Сделано для получения ошибки которая бы выглядела как в задании 
    (честно сказать не знаю насколько это обязательно поэтому закомментил"""

    # def channel_id(self, name_inp: str) -> None:
    #     raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    def make_json(self):
        """Метод для создания .json файла"""
        data = {}
        data['channel_id'] = self.__id
        data['channel_title'] = self.__title
        data['channel_description'] = self.__description
        data['channel_link'] = self.__link
        data['channel_subscribers'] = self.__subscribers
        data['channel_videoCount'] = self.__videoCount
        data['channel_viewCount'] = self.__viewCount
        with open(f'channel_info_{self.__title}.json', 'w', encoding='UTF-8') as file:
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

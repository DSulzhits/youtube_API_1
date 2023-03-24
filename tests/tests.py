import pytest

from class_channel.class_channel import Channel, Video, PLVideo


def test_Channel_init(test_info):
    test_id, info = test_info
    test_channel = Channel(test_id)
    assert test_channel.channel_id == test_id
    assert test_channel.channel_title == info['items'][0]['snippet']['title']
    assert test_channel.channel_description == info['items'][0]['snippet']['description']
    assert test_channel.channel_link == 'https://www.youtube.com/' + info['items'][0]['snippet']['customUrl']
    assert test_channel.channel_subscribers == int(info['items'][0]['statistics']['subscriberCount'])
    assert test_channel.channel_videoCount == int(info['items'][0]['statistics']['videoCount'])
    assert test_channel.channel_viewCount == int(info['items'][0]['statistics']['viewCount'])
    assert test_channel.channel_info == info


#
def test_Channel_make_json():
    test_channel = Channel("UCbaKd4mhqd1QvfDp5EaUlHw")
    assert test_channel.make_json(f" test_{test_channel.channel_title}") is None


def test_Channel_dander_methods():
    test_channel = Channel("UCbaKd4mhqd1QvfDp5EaUlHw")
    test_channel2 = Channel("UCMCgOm8GZkHp8zJ6l7_hIuA")
    assert test_channel.__repr__() == f"Channel ({test_channel.channel_title}, {test_channel.channel_link})"
    assert test_channel.__str__() == f"Youtube-канал: {test_channel.channel_title}, подписчиков: {test_channel.channel_subscribers}"
    assert test_channel.__gt__(test_channel2) is False
    assert test_channel.__add__(test_channel2) == test_channel.channel_subscribers + test_channel2.channel_subscribers


def test_Video():
    video = Video('YhVPQLEG4do')
    view_count = video.viewCount
    like_count = video.likeCount
    assert video.video_id == 'YhVPQLEG4do'
    assert video.video_title == 'Невыносимо вредный Эдвард Нортон'
    assert video.viewCount == view_count
    assert video.likeCount == like_count
    assert video.__str__() == f"Название Невыносимо вредный Эдвард Нортон, просмотры {video.viewCount}, лайки {video.likeCount}"
    video1 = Video('12345')
    assert video1.video_id == '12345'
    assert video1.video_info is None
    assert video1.video_title is None
    assert video1.viewCount is None
    assert video1.likeCount is None


def test_PLVideo():
    pl_video = PLVideo('YhVPQLEG4do', 'PLTw6imIlfumxmcC6uUBdbIehnNrPWCkR7')
    pl_info = pl_video.playlist_info
    assert pl_video.playlist_title == 'Взлеты и падения'
    assert pl_video.__str__() == 'Невыносимо вредный Эдвард Нортон, (Взлеты и падения)'
    assert pl_video.playlist_info == pl_info


def test_Playlist(test_playlist):
    playlist, title, link, total_duration, best_video = test_playlist
    assert playlist.playlist_title == title
    assert playlist.playlist_link == link
    assert playlist.total_duration == total_duration
    assert playlist.show_best_video == best_video

import pytest
from class_channel.class_channel import Channel, Playlist


@pytest.fixture
def test_info():
    channel = Channel("UCbaKd4mhqd1QvfDp5EaUlHw")

    return channel.channel_id, channel.channel_info


@pytest.fixture
def test_playlist():
    playlist = Playlist("PLTw6imIlfumzfdAvVcMLYrDJz1uHEOqK4")
    title = playlist.playlist_title
    link = playlist.playlist_link
    total_duration = playlist.total_duration
    best_video = playlist.show_best_video
    return playlist, title, link, total_duration, best_video

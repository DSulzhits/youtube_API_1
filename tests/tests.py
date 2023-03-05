from class_channel.class_channel import Channel


def test_Class(test_info):
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
def test_make_json():
    test_channel = Channel("UCbaKd4mhqd1QvfDp5EaUlHw")
    assert test_channel.make_json(f" test_{test_channel.channel_title}") is None



def test_dander_methods():
    test_channel = Channel("UCbaKd4mhqd1QvfDp5EaUlHw")
    test_channel2 = Channel("UCMCgOm8GZkHp8zJ6l7_hIuA")
    assert test_channel.__repr__() == f"Channel ({test_channel.channel_title}, {test_channel.channel_link})"
    assert test_channel.__str__() == f"Youtube-канал: {test_channel.channel_title}, подписчиков: {test_channel.channel_subscribers}"
    assert test_channel.__gt__(test_channel2) is False
    assert test_channel.__add__(test_channel2) == test_channel.channel_subscribers + test_channel2.channel_subscribers

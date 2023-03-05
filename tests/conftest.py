import pytest
from class_channel.class_channel import Channel


@pytest.fixture
def test_info():
    channel = Channel("UCbaKd4mhqd1QvfDp5EaUlHw")

    return channel.channel_id, channel.channel_info

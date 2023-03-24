from class_channel.class_channel import Channel, Video, PLVideo, Playlist


def main():
    # green_grass = Channel('UCbaKd4mhqd1QvfDp5EaUlHw')
    # info = green_grass.channel_info
    # print(info)
    # print(green_grass.channel_id)
    # print(green_grass.channel_title)
    # print(green_grass.channel_description)
    # print(green_grass.channel_link)
    # print(green_grass.channel_subscribers)
    # print(green_grass.channel_videoCount)
    # print(green_grass.channel_viewCount)
    # green_grass.channel_id = 'Новое название'
    # green_grass.make_json(green_grass.channel_title)
    # vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    # vdud.make_json(vdud.channel_title)
    # print(green_grass)
    # print(vdud)
    # print(green_grass > vdud)
    # print(green_grass < vdud)
    # print(green_grass + vdud)
    # vd = Video('YhVPQLEG4do')
    # print(vd.video_id)
    # pl = Playlist('PLTw6imIlfumzfdAvVcMLYrDJz1uHEOqK4')
    # print(pl.playlist_title)
    # print(pl.playlist_link)
    # duration = pl.total_duration
    # print(duration)
    # print(type(duration))
    # print(duration.total_seconds())
    # print(pl.show_best_video)
    vd_broken = Video('12345')
    print(vd_broken.video_title)
    print(vd_broken.likeCount)


    pass


if __name__ == "__main__":
    main()

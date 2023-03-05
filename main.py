from class_channel.class_channel import Channel

def main():
    green_grass = Channel('UCbaKd4mhqd1QvfDp5EaUlHw')
    # print(green_grass.channel_info)
    # print(green_grass.channel_id)
    # print(green_grass.channel_title)
    # print(green_grass.channel_description)
    # print(green_grass.channel_link)
    # print(green_grass.channel_subscribers)
    # print(green_grass.channel_videoCount)
    # print(green_grass.channel_viewCount)
    # green_grass.channel_id = 'Новое название'
    # green_grass.make_json()
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    # vdud.make_json()
    print(green_grass)
    print(vdud)
    print(green_grass > vdud)
    print(green_grass < vdud)
    print(green_grass + vdud)
    pass



if __name__ == "__main__":
    main()
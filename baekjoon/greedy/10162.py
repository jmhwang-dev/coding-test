def get_microwave_time(sec=100):
    A = 5 * 60
    B = 1 * 60
    C = 10
    micro_waves = [A, B, C]
    button_clicks = []

    for i, wave in enumerate(micro_waves):
        button_clicks.append(sec // micro_waves[i])
        sec = sec % micro_waves[i]
    
    if sec != 0:
        print('-1')
    else:
        print("{} {} {}".format(button_clicks[0], button_clicks[1], button_clicks[2]))

T = int(input())
get_microwave_time(T)

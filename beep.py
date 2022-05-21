import winsound
import time

def three_beeps(frequency, duration):
    for i in range(3):
        winsound.Beep(frequency, duration)
        time.sleep((duration) / 1000)

    time.sleep((duration * 5) / 1000)


def nine_beeps():
    frequency = 2500  # Set Frequency of sound To 2500 Hertz
    duration = 100  # 100 ms ==  0.1 second

    three_beeps(frequency, duration)
    three_beeps(frequency, duration)
    three_beeps(frequency, duration)
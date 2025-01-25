import pygame
import keyboard
import time


def main():
    pygame.init()
    pygame.mixer.music.load("so.mp3")
    pygame.mixer.music.play()

    start_time = time.time()
    timestamps = []

    print("Press SPACE to record a beat, ESC to quit.")

    try:
        while True:
            if keyboard.is_pressed('space'):
                current_time = time.time() - start_time
                timestamps.append(current_time)
                print(f"Beat recorded at {current_time:.3f} sec")
                time.sleep(0.2)
            if keyboard.is_pressed('esc'):
                break
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass
    pygame.mixer.music.stop()

    float_array_str = ", ".join(f"{t:.3f}f" for t in timestamps)
    output_str = f"public float[] beatTimes = {{ {float_array_str} }};"
    print("\n" + output_str)

if __name__ == "__main__":
    main()

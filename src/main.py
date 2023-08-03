from src.visual.baseWindow import BaseWindow


if __name__ == '__main__':
    a = BaseWindow()

    while a.running:
        a.window_loop()

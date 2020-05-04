import threading
import requests
import click
import time
import sqlite3


progress = None


@click.command()
@click.option('--stream_url', default='http://rbb-edge-2070.fra-lg.cdn.addradio.net/rbb/fritz/live/mp3/128/stream.mp3')
@click.option('--filename', default='myRadio.mp3')
@click.option('--duration', default=30)
def record(stream_url, duration, dateiname):
    # click.echo("{}, {}, {}".format(stream_url, duration, filename))
    with open(dateiname, 'wb') as f:
        global progress
        progress = duration
        print_progress()

        response = requests.get(stream_url, stream=True)

        current = time.time()
        target = current + duration
        while current <= target:
            current = time.time()
            c = next(response.iter_content())
            f.write(c)
        response.close()
        print('Done!')
    # print(f'result: {result}')


def print_progress():
    global progress
    if progress >= 1:
        print(progress)
        progress -= 1
        threading.Timer(1.0, print_progress).start()


if __name__ == '__main__':
    record()

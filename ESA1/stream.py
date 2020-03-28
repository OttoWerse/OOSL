import requests
import click
import time
import sqlite3

click.command()
click.argument('stream_url')
click.option('--duration', default=time.time() + 30)
click.option('dateiname', default='myRadio.mp3')


def record(stream_url, duration, dateiname):
    with open(dateiname, 'wb') as f:
        response = requests.get(stream_url, stream=True)

        current = time.time()
        target = current + duration
        while current <= target:
            print(f'Current: {current}, Target: {target}')
            current = time.time()
            c = next(response.iter_content())
            f.write(c)
        response.close()
    # print(f'result: {result}')


if __name__ == '__main__':
    stream_link = 'http://rbb-edge-2070.fra-lg.cdn.addradio.net/rbb/fritz/live/mp3/128/stream.mp3'
    record(stream_link, 5, 'test.mp3')

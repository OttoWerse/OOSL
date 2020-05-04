import threading
import requests
import time
import tkinter
import sqlite3

progress = None


def record(stream_url, duration, filename):
    with open(filename, 'wb') as f:
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
        label_progress['text'] = 'Done!'
        f.close()
    conn = None
    try:
        conn = sqlite3.connect('database.sqlite')
        sql = '''   INSERT INTO recordings(stream_url, duration, filename) 
                    VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (stream_url, duration, filename))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    update_rows()


def print_progress():
    global progress
    if progress >= 1:
        progress -= 1
        label_progress['text'] = f'Recording: {progress} seconds remaining...'
        threading.Timer(1.0, print_progress).start()


def threaded_start():
    th = threading.Thread(target=(start))
    th.start()


def start():
    url = entry_url.get()
    str = entry_duration.get()
    dur = int(str)
    file = 'test.mp3'
    record(url, dur, file)


def update_rows():
    global frame
    conn = None
    try:
        conn = sqlite3.connect('database.sqlite')
        cur = conn.cursor()

        sql = '''SELECT * FROM recordings'''
        cur.execute(sql)
        rows = cur.fetchall()

        frame.destroy()
        new_frame = tkinter.LabelFrame(gui, text="Recordings")

        for row in rows:
            label = tkinter.Label(new_frame, text=row)
            label.pack()

        frame.destroy()
        frame = new_frame
        frame.pack()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_database():
    conn = None
    try:
        conn = sqlite3.connect('database.sqlite')
        cur = conn.cursor()

        sql = ''' CREATE TABLE IF NOT EXISTS recordings(stream_url VARCHAR(200), duration VARCHAR(200), filename VARCHAR(200))'''
        cur.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


gui = tkinter.Tk()
label_welcome = tkinter.Label(gui, text="Audio Recorder v2")
label_welcome.pack()

label_progress = tkinter.Label(gui, text="Not recording")
label_progress.pack()

entry_duration = tkinter.Entry(gui, width=100)
entry_duration.pack()

entry_url = tkinter.Entry(gui, width=100)
entry_url.insert(tkinter.END, 'http://rbb-edge-2070.fra-lg.cdn.addradio.net/rbb/fritz/live/mp3/128/stream.mp3')
entry_url.pack()

button_start = tkinter.Button(gui, text="Start", command=threaded_start)
button_start.pack()

frame = tkinter.LabelFrame(gui, text="Recordings")
frame.pack()

if __name__ == '__main__':
    create_database()
    update_rows()
    gui.mainloop()

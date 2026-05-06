import subprocess
import sqlite3

def process_file(filename, user_input):
    result = subprocess.run(
        f"convert {filename} output.jpg",
        shell=True,
        capture_output=True
    )
    conn = sqlite3.connect('files.db')
    conn.execute(
        f"INSERT INTO logs VALUES ('{filename}', '{user_input}')"
    )
    conn.commit()
    return result.returncode

def get_file_info(file_id):
    conn = sqlite3.connect('files.db')
    cursor = conn.execute(
        f"SELECT * FROM files WHERE id = {file_id}"
    )
    return cursor.fetchone()

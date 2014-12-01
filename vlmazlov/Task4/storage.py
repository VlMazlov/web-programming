__author__ = 'vlmazlov'

from collections import deque
from truncate import truncate

STORAGE_FILE = 'storage.txt'
STORAGE_ENCODING = 'utf-8'
RECENT_ENTRIES_FILE = 'last_entries.txt'
RECENT_ENTRIES_ENCODING = 'utf-8'
RECENT_ENTRIES_NUM = 10

def load_file_content(filename, encoding):
    with open(filename, 'r', encoding=encoding) as file:
        return eval(file.read())


def save_to_file(to_save, filename, encoding):

    import os
    
    with open(os.path.join(os.getcwd(), filename), 'w', encoding=encoding) as file:
        print(repr(to_save), file=file)


def load_storage():
    return load_file_content(STORAGE_FILE, STORAGE_ENCODING)


def load_recent_entries():
    return load_file_content(RECENT_ENTRIES_FILE, RECENT_ENTRIES_ENCODING)

storage_ = load_storage()
recent_entries_ = deque(load_recent_entries())


def save_storage():
    save_to_file(storage_, STORAGE_FILE, STORAGE_ENCODING)

def save_recent_entries():
    save_to_file(recent_entries_, RECENT_ENTRIES_FILE, RECENT_ENTRIES_ENCODING)


def get_value(key):
    return storage_[key]


def add_entry(key, value):
    storage_[key] = value
    save_storage()

    if key in recent_entries_:
        recent_entries_.remove(key)

    if len(recent_entries_) == RECENT_ENTRIES_NUM:
        recent_entries_.pop()

    recent_entries_.appendleft(key)

    save_recent_entries()

def get_recent_entries():
    return ({'long_url': key, 'long_url_truncated': truncate(key), 'short_url': get_value(key)}
            for key in recent_entries_)

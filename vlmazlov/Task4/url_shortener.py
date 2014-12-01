__author__ = 'vlmazlov'

from flask import Flask, request, redirect, render_template, url_for
app = Flask(__name__)

from storage import add_entry, get_recent_entries
from truncate import truncate

SHORTENED_URL_LENGTH = 7

import random
import string


def generate_short_url():
   return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(SHORTENED_URL_LENGTH))


@app.route('/')
def display_home():
    return render_template('home.html', recent_entries=get_recent_entries())


@app.route('/shorten_url', methods=['POST'])
def shorten_url(short_url=generate_short_url):
    long_url = request.form['long_url']

    long_url = long_url.replace('http://', '')

    short_url = request.form['short_url']
    if short_url == '':
        short_url = generate_short_url()

    add_entry(long_url, short_url)
    return redirect(url_for('display_short_url',
                            long_url=long_url, short_url=short_url, long_url_truncated=truncate(long_url)))


@app.route('/dispay_result')
def display_short_url():
    print(request.args)
    return render_template('display_result.html', entry=request.args)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Remote control your totem player
# Author: Yaacov Zamir (2013)

import os, glob
from subprocess import Popen

from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

# Get totem binary file
totem_bin = 'totem'

# Get mp4 files
base_path = os.path.expanduser('~/Downloads')
ls = glob.glob("%s/%s" % (base_path, '*.mp4'))
basenames = [os.path.basename(f) for f in ls]
basename_dict = dict(enumerate(basenames))

# UI web page
@app.route('/')
def index():
    return render_template('index.html')

# API for controlling the binary
@app.route('/api/ls')
def cmd_ls():
    return jsonify(basename_dict)

@app.route('/api/open/<int:n>')
def cmd_open(n):
    file_name = "%s/%s" % (base_path, basename_dict[n])
    Popen([totem_bin, '--fullscreen', file_name])
    return ''

@app.route('/api/cmd/<cmd>')
def cmd(cmd):
    Popen([totem_bin, '--%s' % cmd])
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0')


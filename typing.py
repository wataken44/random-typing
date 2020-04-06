#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" typing.py


"""

import datetime
import json
import os
import random

CHAR_COUNT = 6
TRIAL_COUNT = 5
CHARSET = (
    ' !"#$%&'
    + "'"
    + "()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
)
HISTORY_FILE = os.path.dirname(os.path.abspath(__file__)) + "/" + "history.json"


def main():
    now = datetime.datetime.now()

    print("  hit enter to start")
    input("> ")

    result = []

    for i in range(TRIAL_COUNT):
        result.append(do_trial(i + 1))

    show_result(result)
    write_history(now.isoformat(), result)


def do_trial(index):
    problem = "".join(random.choices(CHARSET, k=CHAR_COUNT))
    print("  %s (%d)" % (problem, index))

    stat = []

    while True:
        st = datetime.datetime.now()
        s = input("> ")
        et = datetime.datetime.now()

        ok = s == problem
        dt = (et - st).total_seconds()

        stat.append([ok, dt])

        if ok:
            break

    return [problem, stat]


def show_result(result):
    print("---------------------------")
    for ret in result:
        print("  %s" % ret[0])
        for data in ret[1]:
            ok = "ng"
            if data[0]:
                ok = "ok"
            print("    %s %s" % (ok, data[1]))


def write_history(name, result):
    history = {}
    if os.path.exists(HISTORY_FILE):
        fp = open(HISTORY_FILE)
        history = json.load(fp)
        fp.close()

    fp = open(HISTORY_FILE, "w")
    history[name] = result
    fp.write(json.dumps(history, indent=4))
    fp.close()


if __name__ == "__main__":
    main()

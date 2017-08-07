# -*- coding: utf-8 -*-

import sys
import os

def guardian(targetstr, ng_patterns):
    """ @param ng_patterns A string list.
    @return None if no matched. """
    contains = []
    for pattern in ng_patterns:
        if targetstr.find(pattern)!=-1:
            contains.append(pattern)
    if contains:
        return contains
    return None

def datetimestrs():
    import datetime
    dows = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    nowdt = datetime.datetime.now()

    date = nowdt.strftime('%Y/%m/%d')
    time = nowdt.strftime('%H:%M:%S')
    dow = dows[nowdt.weekday()]
    nowstr = '%s(%s) %s' % (date, dow, time)

    short_date = nowdt.strftime('%y%m%d')
    short_time = nowdt.strftime('%H%M%S')
    short_dt = '%s-%s' % (short_date, short_time)
    permalinkstr = '<a name="%s"></a>[#](#user-content-%s)' % \
                   (short_dt, short_dt)

    return nowstr, permalinkstr

def file2list(filepath):
    ret = []
    with open(filepath, 'r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, 'w') as f:
        f.writelines(['%s\n' % line for line in ls] )

def is_file(filepath):
    return os.path.isfile(filepath)

def create_file_if_do_not_exists(filepath, contents=None):
    if is_file(filepath):
        return

    if contents==None:
        empty = []
        list2file(filepath, empty)
        return
    list2file(filepath, contents)

def remove_if_exists(filepath):
    if is_file(filepath):
        os.remove(filepath)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--temp', default='temp.txt')
    parser.add_argument('-n', '--ng', default='ng_keywords.txt')
    parser.add_argument('-o', '--out', default=None, required=True)

    parsed_args = parser.parse_args()
    return parsed_args

selfdir = os.path.abspath(os.path.dirname(__file__))

args = parse_arguments()
outpath = args.out

tempfilepath = os.path.join(selfdir, args.temp)
ngfilepath = os.path.join(selfdir, args.ng)
remove_if_exists(tempfilepath)

empty = []
list2file(tempfilepath, empty)
print '[TwDD_WRITER (1/3)] editing...'
os.system(tempfilepath)

contents = file2list(tempfilepath)
if len(contents)==0:
    exit(1)

tweet = contents[0]
if tweet=='t' or tweet=='tweet':
    os.system('start "" %s' % outpath)
    exit(1)

print '[TwDD_WRITER (2/3)] checking NG keywords...'
if is_file(ngfilepath):
    ng_keywords = [line for line in file2list(ngfilepath) if len(line)>0]
    matched_ng = guardian(tweet, ng_keywords)
    if matched_ng:
        print 'Error! There are NG Keywords.'
        print matched_ng
        os.system('pause')
        exit(1)
else:
    print 'skipped.'

print '[TwDD_WRITER (3/3)] writing...'

nowstr, permalinkstr = datetimestrs()
tweet = '- %s %s %s' % (permalinkstr, nowstr, tweet)

in_enc = 'utf-8'
out_enc = 'utf-8'

create_file_if_do_not_exists(outpath)

lines = file2list(outpath)

try:
    real_tweet = tweet.decode(in_enc).encode(out_enc)
except (UnicodeEncodeError, UnicodeDecodeError):
    print 'Encoding error!'
    os.system('start "" %s' % tempfilepath)
lines.insert(0, real_tweet)

list2file(outpath, lines)

print 'fin.'
exit(0)
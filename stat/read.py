import os
import sys
import json
import time

from datetime import datetime

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pipenv run jupyter notebook
# python read.py e:\nohup.out

lineCount = 0
recordCount = 0
pack = []

def read_record(logFile):
    global lineCount
    with open(logFile) as f:
        for line in f:
            # print('line...' + line)
            try:
                record = json.loads(line)
                yield record
            except:
                yield None
            finally:
                lineCount = lineCount + 1

def analysis():
    frame = DataFrame(pack)
    # print(frame['channel'])
    # print(frame['channel'].value_counts()[:10])
    counts = frame['channel'].value_counts()
    print(counts[:10])
    counts[:10].plot(kind="barh", rot=0)
    plt.show()

if __name__ == '__main__':
    inputFile = sys.argv[1]
    i = 0

    ts = time.time()

    try:
        for record in read_record(inputFile):
            if record and len(record) == 1:
                recordCount = recordCount + 1
                pack.append(record[0])
                # if 'timestamp' in record[0]['data']:
                #     sql = "INSERT INTO signal(channel, detail, ts) VALUES(%s, %s, %s)"
                #     print(json.dumps(record[0]['data']))
                #     cursor.execute(sql, (record[0]['channel'], json.dumps(record[0]['data']), datetime.fromtimestamp(record[0]['data']['timestamp'] / 1e3)))
                # else:
                #     sql = "INSERT INTO signal(channel, detail) VALUES(%s, %s)"
                #     print(json.dumps(record[0]['data']))
                #     cursor.execute(sql, (record[0]['channel'], json.dumps(record[0]['data'])))
                if recordCount > 200000:
                    print('Read - records %s in number of lines %s, duration: %s seconds' % (recordCount, lineCount, time.time() - ts))
                    break
    except:
        pass
    finally:
        analysis()
                
import os
import sys
import json

from datetime import datetime
import psycopg2




lineCount = 0
recordCount = 0
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

if __name__ == '__main__':
    inputFile = sys.argv[1]
    i = 0
    conn = psycopg2.connect(database="exnet-data", user="postgres", password="nhn!23nhn", host="127.0.0.1", port="5432")
    cursor = conn.cursor()

    for record in read_record(inputFile):
        if record and len(record) == 1:
            recordCount = recordCount + 1
            if 'timestamp' in record[0]['data']:
                sql = "INSERT INTO signal(channel, detail, ts) VALUES(%s, %s, %s)"
                print(json.dumps(record[0]['data']))
                cursor.execute(sql, (record[0]['channel'], json.dumps(record[0]['data']), datetime.fromtimestamp(record[0]['data']['timestamp'] / 1e3)))
            else:
                sql = "INSERT INTO signal(channel, detail) VALUES(%s, %s)"
                print(json.dumps(record[0]['data']))
                cursor.execute(sql, (record[0]['channel'], json.dumps(record[0]['data'])))
            # if recordCount > 100:
            #     print('break', recordCount)
            #     break
            print("OK....", record[0])
    conn.commit()
    conn.close()
                
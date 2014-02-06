# coding:utf-8


import sqlite3
import codecs
import os



def main(db_path, store_path):

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    select datetime(timestamp,"unixepoch","localtime"), author, body_xml from Messages;
    """
    store_file = os.path.join(store_path, "skype-message.tsv")
    fo = codecs.open(store_file, "wb", "utf-8")

    cur.execute(sql)
    for c in cur:
        line = c[0]
        line += r"/t"
        line += c[1]
        line += r"/t"
        line += unicode(c[2])
        fo.write(line)

    fo.close()

if __name__ == '__main__':
    db_path = r"./main-20140206-1802.db"
    store_path = r"."

    main(db_path, store_path)

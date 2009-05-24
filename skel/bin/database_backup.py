#!/usr/bin/env python

import datetime
import os

from subprocess import Popen, PIPE

from boto.s3.connection import S3Connection
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = '$$$$AWS_ACCESS_KEY_ID$$$$'
AWS_SECRET_ACCESS_KEY = '$$$$AWS_SECRET_ACCESS_KEY$$$$'
DUMP_CMD = ['pg_dump', '-h$$$$PROD_DATABASE_HOST$$$$', '-p5432', '-Upostgres', '$$$$PROJECT_NAME$$$$']

def backup_db():
    path = '/var/database_backups/$$$$PROJECT_NAME$$$$/%s.sql.bz' % (datetime.date.today(),)
    f = open(path, 'wb')
    p1 = Popen(DUMP_CMD, stdout=PIPE)
    p2 = Popen(['bzip2'], stdin=p1.stdout, stdout=f)
    p2.communicate()
    f.close()
    return path

def upload_to_s3(path):
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket('$$$$PROJECT_NAME$$$$-backup')
    k = Key(bucket)
    k.key = os.path.basename(path)
    k.set_contents_from_filename(path)

def main():
    path = backup_db()
    upload_to_s3(path)

if __name__ == '__main__':
    main()
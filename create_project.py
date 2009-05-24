#!/usr/bin/env python

import os
import random

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
BLACKLIST = (
    'jquery',
    '.tar.gz',
    'admin/css',
    'admin/img',
    'admin/js',
    '/.git/'
)

def replace(repl, text):
    text = text.replace('/gitignore', '/.gitignore')
    for key, value in repl.iteritems():
        text = text.replace('$$$$%s$$$$' % (key,), value)
    return text

def main():
    repl = {}
    pn = raw_input('Project name: ')
    repl['PROJECT_NAME'] = pn
    
    repl['DEV_DATABASE_HOST'] = raw_input('Development Database host (e.g. dev.%s.com): ' % (pn,))
    if not repl['DEV_DATABASE_HOST']:
        repl['DEV_DATABASE_HOST'] = 'dev.%s.com' % (pn,)
    
    repl['PROD_DATABASE_HOST'] = raw_input('Production Database host (e.g. db.%s.com): ' % (pn,))
    if not repl['PROD_DATABASE_HOST']:
        repl['PROD_DATABASE_HOST'] = 'db.%s.com' % (pn,)
    
    repl['DEV_APP_HOST'] = raw_input('Development app host (e.g. dev.%s.com): ' % (pn,))
    if not repl['DEV_APP_HOST']:
        repl['DEV_APP_HOST'] = 'dev.%s.com' % (pn,)
    
    repl['PROD_APP_HOST'] = raw_input('Production app host (e.g. %s.com): ' % (pn,))
    if not repl['PROD_APP_HOST']:
        repl['PROD_APP_HOST'] = '%s.com' % (pn,)
    
    repl['AWS_ACCESS_KEY_ID'] = raw_input('AWS access key id: ')
    repl['AWS_SECRET_ACCESS_KEY'] = raw_input('AWS secret access key: ')
    repl['NAME'] = raw_input('Your name: ')
    repl['EMAIL_ADDRESS'] = raw_input('Email address: ')
    repl['SECRET_KEY'] = ''.join([random.choice(CHARS) for i in xrange(50)])
    
    dest_dir = raw_input('Destination directory (currently at %s): ' % (os.getcwd(),))
    dest = os.path.join(dest_dir, repl['PROJECT_NAME'])
    os.makedirs(dest)
    
    for root, dirs, files in os.walk('./skel/'):
        for filename in files:
            source_fn = os.path.join(root, filename)
            dest_fn = replace(repl, os.path.join(dest, root.replace('./skel/', ''), replace(repl, filename)))
            try:
                os.makedirs(os.path.dirname(dest_fn))
            except OSError:
                pass
            print 'Copying %s to %s' % (source_fn, dest_fn)
            should_replace = True
            for bl_item in BLACKLIST:
                if bl_item in dest_fn:
                    should_replace = False
            data = open(source_fn, 'r').read()
            if should_replace:
                data = replace(repl, data)
            open(dest_fn, 'w').write(data)

if __name__ == '__main__':
    main()
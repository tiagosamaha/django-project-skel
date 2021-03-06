#!/usr/bin/env python

import os, random, subprocess

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
    
    # repl['DEV_APP_HOST'] = raw_input('Development app host (e.g. dev.%s.com): ' % (pn,))
    # if not repl['DEV_APP_HOST']:
    #     repl['DEV_APP_HOST'] = 'dev.%s.com' % (pn,)
    
    # repl['NAME'] = raw_input('Your name: ')
    # repl['EMAIL_ADDRESS'] = raw_input('Email address: ')
    repl['NAME'] = 'David Wolever'
    repl['EMAIL_ADDRESS'] = 'david@wolever.net'
    
    repl['SECRET_KEY'] = ''.join([random.choice(CHARS) for i in xrange(50)])
    
    dest_dir = raw_input('Destination directory (currently at %s): ' % (os.getcwd(),))
    dest = os.path.join(dest_dir, repl['PROJECT_NAME'])
    os.makedirs(dest)
    
    skeldir = os.path.join(os.path.dirname(__file__), 'skel')
    for root, dirs, files in os.walk(skeldir):
        for filename in files:
            source_fn = os.path.join(root, filename)
            source_rel_fn = root.replace(skeldir, '')
            source_rel_fn = source_rel_fn.lstrip("/")
            dest_rel_fn = os.path.join(source_rel_fn, replace(repl, filename))
            dest_fn = replace(repl, os.path.join(dest, dest_rel_fn))
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
            os.chmod(dest_fn, os.stat(source_fn)[0])

    print "Done!"
    print "Run %s/setup/setup.sh to setup the environment." %(dest)

if __name__ == '__main__':
    main()

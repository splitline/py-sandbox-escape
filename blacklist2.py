def make_secure():
    Q____Q = ['open',
              'file',
              'execfile',
              'compile',
              #   'reload',
              '__import__',
              'eval',
              'input',
              # and anything you want
              ]
    for func in Q____Q:
        del __builtins__.__dict__[func]


make_secure()


while True:
    try:
        inp = raw_input("> ")
        ret = None
        exec "ret=" + inp
        if ret != None:
            print ret

    except Exception, e:
        print 'Exception:', e


def check_secure(inp):
    Q____Q = [
            'exec',
            'open',
            'file',
            'execfile',
            'import',
            'eval',
            'input',
            'hacker'
            # and anything you want
    ]
    for s in Q____Q:
        if s in inp:
            raise Exception("Sorry, '"+ s +"' is not allowed.")

while True:
    try:
        inp = raw_input("> ")
        check_secure(inp)
        ret = None
        exec "ret=" + inp
        if ret != None:
            print ret

    except Exception, e:
        print 'Exception:', e
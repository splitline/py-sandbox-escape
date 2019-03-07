def make_secure():
    Q____Q = __builtins__.__dict__.keys()
    Q____Q.remove('raw_input')
    Q____Q.remove('print')
    for x in Q____Q:
        del __builtins__.__dict__[x]
    


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

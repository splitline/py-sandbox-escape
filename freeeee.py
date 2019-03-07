while True:
    try:
        inp = raw_input("> ")
        ret = None
        exec "ret=" + inp
        if ret != None:
            print ret
    except Exception, e:
        print 'Exception:', e
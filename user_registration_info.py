import c4d

def main():
    si = c4d.GeGetSerialInfo(c4d.SERIALINFO_MULTILICENSE)
    if len(si['nr']) > 0:
        # Multi-license, do something
        print "Multi-license"
        print si
    else:
        si = c4d.GeGetSerialInfo(c4d.SERIALINFO_CINEMA4D)
        print "Single-license"
        print si
        # Single-license, do something

if __name__=='__main__':
    main()
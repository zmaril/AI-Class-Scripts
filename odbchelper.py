def buildConnectionString(params):
    """Build a connectiong string from a dictionary of parameters. 

    Returns string."""
    return ";".join(["%s=%s" % (k,v) for k,v in params.items()])

if __name__== "__main__":
    myParams ={"server":"mpligrim",\
                  "database":"master",\
                  "uid": "sa",\
                  "pwd":"secret" \
                  }
    print buildConnectionString(myParams)
              
    
def fib(n):
    print 'n = ', n
    if n >1:
        return n * fib(n-1)
    else: 
        print 'end of the line'
        return 

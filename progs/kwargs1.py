def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s = %s" %(key,value)
 
greet_me(id=1,name="shashi",location="Hyderabad")
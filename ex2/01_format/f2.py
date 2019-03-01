a1 = "this is %s,who is my %s" % ('htb', "myself")
a2 = "this is {},who is my {}".format("htb", "myself")

a3 = "this is {0},who is my {1}".format("htb", "myself")
a4 = "this is {1},who is my {0}".format("myself", "htb")

a5 = "this is {who},who is my {whose}".format(who="htb", whose="myself")
print 'a1 is ', a1
print 'a2 is ', a2
print 'a3 is ', a3
print 'a4 is ', a4
print 'a5 is ', a5

class DayName:

    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = DayName("Mon")
e2 = DayName("Tue")
e3 = DayName("Wed")
e4 = DayName("Thurs")

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4

this = e1

while this:
    print(this.dataval)
    this=this.nextval

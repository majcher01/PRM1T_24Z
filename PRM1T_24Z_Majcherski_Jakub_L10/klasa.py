class PhoneBook:
    def __init__(this,id):
        this.id=str(id)
        this.data=dict()

    def add_record(this,user,number):
        assert isinstance(number,str)
        this.data[user]=number
    
    def show_records(this):
        for i in this.data:
            print(str(i),":",str(this.data[i]))
   #Zadanie2 
    def __str__(this):
        return f"{this.data}{this.id}"

    def __eq__(this,other):
        assert isinstance(other, PhoneBook)
        if(this.id==other.id and this.data==other.data):
            return True
        else:
            return False
    def __gt__(this,other):
        assert isinstance(other,PhoneBook)
        if(len(this.data)>len(other.data)):
            return True
        else:
            return False
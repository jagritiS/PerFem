class Users:
    def __init__(self,start_date,enddate,cycle_length,phone,password,dob):
        self.__start_date = ""
        self.__enddate = ""
        self.__cycle_length = ""
        self.__phone = ""
        self.__password = ""
        self.__dob = ""
    def getstart_date(self):
        return self.__start_date
    def setstart_date(self,start_date):
        self.__start_date = start_date

    def getenddate(self):
        return self.__enddate
    def setenddate(self,enddate):
        self.__enddate = enddate

    def getcycle_length(self):
        return self.__cycle_length
    def setcycle_length(self,addr):
        self.__cycle_length = addr

    def getPassword(self):
        return self.__password
    def setPassword(self,pasw):
        self.__password = pasw

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
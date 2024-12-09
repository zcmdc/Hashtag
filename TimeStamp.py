class TimeStamp:
    def __init__(self,timeStamp):
        self.timeStamp = timeStamp
    
        tokens = self.timeStamp.split("T")
        self.day = tokens[0]
        time = tokens[1]
        
        dayToken = self.day.split("-")
        self.year = dayToken[0]
        self.month = dayToken[1]
        self.day = dayToken[2]

        timeToken = time.split(":")
        self.hour = timeToken[0]
        self.min = timeToken[1]
        self.sec = timeToken[2]
        self.sec = self.sec.replace("Z","")


# AppointmentBook ADT implementation
class AppointmentBook:
    '''
    Fields:
    date (Int); date of appointment in single year, from 1 to 365 days
    time (Float); time of makingappointment b/t 8AM-5PM mod 24,
    hence last appointment is at 4:30PM (or 16.5) in full or half clock hours
    purpose (Str); purpose of appointent
    Requires: 1 <= date <= 365 (one calender year)
              8.0 <= time <= 16.5 (at full or half clock) since hours of operations
              is from 8AM to 5PM. (ie. 8.0 for 8AM and 16.5 for 4:30PM)
    '''
    
    ## AppointmentBook() creates an empty appointment book.
    ## Effect: creates an an empty appointment book
    ##__init__: None -> AppointmentBook
    def __init__(self):
        self._book = list ()
        
    ## self == other produces True if self and other (which are both AppointmentBook class
    ## objects) are equal and False otherwise
    ## __eq__: AppointmentBook AppointmentBook -> Bool
    ## Requires: self and other to be both an AppointmentBook class object
    def __eq__(self,other):
        return self._book == other._book
            
        
    ## show(self) produces the list of appointments that are currently in
    ## the AppointmentBook object.  If there are no appointments,an empty
    ## list is returned.
    ## show: AppointmentBook -> listof (listof Int Float Str)
    def show (self):
        lst = []
        for i in range(len(self._book)):
            lst.append(self._book[i])
        return lst
    
    
    ## isAppointment(self, apptDate, apptTime) produces True if an appointment exists
    ## for the date and time specified, and False otherwise.
    ## isAppointment: AppointmentBook Int Float -> Bool
    ## Requires: 1 <= apptDate <= 365
    ##           8.0 <= apptTime <= 16.5 (and half or full clock hours)
    def isAppointment(self, apptDate, apptTime):
        assert 1 <= apptDate <= 365 , "Out of calender year date range, 1-365 days"
        assert 8.0 <= apptTime <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
        assert apptTime % 1 == 0.0 or apptTime % 1 == 0.5, "apptTime not in half or full clock hours" 
        haveappt = []
        for i in range(len(self._book)):
            if self._book[i][0] == apptDate and self._book[i][1] == apptTime:
                haveappt.append(True)
            else:
                haveappt.append(False)
        return True in haveappt

        
    
    ## makeAppointment(self,apptDate,apptTime,purpose) inserts the appointment for the date
    ## time and purpose specified as long as it does not conflict with an existing
    ## appointment (two appointments scheduled at the same date and time) and 
    ## produces True upon success, False otherwise.
    ## Effect: Upon successful insertion of appointment, mutates AppointmentBook
    ##          object by adding in new appointment entry with specified date,
    ##          time and purpose
    ## makeAppointment: AppointmentBook Int Float Str -> Bool
    ## Requires: 1 <= apptDate <= 365
    ##           8.0 <= apptTime <= 16.5 (and half or full clock hours)
    def makeAppointment(self, apptDate, apptTime, purpose):
        assert 1 <= apptDate <= 365 , "Out of calender year date range, 1-365 days"
        assert 8.0 <= apptTime <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
        assert apptTime % 1 == 0.0 or apptTime % 1 == 0.5, "apptTime not in half or full clock hours" 
        if self.isAppointment(apptDate,apptTime) == True:
            return False
        else: 
            self._book.append([apptDate,apptTime,purpose])
            return True
            
        
    ## cancelAppointment(self,apptDate,apptTime) deletes the appointment for the date
    ## and time specified. Returns True, and appointment is successfully deleted 
    ## if there is an existing appointment at the date and time specified. 
    ## Otherwise, False is returned.
    ## Effect: Upon successful deletion of appointment, mutates AppointmentBook object
    ## by removing existing appointment entry with specified date and time.
    ## cancelAppointment: AppointmentBook Int Float -> Bool
    ## Requires: 1 <= apptDate <= 365
    ##           8.0 <= apptTime <= 16.5 (and half or full clock hours)
    def cancelAppointment(self, apptDate, apptTime):
        assert 1 <= apptDate <= 365 , "Out of calender year date range, 1-365 days"
        assert 8.0 <= apptTime <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
        assert apptTime % 1 == 0.0 or apptTime % 1 == 0.5, "apptTime not in half or full clock hours" 
        if self.isAppointment(apptDate,apptTime) == False:
            return False
        else:
            ndx = 0
            for i in range(len(self._book)):
                if self._book[i][0] == apptDate and self._book[i][1] == apptTime:
                    ndx = ndx + i
            self._book.pop(ndx)
            return True
        
            
    ## checkAppointment(self,apptDate,apptTime) retrieves the purpose of the 
    ## appointment at the given date and time, if one exists. Otherwise,
    ## returns a Null string.
    ## checkAppointment: AppointmentBook Int Float -> (anyof Str None)
    ## Requires: 1 <= apptDate <= 365
    ##           8.0 <= apptTime <= 16.5 (and half or full clock hours)
    def checkAppointment(self, apptDate, apptTime):
        assert 1 <= apptDate <= 365 , "Out of calender year date range, 1-365 days"
        assert 8.0 <= apptTime <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
        assert apptTime % 1 == 0.0 or apptTime % 1 == 0.5, "apptTime not in half or full clock hours"         
        if self.isAppointment(apptDate,apptTime) ==  False:
            return None
        else:
            ndx = 0
            for i in range(len(self._book)):
                if self._book[i][0] == apptDate and self._book[i][1] == apptTime:
                    ndx = ndx + i
            return self._book[ndx][2]
                
                       
    ## changeAppointment(self,oldDate,oldTime,newDate,newTime) change the date
    ## or time for an appointment.  Returns True if successful, other False.
    ## Effects: Upon successful change of oldDate, oldTime to newDate, newTime
    ##          mutates AppointmentBook object by changing the existing 
    ##          appointment to newDate and newTime and also will print 
    ##          a message "Your appointment has been rescheduled to ... at ..."
    ##          Upon unsuccessful change, will print a message "You do not have
    ##          an appointment on ... at ..." if you don't have an appointment at
    ##          the given oldDate and oldTime
    ##          Upon unsuccessful change, will print a message "You already 
    ##          have an appointment on ... at ..." if there is already an
    ##          appointment at newDate and newTime
    ## changeAppointment: AppointmentBook Int Float Int Float -> Bool
    ## Requires: 1 <= oldDate <= 365
    ##           1 <= newDate <= 365
    ##           8.0 <= oldTime <= 16.5(and half or full clock hours)
    ##           8.0 <= newTime <= 16.5 (and half or full clock hours)
    def changeAppointment(self, oldDate, oldTime, newDate, newTime):
        assert 1 <= oldDate <= 365 , "Out of calender year date range, 1-365 days"
        assert 1 <= newDate <= 365 , "Out of calender year date range, 1-365 days"
        assert 8.0 <= oldTime <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
        assert 8.0 <= newTime <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
        assert oldTime % 1 == 0.0 or oldTime % 1 == 0.5, "oldTime not in half or full clock hours"      
        assert newTime % 1 == 0.0 or newTime % 1 == 0.5, "newTime not in half or full clock hours"    
        if self.isAppointment(oldDate,oldTime) == False:
            print (" You do not have an appointment on {0} at {1}".format(oldDate,oldTime))
            return False
        elif self.isAppointment(newDate,newTime) == True:
            print (" You already have an appointment on {0} at {1}".format(newDate,newTime))
            return False
        else: 
            ndx = 0
            for i in range(len(self._book)):
                if self._book[i][0] == oldDate and self._book[i][1] == oldTime:
                    ndx = ndx + i
            self._book[ndx][0] = newDate
            self._book[ndx][1] = newTime
            print ("Your appointment has been rescheduled to {0} at {1}".format(newDate,newTime))
            return True
    
    ## getAppointmentByDate(self,date) retrieves all the appointments on the 
    ## given date. Returns a list of tuples containing time and purpose ordered
    ## so that earlier appointments come before later appointments.
    ## If there is no appointment on the date, an empty list returns.
    ## getAppointments: AppointmentBook Int -> (listof anyof (Tupleof Float Str)  None)
    ## Requires: 1 <= date <= 365
    def getAppointmentsByDate(self, date):
        assert 1 <= date <= 365 , "Out of calender year date range, 1-365 days"
        lst = []
        for i in range(len(self._book)):
            if self._book[i][0] == date:
                lst.append((self._book[i][1],self._book[i][2]))
        return sorted(lst)
        
    
    
        
        

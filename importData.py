from appointmentADT import AppointmentBook
import check

## buildApptBook(apptFile) reads in a text file "appointment.txt" and uses
## the AppointmentBook ADT to build an AppointmentBook
## Effects: Builds an AppointmentBook object by reading an appointment record file
##          If the line is to "Make" Upon successful insertion of appointment
##          mutates AppointmentBook object by adding in new appointment
##          entry with specified date, time and purpose
##          If the line is to "Cancel", Upon successful deletion of appointment,
##          mutates AppointmentBook object by removing existing appointment 
##          entry with specified date and time.    
##          If the line is to "Change", upon successful mutates AppointmentBook 
##          object by changing the existing 
##          appointment to newDate and newTime and also will print 
##          a message "Your appointment has been rescheduled to ... at ..."
##          Upon unsuccessful change, will print a message "You do not have
##          an appointment on ... at ..." if you don't have an appointment at
##          the given oldDate and oldTime
##          Upon unsuccessful change, will print a message "You already 
##          have an appointment on ... at ..." if there is already an
##          appointment at newDate and newTime
## buildApptBook: (.txt file) -> AppointmentBook
## Requires: apptFile to be an appointment record .txt file
##           Also requires that file being accessed is in the same folder as the
##           program using it (ie. this program)
## Example1:
## given txt file 'appointment.txt' with entries:
## Make	45	10.5	meeting
## Cancel	80	14.5
## Change	80	15	85	15
## Make	120	12	discussion
## Make	100	18	consulting
## will return AppointmentBook object without making mutations to AppointmentBook 
## object for line 2, 3 and 5
## Example 2:
## given txt file 'appointment2.txt' with entries:
##
## will return AppointmentBook object without making any mutations to AppointmentBook
## object.
## Example 3: 
## given txt file 'appointment3.txt' with entries:
## Make	400	8.0	cleaning
## Make	365	7.5	brushing
## Cancel	11	11.0	
## Change	400	8.0	100	8.5
## will return AppointmentBook object without making any mutations to AppointmentBook
## object.
## Example 4:
## given txt file 'appointment4.txt' with entries:
## Make	21	8.5	brushing
## Make	23	9.0	dental
## Make	144	11.0	flossing
## Make	298	13.5	meeting
## Cancel	21	8.5
## Cancel	298	13.5	21	8.5
## will return AppointmentBook object making mutations to AppointmentBook object
## for each line
def buildApptBook(apptFile):
    record = AppointmentBook()
    file = open (apptFile,"r")
    action = file.readline().split()
    while (action != []):
        if action[0] == "Make":
            try:
                assert 1 <= int(action[1]) <= 365 , "Out of calender year date range, 1-365 days"
                assert 8.0 <= float(action[2]) <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
                assert float(action[2]) % 1 == 0.0 or float(action[2]) % 1 == 0.5, "apptTime not in half or full clock hours" 
                record.makeAppointment(int(action[1]),float(action[2]),action[3])
            except AssertionError:
                action = file.readline().split()
        elif action[0] == "Cancel":
            try:
                assert 1 <= int(action[1]) <= 365 , "Out of calender year date range, 1-365 days"
                assert 8.0 <= float(action[2]) <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
                assert float(action[2]) % 1 == 0.0 or float(action[2]) % 1 == 0.5, "apptTime not in half or full clock hours"                 
                record.cancelAppointment(int(action[1]),float(action[2]))
            except AssertionError:
                action = file.readline().split
        elif action[0] == "Change":
            try:
                assert 1 <= int(action[1]) <= 365 , "Out of calender year date range, 1-365 days"
                assert 1 <= int(action[3]) <= 365 , "Out of calender year date range, 1-365 days"
                assert 8.0 <= float(action[2]) <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
                assert 8.0 <= float(action[4]) <= 16.5, "Appointment time out of range, Hours of operation between 8AM-5PM mod 24" 
                assert float(action[2]) % 1 == 0.0 or float(action[2]) % 1 == 0.5, "oldTime not in half or full clock hours"      
                assert float(action[4]) % 1 == 0.0 or float(action[4]) % 1 == 0.5, "newTime not in half or full clock hours"                             
                record.changeAppointment(int(action[1]),float(action[2]),\
                                     int(action[3]),float(action[4]))
            except AssertionError:
                action = file.readline().split()
        else:
            action = file.readline().split()
        action = file.readline().split()
    file.close()
    return record

## Tests

#Test_1
test1 = AppointmentBook()
test1.makeAppointment(45,10.5,'meeting')
test1.makeAppointment(120,12,'discussion')
check.expect('Q2T1',buildApptBook('appointment.txt'),test1)

#Test_2
test2 = AppointmentBook()
check.expect('Q2T2',buildApptBook('appointment2.txt'),test2)
    
#Test3
test3 = AppointmentBook()
test3.makeAppointment(21,8.5,'brushing')
test3.makeAppointment(23,9.0,'dental')
test3.makeAppointment(144,11.0,'flossing')
test3.makeAppointment(298,13.5,'meeting')
test3.cancelAppointment(21,8.5)
test3.changeAppointment(298,13.5,21,8.5)
check.expect('Q2T3',buildApptBook('appointment3.txt'),test3)

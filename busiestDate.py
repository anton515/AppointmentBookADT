
from appointmentADT import AppointmentBook
import check


## busiestDate(apptBook) returns a list containing the date(s) that have the largest
## number of appointments in ascending order from an AppointmentBook.
## The busiest dates in an empty AppointmentBook is an empty list.
## busiestDate: AppointmentBook -> (listof Int)
## Requires: apptBook to be an AppointmentBook 
## Example1:
## An empty AppointmentBook
## busiestDate(apptBook) => []
## Example2:
## AppointmentBook with one appointment on Date 200
## busiestDate(apptBook) => [200]
## Example3:
## AppointmentBook with three appointments on Date 10, three on Date 11,
## three on Date 365 and one on Date 12
## busiestDate(apptBook) => [10,11,365]
## Example 4:
## AppointmentBook with two appointments on Date 199 and one on Date 255
## busiestDate(apptBook) => [199]

def busiestDate(apptBook):
    largest = []
    listofdatecount = []
    for i in range(1,366):
        count = len(apptBook.getAppointmentsByDate(i))
        if count != 0:
            listofdatecount.append([i,count])
    if listofdatecount == []:
        return []
    else:
        noappts = []                       
        for j in range(len(listofdatecount)):
            noappts.append(listofdatecount[j][1])
        maxcount = max (noappts)
        for k in range(len(listofdatecount)):
            if listofdatecount[k][1] == maxcount:
                largest.append(listofdatecount[k][0])
    return largest
                                           
## Tests

#test1, empty Appointment Book
test1 = AppointmentBook()
check.expect('Q3T1',busiestDate(test1),[])

#test3, AppointmentBook with one appointment on Date 200
test2 = AppointmentBook()
test2.makeAppointment(200,14.0,'1')
check.expect('Q3T2',busiestDate(test2),[200])


#test3, AppointmentBook with three appointments on Date 10, three on Date 11,
#three on Date 365 and one on Date 12
test3 = AppointmentBook()
test3.makeAppointment(11,12,'1')
test3.makeAppointment(365,8,'1')
test3.makeAppointment(365,10,'1')
test3.makeAppointment(10,11,'1')
test3.makeAppointment(365,9,'1')
test3.makeAppointment(10,12,'1')
test3.makeAppointment(11,10,'1')
test3.makeAppointment(11,11,'1')
test3.makeAppointment(10,10,'1')
test3.makeAppointment(12,12,'1')
check.expect('Q3T3',busiestDate(test3),[10,11,365])

#test4, AppointmentBook with two appointments on Date 199 and one on Date 255
test4 = AppointmentBook()
test4.makeAppointment(199,10,'1')
test4.makeAppointment(255,14,'1')
test4.makeAppointment(199,15,'1')
check.expect('Q3T4',busiestDate(test4),[199])
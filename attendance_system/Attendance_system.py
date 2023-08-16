

def attendance():
    
    while True:
        from time import sleep
        import time
        from datetime import date
        name=input('Enter name ')
        staff_id=input('Enter name ')
        todays_date=date.today()
        with open('Attendance.txt','a') as file:
            file.write("Name: {} Staff ID:{} Date:{} Time: {} \n".format(name,staff_id,todays_date.strftime("%d/%m/%Y"),time.strftime("%I:%M:%S")))
        sleep(5)
def main():
    attendance()

if __name__=="__main__":
    main()            
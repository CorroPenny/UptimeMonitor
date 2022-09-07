from time import sleep
import yagmail
from ping3 import ping
from datetime import datetime



# variables
fromy = "FROM EMAIL"
passy = "FROM EMAIL APP PASSWORD"
to = "YOUR EMAIL HERE"
subject = ""
body = ""
ipToPing = "YOUR IP OR WEBSITE HERE"
now = datetime.now()
current_time = now.strftime("%H:%M")
fails = 0
pingInt = 60
pingIntAfterFail = 10
failsBeforeEmail = 5



# block to actually send the email
def sendemail(sub, bod):
    yag = yagmail.SMTP(fromy, passy)
    yag.send(to, sub, bod)




with open("PingTestFile.txt", "w") as f:
    f.write("")
with open("PingTestFile.txt", "a") as f:
    f.write("Beginning Ping at " + current_time)





def main():
    global fails

    while True:
        # try pinging the machine
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try:
            pingy = ping(ipToPing)  # Returns delay in seconds.
            ms = pingy * 1000        
            print("Ping time: " + str(int(ms)) + " ms at: " + current_time)
            with open("PingTestFile.txt", "a") as f:
                f.write("\nSuccessful Ping at " + current_time)
            fails = 0
            sleep(pingInt)
            
        # if ping fails
        except:
            print("Machine Offline")
            with open("PingTestFile.txt", "a") as f:
                f.write("\n\nFAILED PING at " + current_time)
            sleep(pingIntAfterFail)

            fails = fails + 1 # number of times ping has failed

            if fails >= failsBeforeEmail:
                # sendemail (subject, body)
                print("Sent Email")
                with open("PingTestFile.txt", "a") as f:
                    f.write("\n\nSENT EMAIL at: " + current_time)
                sendemail("PING FAILED", "Pinging " + ipToPing + " yielded a failure at " + current_time + ". Verify connection.")
                fails = 0

            else:

                main()

        

main()

import pywhatkit as kit
from plyer import notification as notify


print('''                                ## Menu ##
      
          To search ->                    search
          To get information ->           info
          To youtube play ->              play
          To shutdown ->                  shutdown
          To cancel shutdown ->           cancel
          To send message on whatsapp ->  sendwhatmsg
          To send imageg in whatsapp ->   sendimg
          To get whatsapp sent history -> history
      \n''')

while True:

    func = input("Enter operation!: ")

    if (func == "search" or func == "info" or func=="play"):
        query = input("Enter Query to search!:   ")

    elif func == "sendwhatmsg":
        Phone_no = input("Enter phone number with '+91'!:  ")
        msg = input("Enter message to send!:  ")
        hours = int(input("Enter hour!:  "))
        mins = int(input("Enter Minutes!:  "))
        
    elif func == "shutdown" :
        T = int(input("Enter time to shutdown in 'second'!:   "))

    elif func == "sendimg" or func == "sendfile":
        Phone_no = input("Enter phone number with '+91'!:  ")
        file = input("Enter img/file path! (formate: D:folder1/folder2/file):  ")
        msg = input("Enter message to send!:  ")
        # hours = int(input("Enter hour!:  "))
        # mins = int(input("Enter Minutes!:  "))
        
    elif func =="cancel":
        pass
    else:
        print("you have entered nothing!")
        print("please try again!! ")
        



    match func:
        case "search" :
            try:
                kit.search(query)
                print("\nDone!!!\n")
            
                notify.notify(title="Google Search!" , message ="Searching completed" , timeout = 4)
                
            except:
                print("Something is wrong!!!\n")
                
        case "play" :
                
            try:
                notify.notify(title="Youtube play" , message ="playing...." , timeout = 4)
                kit.playonyt(query)
                print("\nDone!!!\n")
                
                
            except:
                print("Something is wrong!!!\n")

        case "info" :

            try:
                print("\n                                          *************** " +query+ " ****************\n")
                kit.info(query)
                print("\nDone!!!\n")
                
                notify.notify(title="Google Search!" , message ="Searching......." , timeout = 7)
                
            except:
                print("Something is wrong!!!\n")

        case "shutdown" :
            
            try:
                kit.shutdown(time=T)
                print("\nDone!!!\n")
                
                notify.notify(title="Shut Down" , message =f"Shuting Down in {T}s. " , timeout = 10)
                
            except:
                print("Something is wrong!!!\n")

        case "cancel" :

            try:
                kit.cancel_shutdown()
                print("\nDone!!!\n")
                
                notify.notify(title="Shut Down Cancel" , message ="canceled" , timeout = 4)
                
            except:
                print("Something is wrong!!!\n")

        case "sendwhatmsg" :

            try:
                kit.sendwhatmsg(Phone_no , msg , hours , mins)
                print("\nDone!!!\n")
                
                notify.notify(title="Whatsapp massage" , message ="sending...." , timeout = 10)
            except:
                print("Something is wrong!!!")

        case "history" :

            try:
                kit.show_history()
                print("\nDone!!!\n")
                
                notify.notify(title="Task History" , message ="History preview" , timeout = 6)
            except:
                print("Something is wrong!!!\n")
                
        case "sendimg" :

            try:
                kit.sendwhats_image(Phone_no , file ,  msg)
                print("\nDone!!!\n")
                
                notify.notify(title="Image Send" , message ="Sending Image....." , timeout = 4)
                
            except:
                print("Something is wrong!!!\n")
                
import os, subprocess, sys, time

#Get and set the current working directory
if getattr(sys, 'frozen', False):
    absWorkingDir = os.path.dirname(sys.executable)
elif __file__:
    absWorkingDir = os.path.dirname(__file__)
os.chdir(absWorkingDir)

filePath = os.path.join(absWorkingDir,"rwd.exe")
sc = ''
mo = ''



def quit():
    print('Done, closing window...')
    time.sleep(2)
    #input('Done')
    
def createSched():
    print()
    command=['schtasks.exe','/CREATE','/SC','%s'%sc,'/TN','Reddit Wallpaper Changer','/TR','"%s"'%filePath,'/MO','%s'%mo]
    proc = subprocess.Popen(command)
    proc.wait()
    quit()

def askInterval():
    while(True):
        print()
        userInput= input('Enter interval between wallpaper change: (format example: 1 hour, 2 min)\n')
        userInput = userInput.split()
        if len(userInput)==2:
            try:
                global mo
                mo = int(userInput[0])
            except:
                print('Wrong input')       
                continue
            global sc
            
            if userInput[1] == 'min':
                sc = 'MINUTE'
                createSched()
                break
            
            elif userInput[1] == 'hour':
                sc = 'HOURLY'
                createSched()
                break
            else:
                print('Wrong input')
                continue
        else:
            print('Wrong input')
            continue
                  
def deleteSched():
    print()
    command=['schtasks.exe','/delete','/TN','Reddit Wallpaper Changer']
    p = subprocess.Popen(command)
    p.wait()
    quit()


def mainMenu():
    while(True):
        userInput = input('MAIN MENU:\n[1]:Create new schedule or change current schedule\n[2]:Delete schedule\nEnter value: ')
        if userInput == '1':
            askInterval()
            break
        elif userInput == '2':
            deleteSched()
            break
        else:
            print('wrong input')
            continue
    
mainMenu()

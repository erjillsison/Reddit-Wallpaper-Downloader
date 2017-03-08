#!python3
#Wallpaper Changer, wallpapers downloaded from reddit and set as desktop background

import requests, os, re, ctypes, sys

#Get and set the current working directory
if getattr(sys, 'frozen', False):
    absWorkingDir = os.path.dirname(sys.executable)
elif __file__:
    absWorkingDir = os.path.dirname(__file__)
os.chdir(absWorkingDir)

print(absWorkingDir)

#Create folder to store images if it doesnt exist
imgSaveLoc=os.path.join(absWorkingDir,'wallpapers')
if not os.path.exists(imgSaveLoc):
    os.makedirs(imgSaveLoc)
	
#Create config file if it doesnt exist		
if not os.path.isfile('config.txt'):
	config = open('config.txt','w')
	configSettings = {'subreddits':'wallpapers','numberOfDownloads':10}
	config.write(str(configSettings))
	config.close()
	
#VARIABLES	
linkLimit = 200
listOfFilePaths = [] #Before Saving
fileList =[] #used to track if downloaded file is already set as wallpaper

#subreddits and number of files to download taken from config.txt
with open('config.txt','r') as c:
    s = c.read()
    s = eval(s)
    print('Reading config file: '+str(s))
    subreddits = s['subreddits']
    maxLinks = s['numberOfDownloads']
    
#Create links text file, used to store a list of the image file paths
#Once used as a wallpaper, the image file path is deleted from here
#To ensure usage of all images before redownloading
if not os.path.isfile('links.txt'):
    linksFile = open('links.txt','w')
    linksFile.close()
    
#regex to get the file format
imgUrlPattern = re.compile(r'(.*)(.jpg$|.png$)')
imgSizePattern =  re.compile(r'''
                             (.*)?
                             (\[?)
                             (\d{4})
                             (\s?)
                             (x|×)
                             (\s?)
                             (\d{4})
                             (\]?)
                             ''',re.VERBOSE)

def downloadImage(imageUrl, localFileName):
    response = requests.get(imageUrl)
    with open(localFileName, 'wb') as fo:
              for chunk in response.iter_content(4096):
                  fo.write(chunk)
                  
def deleteDirectoryFiles():
    listOfFiles = os.listdir(imgSaveLoc)
    for fileName in listOfFiles:
        mo = imgUrlPattern.search(fileName)
        if mo:          
            print('Deleting '+fileName)
            os.remove(os.path.join(imgSaveLoc,fileName))
            
#iterate for every submission
def downloadLinks():
    #Pull data from reddit website
    r = requests.get("http://reddit.com/r/%s/.json" %subreddits, params='limit=200', headers = {'User-agent': 'wallpaper downloader by /u/kerrydon'})
    data = r.json()
	
    #limit counter on returned titles
    counter=0
    for submission in data['data']['children']:
        #NSFW check
        if not submission['data']['over_18']:
            
            #check if title includes jpg or png
            mo = imgUrlPattern.search(submission['data']['url'])
            if mo:
                
                #check if title includes image size          
                mo2 = imgSizePattern.search(submission['data']['title'])
                if mo2:
                    
                    #Get submission title
                    title = mo2.group(1)
                    title = re.sub('[\[\(\]\)\/:?*<>"|.]','',title)
                    title = title[:75]
                    
                    #Create local file name with the file format
                    localFileName = title+'['+mo2.group(3)+'x'+mo2.group(7)+']'+mo.group(2)
                    
                    #create the file path to save
                    newFilePath = os.path.join(imgSaveLoc,localFileName)
                    
                    if mo2.group(3)>mo2.group(7):
                        w = int(mo2.group(3))
                        h = int(mo2.group(7))
                    else:
                        w = int(mo2.group(7))
                        h = int(mo2.group(3))
                        
                    #check if image dimensions above 1440p
                    if w>=1920 and h>=1080 and w/h>=1.6 and w/h<=1.9:                  
                        
                        #download file
                        print('Downloading %s...' %localFileName)
                        downloadImage(submission['data']['url'],newFilePath)

                        #add file path to list
                        listOfFilePaths.append(newFilePath)
                        
                        counter+=1                
                    if counter==maxLinks:
                        break
                   
def setWallpaper(filePath):                   
    SPI_SETDESKTOPWALLPAPER=20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, filePath,3)
    print('Setting desktop background to ' + filePath)
    del fileList[fileList.index(filePath)]
    print('Images left before redownload: '+str(len(fileList)))
    linksFile = open('links.txt','w')
    for s in fileList:
        linksFile.write('%s\n' %s)
        
#delete files before download then download images
def reDownload():
    deleteDirectoryFiles()
    downloadLinks()
    global fileList
    fileList = listOfFilePaths
    print('Images left before redownload: '+str(len(fileList)))
    linksFile = open('links.txt','w')
    for s in fileList:
        linksFile.write('%s\n' %s)
        
def isImgFolderEmpty():
    listOfFiles = os.listdir(imgSaveLoc)
    if len(listOfFiles)==0:
        return True
    else:
        return False

#Read from existing link text file    
linksFile = open('links.txt','r')

#Store into a list variable
fileList = linksFile.read().splitlines()
print(len(fileList))

#Check if fileList is not empty, set wallpaper according to fileList    
while(len(fileList)!=0):  
    if os.path.isfile(fileList[0]): #check if file exists, else, delete
        setWallpaper(fileList[0])
        break
    else:
        del fileList[0]
        print('Image file missing, moving to next file path')
        continue

#Check if fileList/links.text has run out or the image folder is empty
if len(fileList)==0 or isImgFolderEmpty():    
    reDownload()
    setWallpaper(fileList[0])
    

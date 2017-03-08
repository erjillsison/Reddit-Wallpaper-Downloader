REDDIT WALLPAPER DOWNLOADER by erjill sison

SUMMARY:
	-No Console/GUI
	-Downloads wallpapers or any images from subreddits in reddit.com (see CONFIG:)
	[default values: (subreddit: reddit.com/r/wallpapers, number of files to download:10]
	-Sets the desktop background to one of the downloaded wallpapers
	-Can be ran automatically using Windows Task Scheduler (see TASK SCHEDULING:)

HOW IT WORKS:
	On the first run:

		NOTE: No console or any prompt will show when it runs, 
		wait until number of files in wallpapers folder match the required number(default:10)
		
		-Automatically creates config.txt, links.txt and wallpapers folder
		-Downloads images (subreddits downloaded from and number of files downloaded is set in config.txt)
		-The list of file paths is saved in links.txt (DO NOT EDIT THIS)
		
		-Sets the wallpaper according to the first entry in links.txt
		-Deletes the entry from links.txt
		

	Subsequest runs:		
		-Sets the wallpaper according to the first entry in links.txt
		-Deletes the entry from links.txt
		-Once the links.txt has ran out of paths, redo the first run sequence(download..)
	
TASK SCHEDULING:
	The app uses Windows Task Scheduler to run automatically in given intervals
	To enable this: 
		-Can be done manually by using the Windows Task Scheduler app
		-or use the scheduler.exe included and follow the steps given by the prompt

	
CONFIG:
	-Edit config.txt to add more subreddits(under 'subreddits' key separated by a '+')
	or increase number of files to download (under 'numberOfDownloads' key)
	-Sample format in config.txt file:
	{'subreddits': 'wallpapers+wallpaper+WQHD_wallpaper', 'numberOfDownloads': 10}
	
NOTES:
	-ONLY DOWNLOADS:
		-from submissions with the image dimensions in the post title e.g "something [1920x1080]"(for speed)
		-if said dimension is bigger than 1920x1080
		-if aspect ratio is bigger than 1.6 or less than 1.9
UNINSTALL:
	-run scheduler.exe to delete create task
	-delete all files normally
ABOUT:
	-Built using python language
	-Packaged using Pyinstaller module to a windows exe file
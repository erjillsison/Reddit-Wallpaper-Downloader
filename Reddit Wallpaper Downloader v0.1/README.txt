REDDIT WALLPAPER DOWNLOADER by erjill sison

Download:
	-Click Clone or download on the top right of the GitHub page https://github.com/erjillsison/Reddit-Wallpaper-Downloader
	-Download ZIP
	-Extract and run rwd.exe from Reddit Wallpaper Downloader folder

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
		-Downloads 10 images by default		
		-Sets the desktop background from one of the downloaded images

	Subsequest runs:		
		-Cycles through the images download to set as desktop background
		-Once all images have been used, images will be deleted and a new set will be downloaded
	
TASK SCHEDULING:
	-Run scheduler.exe and follow prompt
	-This creates a task schedule using Windows Task Scheduler
	
CONFIG:
	-Edit config.txt to add more subreddits(under 'subreddits' key separated by a '+')
	or increase number of files to download (under 'numberOfDownloads' key)
	-Sample format in config.txt file:
	{'subreddits': 'wallpapers+wallpaper+WQHD_wallpaper', 'numberOfDownloads': 10}
	
NOTES:
	-ONLY DOWNLOADS:
		-from submissions with the image dimensions in the post title e.g "something [1920x1080]"(for speed)
		-if said dimension is same as or greater than 1920x1080
		-if aspect ratio is bigger than 1.6 or less than 1.9
		
UNINSTALL:
	-run scheduler.exe to delete created task
	-delete all files normally
	
ABOUT:
	-Built using python language
	-Packaged using Pyinstaller module to a windows exe file
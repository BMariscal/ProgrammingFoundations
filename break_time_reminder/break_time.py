import webbrowser
import time
"""This program runs 3 times and it will remind you to take a break every 2 hours"""
runs = 3
print("This program started on" + time.ctime())
while runs > 0:
	#2*60*60 = number of seconds in 2 hours
    time.sleep(2*60*60)
    webbrowser.open_new_tab('"http://www.youtube.com/watch?v=dQw4w9WgXcQ')
    runs-=1

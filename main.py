 '''input
test.mp4
test2.mp4
1
Todo : Add dynamic input
'''

from ffmpy import FFmpeg

raw = raw_input('Enter the name ')
export = raw_input('Save file as ')
choice = int(raw_input('Enter  \n 1-change format \n 2-trim \n'))
if choice==2:
	starttime = raw_input('Start time (hh:mm:ss)  ')
	duration = raw_input('enter the duration (hh:mm:ss)  ')
	argument='-ss: '+starttime+' -t: '+duration+' -async 1 -strict -2'
	ff = FFmpeg(
		inputs={raw: None},
		outputs={export : argument}
		)
	#-t: duration(delete it to crop till the end) -ss:starttime
	ff.cmd
	ff.run()
elif choice==1:
	ff = FFmpeg(
		inputs={raw: None},
		outputs={export : None}
		)
	#-t: duration(delete it to crop till the end) -ss:starttime
	ff.cmd
	ff.run()	

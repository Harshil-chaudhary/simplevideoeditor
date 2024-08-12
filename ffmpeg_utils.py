# ffmpeg_utils.py

from ffmpy import FFmpeg

def trim_video(input_file, output_file, start_time, duration):
    """Trim the video using FFmpeg."""
    arguments = f'-ss {start_time} -t {duration} -async 1 -strict -2'
    ff = FFmpeg(inputs={input_file: None}, outputs={output_file: arguments})
    ff.run()

def change_format(input_file, output_file):
    """Change the video format using FFmpeg."""
    ff = FFmpeg(inputs={input_file: None}, outputs={output_file: None})
    ff.run()

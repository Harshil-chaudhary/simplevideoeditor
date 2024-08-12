from ffmpy import FFmpeg

def get_input(prompt):
    """Get input from the user."""
    return input(prompt)

def get_choice():
    """Get the user's choice of action."""
    while True:
        try:
            choice = int(get_input('Enter:\n1 - Change format\n2 - Trim\n'))
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def trim_video(input_file, output_file, start_time, duration):
    """Trim the video using FFmpeg."""
    arguments = f'-ss {start_time} -t {duration} -async 1 -strict -2'
    ff = FFmpeg(inputs={input_file: None}, outputs={output_file: arguments})
    ff.run()

def change_format(input_file, output_file):
    """Change the video format using FFmpeg."""
    ff = FFmpeg(inputs={input_file: None}, outputs={output_file: None})
    ff.run()

def main():
    input_file = get_input('Enter the input video file name: ')
    output_file = get_input('Save file as: ')
    choice = get_choice()
    
    if choice == 2:  # Trim
        start_time = get_input('Start time (hh:mm:ss): ')
        duration = get_input('Enter the duration (hh:mm:ss): ')
        trim_video(input_file, output_file, start_time, duration)
    elif choice == 1:  # Change format
        change_format(input_file, output_file)

if __name__ == "__main__":
    main()

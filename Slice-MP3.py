
## Import easygui

try: import easygui
except  Exception:
    raise 'easygui is not installed. to install it >> pip install easygui'
    sys.exit(0)


#################################################
# Welcome window
msg = """   Welcome to mP3 slicer,
    Requirements for this program:
    1. Download ffmpeg then add ffmpeg/bin path to environment system path.
    2. install Pydub:
        pip install pydub
    press Continue to choose mp3 audio file to slice please ...
"""

title = "mP3 slicer"

if easygui.ccbox(msg, title):     # show a Continue/Cancel dialog
    pass  # user chose Continue
else:  # user chose Cancel
    sys.exit(0)

#########################################
# Import AudioSegment
try: from pydub import AudioSegment
except  Exception:
    raise 'pydub is not installed. to install it >> pip install pydub'
    sys.exit(0)

#################################

# Input file path
file =  easygui.fileopenbox(title = "mP3 slicer")
filename = file.split('.')[0].split('\\')[-1]

#################################

# Input Duration of Slice in Seconds
N = easygui.integerbox(msg="Enter the duration of each slice (in Seconds): "
                   ,title = "mP3 slicer") *1000

#################################

# Input Destination folder of the output slices
easygui.msgbox("Choose the destination folder ...", ok_button="Choose Folder!",title = "mP3 slicer")
dest = easygui.diropenbox(title = "mP3 slicer")

#
##########################################

## Reading Sound
sound = AudioSegment.from_file(file , format='mp3')


R = len(sound) // N  # Number of Slices output

########################
## Start window
easygui.msgbox(f"it will slice the file: {filename}.mp3 \n \ninto {R+1} files of ({N/1000} Seconds) duration \n\nin the directory: {dest} ", ok_button="Start",title = "mP3 slicer")

start = 0  # Seconds *1000
end = N

log = ''
for i in range(R):
    out = sound[start:end]

    out.export( f"{dest}\\{i}.mp3" , format="mp3")
    log += f'{dest}\\{i}.mp3 was exported. \n'

    start += N
    end += N

out = sound[start:len(sound)]
out.export( f"{dest}\\{R+1}.mp3" , format="mp3")
log += f'{dest}\\{i}.mp3 was exported. \n'

easygui.msgbox(log, ok_button="Done!",title = "mP3 slicer")

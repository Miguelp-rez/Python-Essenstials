# winsound
import winsound

# Creating flag argument
filename = 'C:/Users/Sindro86/Music/wav_files/tada.wav'
flags = winsound.SND_FILENAME

winsound.PlaySound(filename, flags)

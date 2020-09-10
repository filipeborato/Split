from spleeter.separator import Separator

def separa(number,wave):    
    separator = Separator(f"spleeter:{number}stems")
    audio_file = wave
    destination = 'files/separate'
    separator.separate_to_file(audio_file, destination)
    
#split.separa(2,"files/It dont mean i think_ master.mp3")     
from spleeter.separator import Separator

def separa(number,wave):    
    separator = Separator(f"spleeter:{number}stems")
    audio_file = wave
    destination = 'files/separate'
    separator.separate_to_file(audio_file, destination)
from spleeter.separator import Separator


separator = Separator('spleeter:5stems')

separator = Separator('path/to/config.json')

createSeparator = lambda number: Separator(f'spleeter:{number}stems')

separator = createSeparator(5)

audio_file = 'files/It dont mean i think_ master.mp3'
destination = 'files/separate'

separator.separate_to_file(audio_file, destination)


from spleeter.separator import Separator
import os

def separa(number, wave):    
    """
    Separação de audio usando Spleeter atualizado
    """
    try:
        # Cria o separador com configuração atualizada
        separator = Separator(f"spleeter:{number}stems-16kHz")
        audio_file = wave
        destination = 'files/separate'
        
        # Cria diretório se não existir
        os.makedirs(destination, exist_ok=True)
        
        # Realiza a separação
        separator.separate_to_file(audio_file, destination)
        
        return True
    except Exception as e:
        print(f"Erro na separação com Spleeter: {e}")
        return False

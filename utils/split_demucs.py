import subprocess
import os
import shutil

def separa(number, wave):
    """
    Separação de audio usando Demucs (alternativa moderna ao Spleeter)
    """
    try:
        # Cria diretório de destino
        destination = 'files/separate'
        os.makedirs(destination, exist_ok=True)
        
        # Mapeia número de stems para modelos Demucs
        model_map = {
            2: "htdemucs_ft",  # 2 stems: vocals, accompaniment
            4: "htdemucs",     # 4 stems: vocals, drums, bass, other
            5: "htdemucs_6s"   # 6 stems (usando 5 mais próximo)
        }
        
        model = model_map.get(number, "htdemucs_ft")
        
        # Executa Demucs
        cmd = [
            "python", "-m", "demucs",
            "--model", model,
            "--out", destination,
            wave
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Reorganiza arquivos para manter compatibilidade com estrutura existente
            reorganize_demucs_output(destination, wave)
            return True
        else:
            print(f"Erro na separação com Demucs: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Erro na separação com Demucs: {e}")
        return False

def reorganize_demucs_output(destination, original_file):
    """
    Reorganiza a saída do Demucs para manter compatibilidade
    """
    try:
        # Demucs cria uma estrutura modelo/nome_arquivo/
        # Precisamos mover para a estrutura esperada
        base_name = os.path.splitext(os.path.basename(original_file))[0]
        
        # Encontra a pasta criada pelo Demucs
        for item in os.listdir(destination):
            item_path = os.path.join(destination, item)
            if os.path.isdir(item_path):
                for subitem in os.listdir(item_path):
                    subitem_path = os.path.join(item_path, subitem)
                    if os.path.isdir(subitem_path) and base_name in subitem:
                        # Move arquivos para a estrutura esperada
                        audio_dest = os.path.join(destination, "audio")
                        os.makedirs(audio_dest, exist_ok=True)
                        
                        for audio_file in os.listdir(subitem_path):
                            if audio_file.endswith('.wav'):
                                src = os.path.join(subitem_path, audio_file)
                                dst = os.path.join(audio_dest, audio_file)
                                shutil.move(src, dst)
                        break
    except Exception as e:
        print(f"Erro ao reorganizar saída: {e}")

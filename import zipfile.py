import zipfile
import os
import tempfile

def move_json_files_to_new_zip(source_zip_path, json_zip_path):
    # Cria um arquivo ZIP temporário para armazenar os arquivos .json
    with tempfile.NamedTemporaryFile(delete=False) as temp_zip:
        temp_zip_path = temp_zip.name
    
    # Abre o arquivo ZIP original e o novo arquivo ZIP para .json
    with zipfile.ZipFile(source_zip_path, 'r') as source_zip:
        with zipfile.ZipFile(temp_zip_path, 'w') as json_zip:
            # Itera sobre todos os arquivos no arquivo ZIP original
            for file_info in source_zip.infolist():
                # Se o arquivo for .json, copia para o novo ZIP
                if file_info.filename.endswith('.json'):
                    # Lê o conteúdo do arquivo .json
                    with source_zip.open(file_info.filename) as file:
                        # Adiciona o arquivo .json ao novo ZIP
                        json_zip.writestr(file_info, file.read())
    
    # Move o arquivo ZIP temporário para o destino final
    os.replace(temp_zip_path, json_zip_path)

# Caminho para o arquivo ZIP original e o caminho do novo arquivo ZIP para os arquivos .json
source_zip_path = r'C:\Users\caios\OneDrive\Documentos\Backup.zip'
json_zip_path = r'C:\Users\caios\OneDrive\Documentos\novo_arquivo_json.zip'

# Verifique se o arquivo de origem existe
if not os.path.exists(source_zip_path):
    print(f'Arquivo não encontrado: {source_zip_path}')
else:
    move_json_files_to_new_zip(source_zip_path, json_zip_path)
    print(f'Arquivos .json foram movidos para: {json_zip_path}')


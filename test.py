import subprocess
import time
import os
import sys

def run_streamlit():
    # Caminho para o Python no ambiente virtual
    python_path = os.path.join(os.path.abspath("venv_FS"), "Scripts", "python.exe")  # Verifique o caminho para o Python do venv

    # Caminho para o script do Streamlit
    script_path = "streamlit_test.py"  # Coloque o caminho correto para o seu script

    # Verificar se o arquivo do script existe
    if not os.path.exists(script_path):
        print(f"Erro: O arquivo {script_path} não foi encontrado!")
        sys.exit(1)

    # Verificar se o Python do ambiente virtual existe
    if not os.path.exists(python_path):
        print(f"Erro: O Python não foi encontrado em {python_path}!")
        sys.exit(1)

    # Rodar o Streamlit com o Python do ambiente virtual
    process = subprocess.Popen(
        [python_path, "-m", "streamlit", "run", script_path, "--server.headless", "true"], 
        stdout=subprocess.PIPE,  
        stderr=subprocess.PIPE,  
        text=True,  # Lê a saída como string
        shell=True  # Necessário no Windows
    )

    # Aguarda o servidor iniciar
    time.sleep(3)

    # Captura o stdout e stderr
    stdout, stderr = process.communicate()
    if stderr:
        print(f"Erro ao rodar Streamlit:\n{stderr}")
    
    # Exibe a saída do processo
    if stdout:
        print(f"Saída do Streamlit:\n{stdout}")

    # Mantém o script rodando enquanto o Streamlit estiver ativo
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

if __name__ == "__main__":
    run_streamlit()

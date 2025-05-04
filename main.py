import os
import shutil
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

# Configurações da API
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

# Extensões de vídeo suportadas
VIDEO_EXTENSIONS = {
    '.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.mpeg', '.mpg', '.m4v', '.3gp'
}

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=8080)
    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )

def upload_video(youtube, video_file, title, description, tags, category_id, privacy_status):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload {int(status.progress() * 100)}% concluído")
    print(f"Upload concluído: {video_file} (Vídeo ID: {response['id']})")
    return response

if __name__ == "__main__":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # para testes em HTTP

    # Solicita ao usuário o caminho da pasta de vídeos
    raw_path = input("Informe o caminho da pasta de vídeos: ")
    pasta_videos = raw_path.strip().strip('"').strip("'")
    if not os.path.isdir(pasta_videos):
        print("O caminho informado não é uma pasta válida.")
        exit(1)

    # Pergunta a visibilidade
    print("Selecione a visibilidade dos vídeos:")
    print("  [1] Público (padrão)")
    print("  [2] Privado")
    escolha = input("Opção (1 ou 2): ").strip()
    if escolha == "2":
        privacy = "private"
    else:
        privacy = "public"

    # Cria pasta de sucesso, se ainda não existir
    pasta_sucesso = os.path.join(pasta_videos, "upload_success")
    os.makedirs(pasta_sucesso, exist_ok=True)

    # Autentica uma vez
    youtube = get_authenticated_service()

    # Percorre todos os arquivos da pasta
    for arquivo in os.listdir(pasta_videos):
        caminho_arquivo = os.path.join(pasta_videos, arquivo)
        if not os.path.isfile(caminho_arquivo):
            continue
        ext = os.path.splitext(arquivo)[1].lower()
        if ext not in VIDEO_EXTENSIONS:
            continue

        print(f"\nEnviando {arquivo}...")
        try:
            upload_video(
                youtube,
                caminho_arquivo,
                title=os.path.splitext(arquivo)[0],
                description="",
                tags=[],
                category_id="22",      # People & Blogs
                privacy_status=privacy
            )
            # Move para a pasta de sucesso
            destino = os.path.join(pasta_sucesso, arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f"{arquivo} movido para {pasta_sucesso}")
        except Exception as e:
            print(f"Erro ao enviar {arquivo}: {e}")

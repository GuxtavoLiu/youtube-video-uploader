import os
import argparse
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES)
    credentials = flow.run_console()
    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

def upload_video(youtube, video_file, title, description, tags, category_id, privacy_status):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status  # "public", "unlisted" ou "private"
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
    print("Upload concluído! Vídeo ID:", response["id"])
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Envio de vídeo ao YouTube")
    parser.add_argument("video_file", help="Caminho para o arquivo de vídeo")
    parser.add_argument("--title", default="Título padrão", help="Título do vídeo")
    parser.add_argument("--description", default="", help="Descrição do vídeo")
    parser.add_argument("--tags", nargs="*", default=[], help="Tags do vídeo")
    parser.add_argument("--category", default="22", help="ID da categoria (p.ex. 22 = People & Blogs)")
    parser.add_argument("--privacy", default="private", choices=["public","unlisted","private"],
                        help="Status de privacidade")
    args = parser.parse_args()

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # só para testes em HTTP
    youtube = get_authenticated_service()
    upload_video(youtube,
                 args.video_file,
                 args.title,
                 args.description,
                 args.tags,
                 args.category,
                 args.privacy)

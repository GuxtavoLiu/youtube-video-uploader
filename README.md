<!-- keywords: youtube api, python upload, oauth2, batch upload, video uploader -->

# YouTube Video Uploader CLI

A simple Python tool to batch-upload all videos from a folder to your YouTube channel using the **YouTube Data API v3**.

---

## 🚀 Features

- **Batch upload**: scans all video files in a folder and uploads them automatically.  
- **Custom visibility**: choose **Public** (default) or **Private** before uploading.  
- **Automatic organization**: each successfully uploaded video is moved to an `upload_success` subfolder.  
- **OAuth authentication**: runs in your browser without exposing your password.

---

## 📝 Prerequisites

- **Python 3.7+** installed  
- A Google account with a YouTube channel  
- A Google Cloud project with the **YouTube Data API v3** enabled  
- OAuth 2.0 credentials (a `client_secret.json` file)

---

## ⚙️ Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/GuxtavoLiu/youtube-video-uploader.git
   cd youtube-video-uploader
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Linux / macOS
   source .venv/bin/activate  
   # Windows PowerShell
   .venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

1. In the **Google Cloud Console**, create an **OAuth Client ID** (Application → Desktop) and download the JSON.
2. Ensure the **YouTube Data API v3** is enabled in the same project.
3. Rename the downloaded JSON to `client_secret.json` and place it in the project root.

---

## 🎬 Usage

1. Run the script:

   ```bash
   python main.py
   ```
2. **Enter the folder path** containing your videos (e.g. `C:\Users\gusta\Videos\Fortnite\Teste`).
3. **Select visibility**:

   * `1` — Public (default)
   * `2` — Private
4. A browser window will open for you to authorize the app with Google.
5. The script will upload each video and then move it into the `upload_success/` folder.

---

## 📂 Project Structure

```
├── client_secret.json       # OAuth credentials (gitignored)
├── main.py                  # Main script
├── requirements.txt         # Dependencies
└── README.md                # This file
```

---

## 🤝 Contributing

1. Fork this repository
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 🛡️ License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

Made with ♥ by **G-Liu Code** • [https://gustavoliu.com](https://gustavoliu.com)
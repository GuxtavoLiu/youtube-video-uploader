
# YouTube Video Uploader CLI

Uma ferramenta simples em Python para enviar em lote todos os vídeos de uma pasta para o seu canal do YouTube, usando a **YouTube Data API v3**.

---

## 🚀 Funcionalidades

- **Upload em lote**: percorre todos os arquivos de vídeo de uma pasta e faz o envio automático.  
- **Visibilidade personalizável**: escolha entre **Público** (padrão) ou **Privado** antes de subir.  
- **Organização automática**: cada vídeo enviado com sucesso é movido para uma subpasta `upload_success`.  
- **Autenticação OAuth**: fluxo via navegador, sem expor sua senha.

---

## 📝 Pré-requisitos

- **Python 3.7+** instalado  
- Conta Google com um canal no YouTube  
- Projeto no Google Cloud com a **YouTube Data API v3** ativada  
- Credenciais OAuth 2.0 (arquivo `client_secret.json`)

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/youtube-video-uploader.git
   cd youtube-video-uploader
    ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux / macOS
   .venv\Scripts\activate       # Windows PowerShell
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuração

1. No **Google Cloud Console**, crie um **OAuth Client ID** (tipo “Application → Desktop”) e baixe o JSON.
2. Ative a **YouTube Data API v3** no mesmo projeto.
3. Renomeie o JSON para `client_secret.json` e copie para a raiz do projeto.

---

## 🎬 Como usar

1. Execute:

   ```bash
   python main.py
   ```
2. **Informe o caminho** da pasta com seus vídeos (por ex. `C:\Users\gusta\Videos\Fortnite\Teste`).
3. **Escolha a visibilidade**:

   * `1` — Público (padrão)
   * `2` — Privado
4. O navegador abrirá para você autorizar o App no Google.
5. O script subirá cada vídeo e, ao concluir, moverá para `upload_success/`.

---

## 📂 Estrutura do projeto

```
.
├── client_secret.json       # Credenciais OAuth (gitignore)
├── main.py                  # Script principal
├── requirements.txt         # Dependências
└── README.md                # Documentação
```

---

## 🤝 Contribuições

1. Faça um *fork* deste repositório
2. Crie uma *branch* (`git checkout -b feature/nome-da-feature`)
3. Faça suas alterações e *commits*
4. Abra um **Pull Request**

---

## 🛡️ Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ♥ por **G-Liu Code** • [https://gustavoliu.com](https://gustavoliu.com)

```
```

# 音声操作読み上げサーバー

これは[voice_control](https://github.com/ryo08271154/voice_control)の読み上げサーバーです。
## セットアップ

### クライアント側の設定

[voice_control](https://github.com/ryo08271154/voice_control)の設定をするときに音声読み上げサーバーのURLを`http://127.0.0.1:8000/voice`に設定してください。

### サーバー側の設定

1. **リポジトリのクローン**
   ```bash
   git clone https://github.com/ryo08271154/voice_control_server.git
   cd voice_control_server
   ```

2. **依存関係のインストール**
   ```bash
   pip install -r requirements.txt
   ```

3. **サーバーの起動**
   ```bash
   uvicorn main:app
   ```

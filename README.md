# 音声操作読み上げサーバー

これは[voice_control](https://github.com/ryo08271154/voice_control)の読み上げサーバーです。

## セットアップ

### サーバー側の設定

1. **リポジトリのクローン**

   ```bash
   git clone https://github.com/ryo08271154/voice-control-yomiage.git
   cd voice-control-yomiage
   ```

2. **依存関係のインストール**

   ```bash
   pip install -r requirements.txt
   ```

3. **音声合成エンジンの選択と設定**

   A. 標準の音声合成エンジンを使用する場合
   - 追加の設定は不要です

   B. VOICEVOXを使用する場合
   - [VOICEVOX](https://voicevox.hiroshiba.jp/)をダウンロードしてインストール
   - VOICEVOXエンジンを起動（デフォルトポート: 50021）
   - `.env`ファイルをプロジェクトのルートディレクトリに作成し、以下の内容を設定：

     ```bash
     VOICEVOX_URL="http://127.0.0.1:50021"
     SPEAKER_ID=1
     ```

   - SPEAKER_IDは使用したいVOICEVOXのキャラクターIDを指定

4. **サーバーの起動**

   ```bash
   uvicorn main:app
   ```

### クライアント側の設定

[voice_control](https://github.com/ryo08271154/voice_control)の設定時に、使用する音声合成エンジンに応じて以下のURLを設定してください：

- 標準の音声合成エンジンを使用する場合: `http://127.0.0.1:8000/voice`
- VOICEVOXを使用する場合: `http://127.0.0.1:8000/voice_vox`

## 利用可能なエンドポイント

### POST /voice

標準の音声合成エンジンを使用して読み上げを行います。追加の設定は不要です。

### POST /voice_vox

VOICEVOXを使用して読み上げを行います。使用する場合は、VOICEVOXの起動と環境変数の設定が必要です。

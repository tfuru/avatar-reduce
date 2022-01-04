# avatar-reduce

# プロジェクト作成
Google Cloud Console で 作成する 

```
gcloud app create --project=avatar-reduce

asia-northeast1
```

# python 開発環境構築
M1 macbook の構築例
```
brew update
brew install pyenv

vi  ~/.zshrc
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

source ~/.zshrc

cd work/xxxxx/

# ローカルに 3.9.2 をインストール
pyenv install 3.9.2
pyenv local 3.9.2
# python -m ensurepip --upgrade

pip install -t lib -r requirements.txt
```

# デプロイ

```
# gcloud app deploy --project=[PROJECT]
gcloud app deploy --no-cache --project=avatar-reduce
gcloud app browse --project=avatar-reduce
```

# ログ表示

```
# gcloud app logs tail -s default --project=[PROJECT]
gcloud app logs tail -s default --project=avatar-reduce
gcloud app logs read --project=avatar-reduce
```

# 利用ライブラリ
[VReducer](https://github.com/nkjzm/VReducer)
[VReducer-VroidMobile対応](https://github.com/tfuru/VReducer) 

# 参考 サイト
[DockerのイメージをGAE/FEにデプロイする](https://qiita.com/wasnot/items/b8691bb4940e6f4a9c24)

[vrm-specification](https://github.com/vrm-c/vrm-specification)

# avatar-reduce

# プロジェクト作成
Google Cloud Console で 作成する 

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

# ローカルに 2.7.18 をインストール
pyenv install 2.7.18
pyenv local 2.7.18

# pip をローカルにインストール
python -m ensurepip --upgrade

```

# デプロイ

```
# gcloud app deploy --project=[PROJECT]
gcloud app deploy --project=avatar-reduce
gcloud app browse --project=avatar-reduce
```

# ログ表示

```
# gcloud app logs tail -s default --project=[PROJECT]
gcloud app logs tail -s default --project=avatar-reduce
```

# 利用ライブラリ
[VReducer](https://github.com/nkjzm/VReducer) 

# 参考 サイト
[DockerのイメージをGAE/FEにデプロイする][https://qiita.com/wasnot/items/b8691bb4940e6f4a9c24]

[vrm-specification](https://github.com/vrm-c/vrm-specification)

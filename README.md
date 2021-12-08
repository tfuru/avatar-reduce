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

# ビルド

```
cd work/xxxxx/
# pip freeze > requirements.txt
pip install -r requirements.txt -t lib
```

# デプロイ

```
# gcloud app deploy --project=[PROJECT]
gcloud app deploy --project=avatar-reduce
gcloud app browse --project=avatar-reduce
```

# ライブラリ
[VReducer](https://github.com/nkjzm/VReducer)
- 

# GAE 参考 記事
https://datumstudio.jp/blog/gae%E3%81%A7%E3%82%B5%E3%82%AF%E3%83%83%E3%81%A8api%E3%82%B5%E3%83%BC%E3%83%90%E6%A7%8B%E7%AF%89/

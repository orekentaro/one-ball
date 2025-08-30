
# ベースイメージ
FROM python:3.12-slim

# wait-for-it.sh用にnetcat(nc)をインストール
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ作成
WORKDIR /app

# 依存関係コピー
COPY pyproject.toml uv.lock ./


# uvインストール＆依存関係解決
RUN pip install --no-cache-dir uv && \
    uv pip install --system --requirement pyproject.toml


# アプリケーションコードコピー
COPY . .
# wait-for-it.shのみ明示的にコピー＆実行権限付与
COPY scripts/wait-for-it.sh /app/scripts/wait-for-it.sh
RUN chmod +x /app/scripts/wait-for-it.sh

# ポート開放
EXPOSE 8000

# サーバ起動コマンド（PostgreSQLの起動を待機）
CMD ["/app/scripts/wait-for-it.sh", "db", "5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

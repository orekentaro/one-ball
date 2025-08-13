#!/usr/bin/env bash
# wait-for-it.sh: DBが起動するまで待機する
# 公式: https://github.com/vishnubob/wait-for-it

set -e

host="$1"
port="$2"
shift 2

while ! nc -z "$host" "$port"; do
    echo "Waiting for $host:$port..."
    sleep 1
done

echo "$host:$port is available!"
exec "$@"

# コンテナ起動
up:
	docker-compose up -d

# コンテナ停止
stop:
	docker-compose stop

# ログ監視
logs:
	docker-compose logs -f

# Pythonのコンテナに入る
CONTAINER=web
bash:
	docker-compose exec ${CONTAINER} bash

# PostgreSQLのコンテナに入る
DATABASE=db
psql:
	docker-compose exec ${DATABASE} bash
cd chat_room_backend\Redis
start cmd.exe /k "redis-server.exe redis.windows.conf"

cd ..
daphne -b 0.0.0.0 -p 8000 chat_room_backend.asgi:application
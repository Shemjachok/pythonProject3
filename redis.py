import redis

red = redis.Redis(
    host=redis-16450.c280.us-central1-2.gce.cloud.redislabs.com',
    port=16450,
    password='5Rz9VSJE9ooU9uKB0JTroNr69w1SRIWA'
)

red.set('var1', 'value1')  # записываем в кеш строку "value1"
print(red.get('var1'))  # считываем из кэша данные
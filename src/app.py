import logging

from orator import DatabaseManager
from sanic import Sanic
from sanic_cors import CORS

from config.config import Config
from src.department.v1.delivery.http_sanic import bp_department
# from kafka import KafkaConsumer
# from confluent_kafka import Consumer, KafkaError

logger = logging.getLogger(__name__)


def config_log(app):
    # set log config from config
    logging.config.dictConfig(Config.LOGGING)


def connect_db():
    # postgres use pgsql
    config = {
        'postgres': {
            'driver': Config.DB_TYPE,
            'host': Config.DB_HOST,
            'port':Config.DB_PORT,
            'database': Config.DB_NAME,
            'user': Config.DB_USER,
            'password': Config.DB_PASS,
            'prefix': '',
            'log_queries': True,
        }
    }
    return DatabaseManager(config)

# if you are using confluent kafka
# c = Consumer({
#     'bootstrap.servers': '',
#     'group.id': '',
#     'auto.offset.reset': 'earliest'
# })
# c.subscribe(['the-topic'])
# async def kafka_consumer_confluent():
#     while True:
#         msg = c.poll(1.0)
#         if msg is None:
#             continue
#         if msg.error():
#             print("Consumer error: {}".format(msg.error()))
#             continue

#         print('Received message: {}'.format(msg.value().decode('utf-8')))

#     c.close()

# if you are using kafka python
# consumer = KafkaConsumer(
#     "the-topics",
#     bootstrap_servers="",
#     group_id="",
#     auto_offset_reset="earliest"
# )
# async def kafka_consumer():   
#     for msg in consumer:
#         print(msg)

def create_app(config):
    app = Sanic(__name__)
    app.config.from_object(config)
    app.blueprint(bp_department)
    CORS(app, automatic_options=True)
    
    return app

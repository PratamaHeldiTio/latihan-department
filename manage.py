import logging

import asyncio
from sanic.exceptions import ServerError, InvalidUsage
# from src.app import create_app, connect_db, kafka_consumer_confluent, kafka_consumer
from src.app import create_app, connect_db, config_log
from schemas.json.loader import JSONSchemaLoader

from config.config import Config
from src.shared import response_object
from sanic.response import json

app = create_app(config=Config)

# config log
config_log(app)
logger = logging.getLogger(__name__)

@app.listener('before_server_start')
def setup_schemas(app, loop):
    # load all json schema
    JSONSchemaLoader.load(path='schemas/json/', filename="*.json")

@app.listener('before_server_start')
def setup_db(app, loop):
    app.db = connect_db()


@app.listener('after_server_stop')
def close_db(app, loop):
    app.db.disconnect()


@app.exception(InvalidUsage)
def invalid_usage(request, exception):
    # log
    logger.error(exception)

    if Config.DEBUG: return exception
    response = response_object.ResponseFailure.build_system_error(
        "{}: {}".format(exception.__class__.__name__, "{}".format(exception))
    )
    return json(response.value, status=Config.STATUS_CODES[response.type])

if __name__ == '__main__':
    if not Config.RUN_MULTIPLE_PROCESS: 
        # the basic run server
        app.run(host=Config.HOST, port=int(Config.PORT), debug=Config.DEBUG, auto_reload=False)
    else:
        # how to run kafka consumer along with the server
        server = app.create_server(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)

        loop = asyncio.get_event_loop()
        # the server
        asyncio.ensure_future(server)
        # kafka python
        # asyncio.ensure_future(kafka_consumer())
        # confluent kafka python
        # asyncio.ensure_future(kafka_consumer_confluent())
        loop.run_forever()

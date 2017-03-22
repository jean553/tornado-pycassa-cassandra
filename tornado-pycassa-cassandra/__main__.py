"""
Program start point
"""
import tornado

from pycassa.pool import ConnectionPool

from simple_handler import SimpleHandler

from config import CASSANDRA_POOL
from config import KEY_SPACE

def main():
    """
    start the tornado server application
    """

    cassandra_session = ConnectionPool(
        KEY_SPACE,
        [CASSANDRA_POOL],
        pool_size=1,
    )

    context = {"cassandra_session": cassandra_session,}

    application_tornado = tornado.web.Application([
        (
            r"/api/1/simple-handler/(.*)", 
            SimpleHandler, 
            context
        ),
    ])
    application_tornado.listen(8080)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

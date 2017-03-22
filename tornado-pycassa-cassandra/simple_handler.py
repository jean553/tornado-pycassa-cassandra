"""
Simple handler
"""
import json

import tornado
import tornado.web

from pycassa.columnfamily import ColumnFamily

from config import COLUMN_FAMILY

class SimpleHandler(tornado.web.RequestHandler):
    """
    Handles /api/1/simple-handler
    """

    def initialize(
        self,
        cassandra_session,
    ):
        """
        Initializer of the received request.

        Args:
            cassandra_session(pycassa.pool.ConnectionPool)
        """
        self.column_family = ColumnFamily(
            cassandra_session,
            COLUMN_FAMILY,
        )

    def post(
        self,
        key,
    ):
        """
        Handle POST /simple-handler requests.
        Save the received data into Cassandra.

        Args:
            key(str) URL key where the data has to be stored
            data(json) posted data in format: 

                `{
                    "first_value": "your value",
                    "second_value": "your value",
                    "third_value": "your value",
                }`
        """
        first_value = json.loads(self.request.body)['first_value']
        second_value = json.loads(self.request.body)['second_value']
        third_value = json.loads(self.request.body)['third_value']

        self.column_family.insert(
            key,
            {
                ('c1_first_value', 'c2_first_value'): str(first_value),
                ('c1_second_value', 'c2_second_value'): str(second_value),
                ('c1_third_value', 'c2_third_value'): str(third_value),
            }
        )

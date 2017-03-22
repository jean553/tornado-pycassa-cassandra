"""
Cassandra database manager
"""
from pycassa.pool import ConnectionPool
from pycassa.system_manager import SystemManager, SIMPLE_STRATEGY
import pycassa.cassandra.ttypes
from pycassa.system_manager import types

from config import KEY_SPACE
from config import COLUMN_FAMILY

def _init_db(server):

    dbsys = SystemManager(server)
    dbsys.create_keyspace(
        KEY_SPACE,
        SIMPLE_STRATEGY, 
        {"replication_factor": "1"}
    )

    column_family_type = types.CompositeType(
        types.UTF8Type(),
        types.UTF8Type(),
    )

    dbsys.create_column_family(
        KEY_SPACE,
        COLUMN_FAMILY,
        comparator_type=column_family_type,
        key_validation_class=types.UTF8Type(),
        default_validation_class=types.UTF8Type(),
    )

def _clean_db(server):

    dbsys = SystemManager(server)
    dbsys.drop_keyspace(KEY_SPACE)
    dbsys.close()

def reset_db(server):

    try:
        _clean_db(server)

    # throws exception if the keyspace does not exist
    except pycassa.cassandra.ttypes.InvalidRequestException, excep:
        pass

    _init_db(server)

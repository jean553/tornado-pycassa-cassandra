# tornado-pycassa-cassandra

Simple demonstration code combining Tornado, Pycassa and Cassandra 1.2.

## Start the service

Start the container:

```bash
vagrant up
```

Connect to the container:

```bash
vagrant ssh
```

Start the service:

```bash
python tornado-pycassa-cassandra
```

## Execute requests to the service

You can replace the values of the following keys:
 * `KEY`
 * `FIRST_VALUE`
 * `SECOND_VALUE`
 * `THIRD_VALUE`

```bash
curl \
    -X POST \
    --data '{"first_value": FIRST_VALUE, "second_value": SECOND_VALUE, "third_value": THIRD_VALUE}' \
    'http://localhost:8080/api/1/simple-handler/KEY'
```

Example:

```bash
curl \
    -X POST \
    --data '{"first_value": 10.46737, "second_value": "5.66473", "third_value": "hello"}' \
    'http://localhost:8080/api/1/simple-handler/my_key'
```

As you can check in `tornado-pycassa-handler/db.py`,
every inserted value is identified by:
 * a key (the `key` field),
 * a composite identifier (the `column1` and `column2` fields)

When inserting data, if the given `key`:`column1`:`column2` already exists,
the existing value is overwritten.


## Check modifications into Cassandra

Connect to the Cassandra container:

```bash
docker exec -it tornado-pycassa-cassandra_cassandra /bin/bash
```

Go into the column family of the keyspace:

```bash
cqlsh
use "KeySpace";
SELECT * FROM "ColumnFamily";
```

======
Munger
======


This is my project to build an automatic data munger with a web based
interface.

- Install and run RethinkDB_

.. _RethinkDB: http://rethinkdb.com/

- Set up a Tornado web app with interface

- Enable upload file to Rethink

  Can we stream the upload?

- Trigger asynchronous task (using, e.g. Celery?) to analyse the data

  Use jsonschema inference tools to derive the schema

- The UI updates real time when the shema is available, asynchronouly


Subsequent ideas include usig the schema information to:

- infer what graphs to show
- trigger other analyses

------------
Dependencies
------------

- `docker copose`__  

__ https://docs.docker.com/compose/

---
Use
---

At the moment all it does is start RethinkDB::

    cd docker
    docker-compose up

That's it. The log messages will tell you which
ip address it's listening to.::

    Recreating docker_rethinkdb_1...
    Attaching to docker_rethinkdb_1
    rethinkdb_1 | Running rethinkdb 2.0.3~0jessie (GCC 4.9.1)...
    rethinkdb_1 | Running on Linux 3.19.0-26-generic x86_64
    rethinkdb_1 | Loading data from directory /data/rethinkdb_data
    rethinkdb_1 | Listening for intracluster connections on port 29015
    rethinkdb_1 | Listening for client driver connections on port 28015
    rethinkdb_1 | Listening for administrative HTTP connections on port 8080
    rethinkdb_1 | Listening on addresses: 127.0.0.1, 172.17.0.8, ::1, fe80::42:acff:fe11:8%23
                                                     ^^^^^^^^^^
    rethinkdb_1 | Server ready, "3cc87f5fc12d_8ya" e659b757-081c-4265-901a-ed5eaf8b3c68
    rethinkdb_1 | A newer version of the RethinkDB server is available: 2.1.3. You can read the changelog at <https://github.com/rethinkdb/rethinkdb/releases>.

So we can access the RethinkDB admin at::

    http://172.17.0.8:8080/


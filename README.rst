Munger
======


This is my project to build an automatic data munger with a web based interface.

- Install RethinkBD 
  We should use docker to set this up, and maybe the fig tool to link to other parts of the system

- Set up a Tornado web app with interface

- Enable upload file to Rethink

  Can we stream the upload?

- Trigger asynchronous task (using, e.g. Celery?) to analyse the data

  Use jsonschema inference tools to derive the schema

- The UI updates real time when the shema is available, asynchronouly


Subsequent ideas include usig the schema information to:

- infer what graphs to show
- trigger other analyses



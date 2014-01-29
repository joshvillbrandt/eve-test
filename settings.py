# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2013 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# Running on local machine. Let's just use the local mongod instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'versioning_test_3'
XML = False

# let's not forget the API entry point
# SERVER_NAME = '0.0.0.0:5000'
URL_PREFIX = 'api'
API_VERSION = 'v0'
X_DOMAINS = '*'
X_HEADERS = ['Content-Type', 'If-Match'] #'X-HTTP-Method-Override'

# http://python-eve.org/config.html#global-configuration
LAST_UPDATED = '_modified_at'
DATE_CREATED = '_created_at'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE'] #PUT

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=0'
CACHE_EXPIRES = 0

DEBUG = True

todos = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'item_title': 'todo', # this isn't doing what i expected it to do
    'versioning': True,
    'schema': {
        'title': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 255,
            'required': True,
            'versioned': False,
        },
        'description': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1023,
        }
    }
}

users = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 255,
            'required': True,
        }
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'todos': todos,
    'users': users,
}

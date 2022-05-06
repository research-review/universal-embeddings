# This file contains public configuration (do not insert passwords etc.)
# Copy this file into the 'instance' directory to enable usage.

# Elasticsearch
ES_HOST       = 'https://localhost:9200/'
ES_USER       = 'elastic'
ES_PASSWORD   = '123123'
ES_INDEX      = 'index_test'

# Webservice password.
# Generate with scripts/generate-salt-password.py
SALT          = b'\x02\xee\xc9\\\x16\xbf\xb3;s\xc8N\x97\x1c\xbcv%\tE!\x81n\xe8z{\x1f\xd0\xcfQXw\x9a1'
PSW_SALT_HASH = b"\xbf\xf4D\xd1mq\xeas\x83\xd0PNR\xa3DJ\xddo\x12\x9b\xf3\xa6\xff'\xaf\xb5\xb7$\xcf{\x8dK"
# 123123

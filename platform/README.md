# Universal Knowledge Graph Embeddings

This repository contains code to run [embeddings.cc](https://embeddings.cc/) and [embeddings.cs](https://embeddings.cs:8443/) ([without TLS](http://embeddings.cs.uni-xxx.de/)).

## Documentation

### Public API (for users)

- The API is documented at [embeddings.cc/api](https://embeddings.cc/api)
- Additional examples are provided in [Python examples](api/embeddings_cc_public_examples.py) and [JavaScript HTML form](api/embeddings_cc_public.htm)

### Index API (for universal embeddings developers)

- Use the Index API to create Elasticsearch indexes and to **add data**.
- It is only available in uni network (use **VPN**).
- It can easily accessed via the [API python file](api/embeddings_cc_index.py).
- Usage examples are provided in the [examples python file](api/embeddings_cc_index_examples.py) and
  in the [CSV example python file](api/embeddings_cc_index_csv.py).
- **Important**: Create an alias for each index to be available in public. Only aliases can be accessed by webservices.

| Webservice      | Method | Parameters                          |
|-----------------|--------|-------------------------------------|
| /ping           | GET    | -                                   |
| /count          | GET    | index                               |
| /get_embeddings | GET    | index, entity                       |
| /get_indexes    | POST   | password                            |
| /create_index   | POST   | password, index, dimensions, shards |
| /delete_index   | POST   | password, index                     |
| /add            | POST   | password, index, docs               |

### System administration

- [Virtual machine](docs/vm.md) (Installation and deployment)
- [VM nginx](docs/vm-nginx-certbot.md) (Webserver configuration)
- [Development](docs/development.md) (External documentation of integrated components)
- [Deployment](docs/deployment.md) (How to publish a new version)
- Note: This is an extension of [kg-embedding-service](https://github.com/xxx-group/kg-embedding-service)

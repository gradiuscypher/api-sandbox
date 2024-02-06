# api-sandbox
Examples of building an API in Python.

# running the examples
```
❯ poetry run cli test 13.37 "this is an item"
{'item_name': 'test', 'item_desc': 'this is an item', 'item_price': 13.37, 'is_special': False}

❯ poetry run cli special 13.37 "this is an item"
{'item_name': 'special', 'item_desc': 'this is an item', 'item_price': 13.37, 'is_special': True}

❯ poetry run cli protected
401 {'detail': 'Invalid API key'}

❯ poetry run cli protected --empty
401 {"detail":"Invalid API key"}

❯ poetry run cli protected --pass
{'message': 'Nice API key'}
```

# vscode configuration
## editor type checking
- install Pylance
- set `"python.analysis.typeCheckingMode": "basic"` in `settings.json`

# neat FastAPI features
- [Depends](https://fastapi.tiangolo.com/reference/dependencies/)
- [ApiRouter](https://fastapi.tiangolo.com/reference/apirouter/)
- [Override request validation](https://fastapi.tiangolo.com/tutorial/handling-errors/#override-request-validation-exceptions)

# things I'd like to add in the future
- protected route with Depends
- ODM using [beanie](https://beanie-odm.dev/)
- docker container with full example flow, including cli as command pre-installed

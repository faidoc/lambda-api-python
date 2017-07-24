# Test API for Amazon Lambda written in Python
Developed in Python + Flask + Flask RESTful running on Amazon Lambda + API Gateway.


## File structure

```GAP
├─ api/         # All application code in this directory.
│  └─ v1/
│     ├─ base/
│     │  └─ decorators.py
│     │
│     ├─ endpoint1/
│     │  └─ resources.py
│     ├─ endpoint2/
│     │  └─ resources.py
│     │
│     ├─ blueprints.py
│     └─ extensions.py
│
│
├─ config.py
│
└─ application.py          # Main entry-point into the Flask application.
```

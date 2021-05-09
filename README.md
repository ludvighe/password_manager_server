# Password Manager REST API / server

Meant to serve as backend for a [password manager app](https://github.com/ludvighe/murmelpass).

# 1. Use

## 1.1 Initialize database
```bash
sqlite3 app/db/db.sqlite < app/db/db.sqlite.init
```

## 1.2 Run
```bash
# Either 
./venv/bin/python3.8 run.py

# Or
./venv/bin/activate
python3.8 run.py
```

# 2. Requests

*Note: Every request except /register requires api key.*

## 2.1 User
**Register new user**

```
POST /reqister
```

```json
Payload: 
{"name": [unique string], "email": [unique string]}
```

**Get user**

```
GET /user?key=YOUR_API_KEY
```

**Update user information**

```
PUT /user?key=YOUR_API_KEY
```

```json
Payload:
{"name": [unique string], "email": [unique string]}
```

**Delete user**

```
DELETE /user?key=YOUR_API_KEY
```

*Note: This will also delete all associated password data.*

<br>

## 2.2 Password Data

**Create password data**

```
POST /pwdata?key=YOUR_API_KEY
```

```json
Payload: 
{
    "title": [string],
    "salt": [string],
    "count": [int],
    "length": int,
    "created": [string],
    "last_used": [string]
}
```

**Get all password data**

```
All associated with user: 
GET /pwdata?key=YOUR_API_KEY
```

```
Specific: 
GET /pwdata?key=YOUR_API_KEY&id=PASSWORD_DATA_ID
```

**Update password data**

```
PUT /pwdata?key=YOUR_API_KEY&id=PASSWORD_DATA_ID
```

```json
Payload: 
{
    "title": [string],
    "salt": [string],
    "count": [int],
    "length": int,
    "created": [string],
    "last_used": [string]
}
```

**Delete password data**

```
DELETE /pwdata?key=YOUR_API_KEY&id=PASSWORD_DATA_ID
```

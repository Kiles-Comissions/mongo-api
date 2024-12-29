# mongo api
 A clone of the deprecated mongoDB API which allows modifying you database through an API

## General request body
Generally, every request needs `collection` argument. This is so it knows which collection to apply the search/modification to. The Database will always be the one specified when starting the API because it is assumed it will always be the same. Below you can find a destinction between the two:

![image](https://github.com/user-attachments/assets/d58b6ab0-17a5-45d2-b388-7421bfe2e192)


So every request will need 
```js
{
  "collection": "<collection_name>"
}
```
in it's request body. I won't include this in the request details below so keep that in mind. You can also optionally specify the `database` in the request body if you want to change the database from the default one.

> [!TIP] 
> Generally the difference between `operationOne` and `operationMany` is that the former will only apply to the first document that matches the filter, while the latter will apply to all documents that match the filter. For `find` one will also return a single JSON object, while the other will return an array of JSON objects. Generally only use `operationOne` when the filter is unique, such as an ID, otherwise use `operationMany`.

The request is meant to mirror the actual mongodb operation as closely as possible so what mongoDB returns is what you should expect from the API. 
This also allows for the use of special mongodb operators in the request body. Where applicable, I will provide a link to the documentation for the operators used. You only *need* to use these for `update` (`$set`) and `aggregate` (`$match`, `$group`, etc) operations.

## Individual request bodies

## Index
- [find](#find)
- [findOne](#findOne)
- [insertOne](#insertOne)
- [insertMany](#insertMany)
- [updateOne](#updateOne)
- [updateMany](#updateMany)
- [deleteOne](#deleteOne)
- [deleteMany](#deleteMany)
- [aggregate](#aggregate)

### `/find`
type: `POST`
#### Request

```js
{
  "filter": {
    "key": "value"
  }
}
```

#### Response
```js
[
    {
        "key": "value", // It will return all the documents that match the filter
        "other_data": "other_value"
        // ...
    },
    {
        "key": "value",
        "other_data": "other_value"
        // ...
    }
]
```

#### Example
```js
{
  "collection": "users",
  "filter": {
    "name": "John",
    "age": {
        "$gt": 20
    }
  }
}
```

> [!NOTE] 
> You can use special mongodb search operators in the filter object. For example, the `$gt` operator in the example above. You can find more about these operators [here](https://docs.mongodb.com/manual/reference/operator/query/)

### `/findOne`
type: `POST`
#### Request
```js
{
  "filter": {
    "key": "value"
  }
}
```

#### Response
```js
{
    "key": "value", // It will return the first document that matches the filter
    "other_data": "other_value"
    // ...
}
```

#### Example
```js
{
  "collection": "users",
  "filter": {
    "name": "John",
    "age": {
        "$gt": 20
    }
  }
}
```

> [!NOTE] 
> You can use special mongodb search operators in the filter object. For example, the `$gt` operator in the example above. You can find more about these operators [here](https://docs.mongodb.com/manual/reference/operator/query/)

### `/insertOne`
type: `POST`
#### Request
```js
{
  "document": {
    "key": "value"
  }
}
```
#### Response
```js
{
    "_id": "676fe5b60fa547b0c8fa8148" // The generated id of the inserted document
}
```

#### Example
```js
{
  "collection": "users",
  "document": {
    "name": "John",
    "age": 25
  }
}
```

### `/insertMany`
type: `POST`
#### Request
```js
{
  "documents": [
    {
      "key": "value"
    },
    {
      "key": "value"
    }
  ]
}
```
#### Response
```js
[
    {
        "_id": "676fe5b60fa547b0c8fa8148" // The generated id of the first inserted document
    },
    {
        "_id": "676fe5b60fa547b0c8fa8149" // The generated id of the second inserted document
    }
]
```

#### Example
```js
{
  "collection": "users",
  "documents": [
    {
      "name": "John",
      "age": 25
    },
    {
      "name": "Jane",
      "age": 30
    }
  ]
}
```

### `/updateOne`
type: `POST`
#### Request
```js
{
  "filter": {
    "key": "value"
  },
  "update": {
    "$set": {
      "key": "value"
    }
  }
}
```

#### Response
```js
{
    "$clusterTime": {
        "clusterTime": 1735386694,
        "signature": {
            "hash": "<hash>",
            "keyId": 7393337599319867616
        }
    },
    "electionId": "7fffffff0000000000000416",
    "n": 1, // The number of documents that were found with the filter
    "nModified": 1, // The number of documents that were modified
    "ok": 1.0, // If the operation was successful
    "opTime": { 
        "t": 1046,
        "ts": 1735386694
    },
    "operationTime": 1735386694, // The time the operation was executed
    "updatedExisting": true 
}
```

#### Example
```js
{
  "collection": "users",
  "filter": {
    "name": "John"
  },
  "update": {
    "$set": {
      "name": "Johnny"
    },
    "$inc": { // You can use multiple update operators
      "age": 1
    }
  }
}
```

> [!NOTE] 
> You can use special mongodb update operators in the update object. For example, the `$set` and `$inc` operators in the example above. You can find more about these operators [here](https://docs.mongodb.com/manual/reference/operator/update/)

### `/updateMany`
type: `POST`
#### Request
```js
{
  "filter": {
    "key": "value"
  },
  "update": {
    "$set": {
      "key": "value"
    }
  }
}
```

#### Response
```js
{
    "$clusterTime": {
        "clusterTime": 1735386694,
        "signature": {
            "hash": "<hash>",
            "keyId": 7393337599319867616
        }
    },
    "electionId": "7fffffff0000000000000416",
    "n": 1, // The number of documents that were found with the filter
    "nModified": 1, // The number of documents that were modified
    "ok": 1.0, // If the operation was successful
    "opTime": { 
        "t": 1046,
        "ts": 1735386694
    },
    "operationTime": 1735386694, // The time the operation was executed
    "updatedExisting": true 
}
```

#### Example
```js
{
  "collection": "users",
  "filter": {
    "name": "John"
  },
  "update": {
    "$set": {
      "name": "Johnny"
    },
    "$inc": { // You can use multiple update operators
      "age": 1
    }
  }
}
```

> [!NOTE] 
> You can use special mongodb update operators in the update object. For example, the `$set` and `$inc` operators in the example above. You can find more about these operators [here](https://docs.mongodb.com/manual/reference/operator/update/)

### `/deleteOne`
type: `POST`
#### Request
```js
{
  "filter": {
    "key": "value"
  }
}
```

#### Response
```js
{
    "$clusterTime": {
        "clusterTime": 1735229323,
        "signature": {
            "hash": "<hash>",
            "keyId": 7393337599319867616
        }
    },
    "electionId": "7fffffff0000000000000416",
    "n": 1, // The number of documents that were found with the filter
    "ok": 1.0, // If the operation was successful
    "opTime": {
        "t": 1046,
        "ts": 1735229323
    },
    "operationTime": 1735229323 // The time the operation was executed
}
```

#### Example
```js
{
  "collection": "users",
  "filter": {
    "name": "John"
  }
}
```

### `/deleteMany`
type: `POST`
#### Request
```js
{
  "filter": {
    "key": "value"
  }
}
```

### Response
```js
{
    "$clusterTime": {
        "clusterTime": 1735229323,
        "signature": {
            "hash": "<hash>",
            "keyId": 7393337599319867616
        }
    },
    "electionId": "7fffffff0000000000000416",
    "n": 1, // The number of documents that were found with the filter
    "ok": 1.0, // If the operation was successful
    "opTime": {
        "t": 1046,
        "ts": 1735229323
    },
    "operationTime": 1735229323 // The time the operation was executed
}
```

#### Example
```js
{
  "collection": "users",
  "filter": {
    "name": "John"
  }
}
```

### `aggregate`
#### Request
```js
{
  "pipeline": [
    {
      "$match": {
        "key": "value"
      }
    },
    {
      "$group": {
        "_id": "$key",
        "count": {
          "$sum": 1
        }
      }
    }
  ]
}
```

#### Response
```js
[
    {
        "_id": "value",
        "count": 1
    }
]
```

#### Example
```js
{
  "collection": "users",
  "pipeline": [
    {
      "$match": {
        "name": "John"
      }
    },
    {
      "$group": {
        "_id": "$name",
        "count": {
          "$sum": 1
        }
      }
    }
  ]
}
```

> [!NOTE] 
> You can use special mongodb aggregation operators in the pipeline array. For example, the `$match` and `$group` operators in the example above. You can find more about these operators [here](https://docs.mongodb.com/manual/reference/operator/aggregation/)

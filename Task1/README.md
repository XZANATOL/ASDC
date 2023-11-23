## Getting Started

Exceute the following commands:
```bash
pip install pdm
pdm install
pdm run makemigrations
pdm run migrate
pdm run dev
```

Server will run on [http://localhost:8000/](http://localhost:8000/)

## Status Codes

* `200`: success
* `400`: invalid request (body)
* `404`: record not found
* `405`: invalid method

## Endpoints

**POST** `/upload/`

Endpoint will populate recieved data removing Nan rows and saves the data into the database. It returns records that have been successfully saved.

* `<filename>`: `File Object`

**Response**
```json
[
	{
	    "name": "Zephyr",
	    "description": "Gentle Breeze Power",
	    "location": "Island Cove",
	    "price": 199.0,
	    "color": "Peach"
	},
	{
	    "name": "Zephyr",
	    "description": "Gentle Breeze Power",
	    "location": "Island Cove",
	    "price": 199.0,
	    "color": "Peach"
	}
]
```
<hr>

**GET** `/query/<int:id>`

Query's record based on its ID.

**Response**
```json
{
    "name": "Zephyr",
    "description": "Gentle Breeze Power",
    "location": "Island Cove",
    "price": 199.0,
    "color": "Peach"
}
```
<hr>

**PUT** `/update/<int:id>`

Query's record based on its ID, and updates it based on the provided body formated like below. It returns the updated record upon successful validation.

* `name`: `str`
* `description`: `str`
* `location`: `str`
* `price`: `float`
* `color`: `str`

**Response**
```json
{
    "name": "XZANATOL",
    "description": "Gentle Breeze Power",
    "location": "Island Cove",
    "price": 199.0,
    "color": "Peach"
}
```
<hr>

**DELETE** `/delete/<int:id>`

Query's record based on its ID and deletes it. It returns the deleted record upon sucessful deletion.

**Response**
```json
{
    "name": "XZANATOL",
    "description": "Gentle Breeze Power",
    "location": "Island Cove",
    "price": 199.0,
    "color": "Peach"
}
```
<hr>
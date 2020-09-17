# ZipAirlines

This is an API for assessing 10 different airplanes for ZipAirlines.

### Installation

Clone the repository

```sh
$ git clone https://github.com/junccueto/ZipAirlines.git
```

Install dependencies:

```sh
$ cd ZipAirlines
$ pip install -r requirements.txt
```

Start the server:

```sh
$ cd ZipAirlines
$ python manage.py runserver
```

### Endpoints

##### '/assess'

-   Endpoint used to assess the airplanes.
-   Request Type: POST
-   Requires an exact number of 10 airplane data to assess
-   Airplane data should contain id and passengers, both are integers
-   Sample input:

```json
[
	{
		"id": 1,
		"passengers": 10
	},
	{
		"id": 2,
		"passengers": 20
	},
	{
		"id": 3,
		"passengers": 30
	},
	{
		"id": 4,
		"passengers": 40
	},
	{
		"id": 5,
		"passengers": 50
	},
	{
		"id": 6,
		"passengers": 60
	},
	{
		"id": 7,
		"passengers": 70
	},
	{
		"id": 8,
		"passengers": 80
	},
	{
		"id": 9,
		"passengers": 90
	},
	{
		"id": 10,
		"passengers": 100
	}
]
```

-   Sample Output:

```json
[
	{
		"id": 1,
		"passengers": 10,
		"fuel_tank_capacity": 200,
		"fuel_consumption_per_minute": 0.02,
		"max_flight_time": 10000
	},
	{
		"id": 2,
		"passengers": 20,
		"fuel_tank_capacity": 400,
		"fuel_consumption_per_minute": 0.2808239965311849,
		"max_flight_time": 1424.3797002425356
	},
	{
		"id": 3,
		"passengers": 30,
		"fuel_tank_capacity": 600,
		"fuel_consumption_per_minute": 0.44169700377572996,
		"max_flight_time": 1358.3972607263775
	},
	{
		"id": 4,
		"passengers": 40,
		"fuel_tank_capacity": 800,
		"fuel_consumption_per_minute": 0.5616479930623698,
		"max_flight_time": 1424.3797002425356
	},
	{
		"id": 5,
		"passengers": 50,
		"fuel_tank_capacity": 1000,
		"fuel_consumption_per_minute": 0.659176003468815,
		"max_flight_time": 1517.0455155188445
	},
	{
		"id": 6,
		"passengers": 60,
		"fuel_tank_capacity": 1200,
		"fuel_consumption_per_minute": 0.7425210003069148,
		"max_flight_time": 1616.115907164902
	},
	{
		"id": 7,
		"passengers": 70,
		"fuel_tank_capacity": 1400,
		"fuel_consumption_per_minute": 0.8160784320114054,
		"max_flight_time": 1715.5213826070506
	},
	{
		"id": 8,
		"passengers": 80,
		"fuel_tank_capacity": 1600,
		"fuel_consumption_per_minute": 0.8824719895935548,
		"max_flight_time": 1813.0887086137673
	},
	{
		"id": 9,
		"passengers": 90,
		"fuel_tank_capacity": 1800,
		"fuel_consumption_per_minute": 0.94339400755146,
		"max_flight_time": 1908.004487617878
	},
	{
		"id": 10,
		"passengers": 100,
		"fuel_tank_capacity": 2000,
		"fuel_consumption_per_minute": 1,
		"max_flight_time": 2000
	}
]
```

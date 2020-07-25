# social91

First run the Django REST server
  ```
  python manage.py runserver
  ```
Run the threaded request script with takes input from input.json and sends threaded requests to server with maximum number of worker threads set to 10
  ```
  python threaded_request.py input2.json
  ```
Input json data format is assumed to be like below:
  ```json
  {
  "date" : "2013-01-06",
  "name" : "cycle1",
  "components" : {
  "frame" : ["top_tube", "down_tube", "seat_tube"],
  "wheel" : ["spokes", "hub", "rim"],
  "seat" : ["saddle"],
  "handlebar" : ["handlebar_grip", "fork"],
  "chain" : ["chain", "chain_rings"]
  }
  }
  ```

Output is a json data consisting of the following fields:
  ```
  {'name': 'cycle1', 'date': '2013-01-06', 'frame': 111, 'wheel': 163, 'seat': 82, 'handlebar': 133, 'chain': 162, 'total': 651, 'status': 'Found'}
  ```
  
denoting the individual price of each high level component and total price of cycle denoted by name and query date.

Unit tests can be done by running

```
python manage.py test
```



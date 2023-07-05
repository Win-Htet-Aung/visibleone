# Coding test from Visible One
This repo includes the solutions to the problems from a coding test assigned by **Visible One**.

## No. 1 Script for the vending machine
The script's name is **vending_machine.py**.

### Running the script
run the following command:
```python vending_machine.py```

## No. 2 Create an API with Django
The goal is to create an API which returns a JSON response with data loaded from a csv file. The project folder is named **DjangoAPI**

### Running the project
run the following commands:
```
pip install -r requirements.txt
cd DjangoAPI
python manage.py migrate
# load data from csv file to database
python manage.py load_challenges
python manage.py runserver
```
the server will be running at http://localhost:8000.

### The API routes
- **Endpoint** : [GET] http://localhost:8000/api/challenges
- **Response** : 
```
{
	"challenges": [
		{
			"ChallengeID": 1,
			"ChallengeName": "Write Python Script",
			"ChallengeSucessRate": "50.00"
		},
		{
			"ChallengeID": 2,
			"ChallengeName": "Sample HTML development",
			"ChallengeSucessRate": "100.00"
		},
		{
			"ChallengeID": 3,
			"ChallengeName": "Setup web server",
			"ChallengeSucessRate": "80.00"
		}
	]
}
```

## No. 3 Adding GraphQL in No. 2

### Running the project
It's the same as steps in No. 2.

### The API routes
- **Endpoint** : [POST] http://localhost:8000/graphql
- **Request Body** : ```{"query":"{challenges{ChallengeID,ChallengeName,ChallengeSucessRate}}"}```
- **Headers** : 
	- Content-Type : application/json
- **Response** : 
```
{
	"data": {
		"challenges": [
			{
				"ChallengeID": 1,
				"ChallengeName": "Write Python Script",
				"ChallengeSucessRate": "50.00"
			},
			{
				"ChallengeID": 2,
				"ChallengeName": "Sample HTML development",
				"ChallengeSucessRate": "100.00"
			},
			{
				"ChallengeID": 3,
				"ChallengeName": "Setup web server",
				"ChallengeSucessRate": "80.00"
			}
		]
	}
}
```

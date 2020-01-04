# Project Title

WorldOfGames project contains a package of two games:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer

In addition, it contains:
dockerfile - for building a docker image, with all required prerequisites;
docker-compose file - for deploing a docker;
jenkinsfile - for automating building, deploying and testing the project


### Prerequisites

For running a game app, you will need a python installed:
pip install python

for testing:
selenium
flask
chromedriver
chrome
xvfb


### Installing

To install and run on the local host:
1. download the repository
2. run "python mainscore.py"
3. access 127.0.0.1:8777 to get a user's score

To install and run on docker run (from within a project directory where docker-compose file resides):
1. docker-compose build
2. docker-compose up
3. to play the game, run bash on the docker:
	1. docker exec -it <docker id/name> bash
	2. $ python mainscore.py

## Running the tests

This package contains one e2e test, which tests the score web service. To run the test locally:
1. python e2e.py

To run the test on docker:
1. docker exec -it <docker id/name> bash
2. $ python e2e.py

Or use Jenkinsfile for building an automated test.

This test selects the score element in the web page, check that it is a number between 0 to 1000 and return an 0 if it's and -1 otherwise.

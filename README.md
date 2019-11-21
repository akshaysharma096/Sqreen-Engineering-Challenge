# Sqreen-Engineering-Challenge
<div align="center">
  <img src="https://warehouse-camo.cmh1.psfhosted.org/ff0cff6b90e14dae12ba8f267acc4694632db0cf/68747470733a2f2f73717265656e2d6173736574732e73332d65752d776573742d312e616d617a6f6e6177732e636f6d2f6c6f676f732f73717265656e2d6c6f676f2d3236342d312e737667"><br><br>
</div>

### What is this repository for? / Scenario ###

This repository showcases the solution to the coding challenege given by [Sqreen](https://www.sqreen.com/) to me as a part of the interview process.

- On receiving a notification the application should
    - Check that the signature is correct.
    - Redispatch the notification to multiple targets (e.g. log, email, HTTP, SMS, Slack).
    

### Project Details ###

The project requires the candidate to build a flask app, that listens for webhook notifications from Sqreen. Here the details about the project
  
 - The project is built using Python 3.6+, pyest as the testing framework.
 
 - *We don't particularly need two apps (one to be attacked [but sqreened] & one to receive notifications) but can use the same app to do both, this has been solved by parsing the incoming notifications, if **application_id** in notification JSON represents the application which is receiving notifications, this means our server has a security issue*.
  - If a such a scenario arises, apart from dispatching notification to the target backends, we also notify the admins of the server or application using the available backends we have like SMS, EMAIL, SLACK etc, as well also tag the logs with a tag: ***[INTENAL SECURITY ALERT]***
    - Example: ```2019-11-21 05:24:21,308: INFO]: [INTERNAL SECURITY ALERT]: {'humanized_title': 'Massive account takeover attempts on user@example.com', 'pulse_genre': 'account_takeover', 'environment': 'production', 'date_started': '2019-11-20T21:47:00.090825+00:00', 'date_ended': None, 'blocked': True, 'url': 'https://my.sqreen.com/application/5dd058775c3feb0021c0bb43/pulses/5dd5b454e56c7e0024169b4b'} ```
 
 - I have used to celery to process notifications dispatch to different backends, because the code has been written by keeping in mind I am actually building an app for production ready use. RabbitMQ has been used the broker for Celery. Each component can be scaled separately.
 
 - **flaskr** is the project directory which contains the application code for our server.
 
 - **flaskr/tests** is the project directory which contains the tests.
 
 - **flaskr/utils** module contains helper classes used to for verifying the signature of an incoming request and processing and dispatching the incoming notifciation to target backends.
 
 - **flaskr/config.py**, has project wide configurations and constants.
 
 - API for this project has been versioned, the **flaskr/v1** folder the concerned controller and decorators used to handle the incoming request.
 
 - The end-point for the webhook is ```https://{{host_url}}/v1/webhook```, it listens for a POST request
   - A valid incoming request will be responded with a response code of ```200 - OK``` , otherwise if the the request does have the required header or the header is wrong, API responds with the response code of ```401 - UnAuthorized``` or if the structure of request is wrong the API responds with response code of ```422 - Unprocessable Entity```.
 
 - There is a generic interface for dispatching a notification to target backends, named: ```TaskProcessor``` this class abstracts the process of dispatching an incoming notification from Sqreen. You can find the ```TaskProcessor``` class [here](https://github.com/akshaysharma096/Sqreen-Engineering-Challenge/blob/master/flaskr/utils/task_processing.py).
 
 - There is a generic interface for target backends, named: ```BackendProcessor``` this class abstracts the process of dispatching an incoming notification from Sqreen. You can find the ```BackendProcessor``` class [here](https://github.com/akshaysharma096/Sqreen-Engineering-Challenge/blob/master/flaskr/backends/backend_processor.py).
 
 - As per the implementation details of the target backends, i.e: how will the notifcation will be send to backends like: SMS, SLACK or EMAIL, each backend has a specific ***{Backend}Manager*** class. The implementation of sending notification to a specific Backend has not been implemented but a basic code structure has been done, as it was in the scope of the task. 

- There are two types of test written.
  - Functional tests, that tests the overall functionality of our API.
  - Unit tests, that tests the a single module over various test cases. 
  - Pytest is the testing framework used.
 
 
### Akshay's Notes ###

- Incoming request has been considered of JSON format, with content-type as ```application/json```
- Since the incoming request contains a collection of events, a JSON request that is not an array will be rejected with ```response code - 422, Unprocessable Entity.```.
- The problem has been solved by building it as a production ready software.
- The code has been made modular by methods to carry out small tasks, this makes it easy to read as well as easily debuggable.
- The code runs with a runtime complexity of O(n), where n is the number of events passed in the incoming JSON.


### How to run ###
- Put your signature key in the local environment under: ```SIGNATURE_KEY```.
- Put your app token from sqreen in the local environment under```SQREEN_TOKEN```.
- Put your application id from sqreen dashboard in the local environment under: ```SCREEN_APPLICATION_ID```
- Put your application name from sqreen dashboard under: ```SQREEN_APP_NAME```.
- Create a virtual environment, by ```virtualenv venv```.
- ```$ source venv/bin/activate```.
- Install the requirements from requirements.txt
- In the root directory of the project, to run the flask server.
  - ```export FLASK_APP=flaskr```
  - ```export FLASK_ENV=production/development```
  - ```flask run```
  - Logs will be stored in ```logs/server.log```
  
- To run celery.
  - ```$ rabbitmq-server```
  - In the root directory of the project, to run the celery worker.
   - ```$ celery -A flaskr.celery.tasks worker --loglevel=info -f logs/celery.log```
  -  Logs will be stored in ```logs/celery.log```


- To run tests.
  - Once all above steps are completed.
  - ```$ pyest```



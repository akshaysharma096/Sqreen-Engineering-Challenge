# Sqreen-Engineering-Challenge
<div align="center">
  <img src="https://warehouse-camo.cmh1.psfhosted.org/ff0cff6b90e14dae12ba8f267acc4694632db0cf/68747470733a2f2f73717265656e2d6173736574732e73332d65752d776573742d312e616d617a6f6e6177732e636f6d2f6c6f676f732f73717265656e2d6c6f676f2d3236342d312e737667"><br><br>
</div>

### What is this repository for? ###

This repository showcases the solution to the coding challenege given by [Sqreen](https://www.sqreen.com/) to me as a part of the interview process.

### Project Details ###

The project requires the candidate to build a flask app, that listens for webhook notifications from Sqreen. Here the details about the project
  
 - The project is built using Python 3.6+, pyest as the testing framework.
 
 - I have used to celery to process notifications dispatch to different backends, this has been chosen by keeping in mind the use case that, the code has been written by keeping in mind I am actually building an app for production ready use. RabbitMQ has been used the broker for Celery.
 
 - **flaskr** is the project directory which contains the application code for our server.
 
 - **flaskr/utils** module contains helper classes used to for verifying the signature of an incoming request and processing and dispatching the incoming notifciation to target backends.
 
 - **flaskr/config.py**, has project wide configurations and constants.
 
 - API for this project has been versioned, the **flaskr/v1** folder the concerned controller and decorators used to handle the incoming request.
 
 - The end-point for the webhook is ```https://{{host_url}}/v1/webhook```, it listens for a POST request
   - A valid incoming request will be responded with a response code of ```200 - OK``` , otherwise if the the request does have the required header or the header is wrong, API responds with the response code of ```401 - UnAuthorized``` or if the structure of request is wrong the API responds with response code of ```422 - Unprocessable Entity```.
 
 - There is a generic interface for dispatching a notification to target backends, named: ```TaskProcessor``` this class abstracts the process of dispatching an incoming notification from Sqreen. You can find the ```TaskProcessor``` class [here](https://github.com/akshaysharma096/Sqreen-Engineering-Challenge/blob/master/flaskr/utils/task_processing.py).
 
 - There is a generic interface for target backends, named: ```BackendProcessor``` this class abstracts the process of dispatching an incoming notification from Sqreen. You can find the ```BackendProcessor``` class [here](https://github.com/akshaysharma096/Sqreen-Engineering-Challenge/blob/master/flaskr/backends/backend_processor.py).
 
 - As per the implementation details of the target backends, i.e: how will the notifcation will be send to backends like: SMS, SLACK or EMAIL, each backend has a specific ***{Backend}Manager*** class. The implementation of sending notification to a specific Backend has not been implemented but a basic code structure has been done, as it was in the scope of the task. 
 

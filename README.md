# kanjelper

This project takes a kanji list from my JAPAN 301 class and finds readings for each kanji.
The data/readings is stored in an Amazon DynamoDB.

## Setup

Run aws configure. 

`aws configure`

If running a local DynamoDB instance, run before starting the app.

`java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb`
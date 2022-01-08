
# Pokemon game

![logooo](https://user-images.githubusercontent.com/74601548/148529725-cce3981f-d331-4a88-802b-95d1e397a293.png)
## Introduction
In this project we were created and designed a Pokemon game.
The game is structured so that a directed weighted graph is given (you can read about that here: https://en.wikipedia.org/wiki/Directed_graph)
 And given a list of Pokemons (with different values ​​for each) that are located on the edges of the graph. 

The main goal of the game - locate the agents who capture the pokemons and make the agent walk so that they capture as many pokemons as possible at high values, it means, maximize the overall score of the captured pokemons.

The game has different cases that are different in their attributes like: the struct of the graph, the position of the pokemons, the number of agents and their speed.

Below: An image of the Pokemon agent! ('Ash Ketchum', in the series),:

![ash](https://user-images.githubusercontent.com/74601548/148528833-c60c78e7-c361-4fe5-a2c9-608bf6ba4296.png)

An image of our game Pokemons: in yellow-'Pikachu' , in orange-'Charmander' .


![image](https://user-images.githubusercontent.com/74601548/148529412-076466cf-69ee-424a-81c3-e58b69ab3690.png)



The graph in the game is a directed graph, so, we differ in the GUI between yellow Pokemons placed on descending edges (the id of the source vertex is higher than the destination vertex) and orange pokemon placed on ascending edges.

## That's how the game GUI looks like:

A short clip (case 11) in live version:

https://user-images.githubusercontent.com/74601548/148662171-daa7beac-f887-46c0-87ae-9fc20be21a24.mp4

And for download:
[Screen Recording - Made with RecordCast.zip](https://github.com/ChaimW25/Ex4/files/7834136/Screen.Recording.-.Made.with.RecordCast.zip)


A screenshot of case 1:
![image](https://user-images.githubusercontent.com/74601548/148536180-e9859187-47aa-4045-8161-1def0ff25d2f.png)

## A bit about what we've done in this project:

We have written an algorithm that maximize the grades of the agents in capturing the pokemons in the different cases and difficulty levels. In addition, we have created a GUI (Graphical user interface) for the game that illustrates the original characters in the 'Pokemon' series.

The game is running by communication with a server (link to server here: https://github.com/ChaimW25/Ex4/blob/master/Ex4_Server_v0.0.jar ). That's how it works: the server writes us a script of different cases and different levels in the game and we send our code algorithm to the server and running the game. Meanwhile, We can watch the GUI of the game and watch the info results that printed in our IDE.

## A view to our code:
For the purpose of using a directed weighted graph we have expanded the skeleton we have already created in a previous projects. Please have a short look in our 'Directed Weighted Graph' projects:

In Python- https://github.com/ChaimW25/Ex3.git
 
And in Java- https://github.com/ChaimW25/ex2.git

To get a width picture of the project we recommend you take a look at the UML diagram we have attached below.
As already mentioned the project is built on the infrastructure we created in the previous project. This allows us to receive the data about the graphs in the game from the server and to manage them optimally on the various functions and algorithms we've already written.

We've added additional classes for creating game-related objects like Pokemon, Agents and GameInfo.
The department that connects all the departments related to the game is the GameManager and it actually communicates in addition with the departments that are related to the graph, and basically, manages the game centrally. There is another department called GUI whose job is to create a graphical user interface and enhance the user experience.

The controller class is our execution class and it communicates separately with the classes related to the algorithm and with the classes related to the GUI according to the MVC method in order not to confuse the purposes of the different departments and to create order in our projec (you can read more about MVC design pattern here: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) 

## UML of our project:

![image](https://user-images.githubusercontent.com/74601548/148660010-219af4dd-be48-45a7-9bd3-3248ade8bdcb.png)


## Our results:

![image](https://user-images.githubusercontent.com/74601548/148657201-a9f775b4-3834-42be-a2ff-7819a0e41b0d.png)

## How to run this game?

Please follow the next steps:
1. Clone the project from here: https://github.com/ChaimW25/Ex4
2. Open the cmd in the folder of the jar file: Ex4_Server_v0.0.jar
3. Write there: java -jar Ex4_Server_v0.0.jar 0 (instead of writing 0 you can write each level you want between 0-15)
4. run the "Controller" class in the path: src/Game/Controller.py
 
Congratulations! You succeeded to run our Pokemon game!



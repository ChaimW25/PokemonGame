
# Pokemon game

![logooo](https://user-images.githubusercontent.com/74601548/148529725-cce3981f-d331-4a88-802b-95d1e397a293.png)
## Introduction
In this project we were created and designed a Pokemon game.
The game is structured so that a directed weighted graph is given (you can read about that here: https://en.wikipedia.org/wiki/Directed_graph)
 And given a list of Pokemons (with different values ​​for each) that are located on the edges of the graph. 

The main goal of the game - locate the agents who capture the pokemons and make the agent walk so that they capture as many pokemons as possible at high values, it means, maximize the overall score of the captured pokemons.

The game has different cases that are different in their attributes like: the struct of the graph, the position of the pokemons, the number of agents and their speed.

 We have written an algorithm that maximize the grades of the agents in capturing the pokemons in the different cases and difficulty levels. In addition, we have created a GUI (Graphical user interface) for the game that illustrates the original characters in the 'Pokemon' series.

Below: An image of the Pokemon agent! ('Ash Ketchum', in the series),:

![ash](https://user-images.githubusercontent.com/74601548/148528833-c60c78e7-c361-4fe5-a2c9-608bf6ba4296.png)

An image of our game Pokemons: in yellow-'Pikachu' , in orange-'Charmander' .


![image](https://user-images.githubusercontent.com/74601548/148529412-076466cf-69ee-424a-81c3-e58b69ab3690.png)



The graph in the game is a directed graph, so, we differ in the GUI between yellow Pokemons placed on descending edges (the id of the source vertex is higher than the destination vertex) and orange pokemon placed on ascending edges.

That's how the game GUI looks like:


![image](https://user-images.githubusercontent.com/74601548/148536180-e9859187-47aa-4045-8161-1def0ff25d2f.png)

The game is running by communication with a server (link to server here: https://github.com/ChaimW25/Ex4/blob/master/Ex4_Server_v0.0.jar ). That's how it works: the server writes us a script of different cases and different levels in the game and we send our code algorithm to the server and running the game. Meanwhile, We can watch the GUI of the game and watch the info results that printed in our IDE.

## A view to our code:
For the purpose of using a weighted directed graph we have expanded the skeleton we have already created in a previous projects. Please have a short look in our 'Directed Weighted Graph' projects:
 in Python- https://github.com/ChaimW25/Ex3.git
 
And in Java- https://github.com/ChaimW25/ex2.git

## UML of our project:

![image](https://user-images.githubusercontent.com/74601548/148660010-219af4dd-be48-45a7-9bd3-3248ade8bdcb.png)


## Our results:

![image](https://user-images.githubusercontent.com/74601548/148657201-a9f775b4-3834-42be-a2ff-7819a0e41b0d.png)





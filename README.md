
# Pokemon game

![logooo](https://user-images.githubusercontent.com/74601548/148529725-cce3981f-d331-4a88-802b-95d1e397a293.png)
## Authors:
Tahel Zecharia

Haim Willinger

## Introduction
In this project, we created and designed a Pokémon game. The game is structured around a directed weighted graph (you can read about it here: https://en.wikipedia.org/wiki/Directed_graph). Additionally, there is a list of Pokémon located on the edges of the graph, each with its own unique values.

The main objective of the game is to locate the agents who capture the Pokémon and guide them to capture as many high-value Pokémon as possible. The goal is to maximize the overall score of the captured Pokémon.

The game features different cases that vary in attributes such as the structure of the graph, the positions of the Pokémon, the number of agents, and their speeds.

Below is an image of the Pokémon agent, 'Ash Ketchum', from the series:

![ash](https://user-images.githubusercontent.com/74601548/148528833-c60c78e7-c361-4fe5-a2c9-608bf6ba4296.png)

Here is an image of the Pokémon in our game: Pikachu, represented by the color yellow, and Charmander, represented by the color orange.

![image](https://user-images.githubusercontent.com/74601548/148529412-076466cf-69ee-424a-81c3-e58b69ab3690.png)



The graph in the game is a directed graph. In the game's graphical user interface (GUI), we distinguish between yellow Pokémon placed on descending edges (where the ID of the source vertex is higher than the destination vertex) and orange Pokémon placed on ascending edges.

## That's how the game GUI looks like:

A short clip (case 11) in live version:


![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/74601548/148663364-b99f80aa-a9c5-438b-8bb9-bf441539f66e.gif)

And for download:
[Screen Recording - Made with RecordCast.zip](https://github.com/ChaimW25/Ex4/files/7834136/Screen.Recording.-.Made.with.RecordCast.zip)


A screenshot of case 7:

![image](https://user-images.githubusercontent.com/74601548/148664191-3d591c50-7b5c-4a58-b700-28577c02bf4b.png)

screenshot of case 15:

![image](https://user-images.githubusercontent.com/74601548/148664169-6b13fef0-e8f1-49fc-83e1-af6fa3544e8b.png)

## A bit about what we've done in this project:

We have developed an algorithm that maximizes the scores of the agents in capturing the Pokémon across various cases and difficulty levels. Additionally, we have created a graphical user interface (GUI) for the game, featuring original characters from the 'Pokémon' series.

The game runs by communicating with a server (link to server: https://github.com/ChaimW25/Ex4/blob/master/Ex4_Server_v0.0.jar). Here's how it works: the server provides us with a script containing different cases and levels for the game. We send our algorithm code to the server, which then runs the game. We can simultaneously observe the GUI of the game and view the information and results displayed in our integrated development environment (IDE).

## A view to our code:

To utilize a directed weighted graph, we have expanded on the skeleton we previously developed in a previous project. Please take a moment to review our 'Directed Weighted Graph' projects:

In Python: https://github.com/ChaimW25/Ex3.git

And in Java: https://github.com/ChaimW25/ex2.git

To gain a comprehensive understanding of the project, we recommend referring to the UML diagram attached below. As mentioned earlier, the project is built upon the infrastructure we created in the previous project. This enables us to receive data about the graphs in the game from the server and efficiently manage them using the various functions and algorithms we have already implemented.

We have introduced additional classes to create game-related objects such as Pokemon, Agents, and GameInfo. The GameManager serves as the central component that connects all the departments related to the game. It communicates with the graph-related departments and manages the game's operations. Another department, GUI, focuses on creating a graphical user interface to enhance the user experience.

The controller class functions as our execution class. It communicates independently with the algorithm-related classes and the GUI-related classes, following the MVC (Model-View-Controller) design pattern. This separation of responsibilities ensures clarity and organization within our project. You can read more about the MVC design pattern here: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller

## UML of our project:

![image](https://user-images.githubusercontent.com/74601548/148660010-219af4dd-be48-45a7-9bd3-3248ade8bdcb.png)


## Our results:

![image](https://user-images.githubusercontent.com/74601548/148657201-a9f775b4-3834-42be-a2ff-7819a0e41b0d.png)

## How to run this game?

To run this game, please follow the steps below:

Clone the project from the following repository: https://github.com/ChaimW25/Ex4.
Open the command prompt (cmd) and navigate to the folder containing the Ex4_Server_v0.0.jar file.
Execute the following command: java -jar Ex4_Server_v0.0.jar 0 (Replace the "0" with the desired level between 0-15).
Run the "Controller" class located in the path: src/Game/Controller.py.
Congratulations! You have successfully launched our Pokémon game!
Please ensure that you have the necessary dependencies installed and configured correctly before running the game.



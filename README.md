# chat_application
A complete chat application with front and back end features done using flask and socket server

How's this gonna work? Well, the first thing that will show up is the pop up window where you type your name and after that your get randomly put in the chat room. So every user will get dragged in the same chat room to shake the party. 

The chat room will look pretty straight forward. A basic window with the input area where you can type your messages and the send button and all the messages will be displayed inside the window. Plain and simple. 

On the side I'm gonna have a chat server that will handle all the messages and communication things and I'm gonna have another server which is gonna be the web server. You connect to the web server which will display the web page itself using Flask and the web server is gonna be communicating with the chat server which will display the messages on the screen. So basically you send the message to the web server, which in turn sends it to the chat server and the chat server broadcasts it to everyone in the chat room.

The main part of the code for creating the chat server I borrowed from this guy at https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170 . Read more of his articles, he's awesome!
Huge shout out to Saurabh Chaturvedi follow him at @arichduvet https://twitter.com/arichduvet ❤️❤️❤️

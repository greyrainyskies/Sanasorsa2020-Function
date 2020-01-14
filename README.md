# Sanasorsa 2020 :duck:

Sanasorsa 2020 is a small browser-based word game created as the final project for the C#.NET / Azure course of Academy Finland in 2019. The game utilises a machine learning model (Word2Vec) trained with Finnish Wikipedia articles to give scores to the player.

## Architecture

All the components of the game were designed to run on Azure. This Azure function was written in Python and it handles querying the Word2Vec model for distances between vectors and scoring the player's guesses according to the distances between the original prompt word and the guessed words. The function is called by the backend REST API written in C# instead of being called directly by the application frontend. The REST API handles checking for repeated guesses and normalising the user inputs.

![Architecture diagram](Sanasorsa2020-diagram.png)

## Gameplay

The game is voice controlled and can be played without using the keyboard. Alternatively, the player can write their guesses into the text box. The goal of the game is to list as many words related to the word provided by the game in 10 seconds. After three rounds, the player can choose to enter their score to be included in the leaderboard or they can start again without saving their scores.

[You can play the live version of the game here.](https://sanasorsa.azurewebsites.net/ "Play Sanasorsa 2020") 

For the voice control to work, you need to open the game through an HTTPS link. As the site is for proof-of-concept demo use only, tallying the scores might take some 30 s - 1 min to be completed during the first round as the Azure function will have to perform a cold start.

[Watch the gameplay video here.](http://www.youtube.com/watch?v=vCN54GZkiyo "Sanasorsa 2020 Gameplay")

[![A full gameplay video](Sanasorsa2020-screen.png)](http://www.youtube.com/watch?v=vCN54GZkiyo "Sanasorsa 2020 Gameplay")

## Related Repositories

We worked on different parts of the software as separate projects. This repository contains the code that runs the word model in an Azure Function and comminucates with the backend API. 

The code for the frontend single-page-application as well as the backend REST-API can be found in [this repository](https://github.com/SaskaYl/Sanasorsa).

The material cleaning scripts and model training scripts are yet to be updated to be public.

## Collaborators

This project was made with :heart: by [Johanna](https://github.com/johnur), [Saska](https://github.com/SaskaYl), [Urho](https://github.com/unie31) and [Ville](https://github.com/greyrainyskies)

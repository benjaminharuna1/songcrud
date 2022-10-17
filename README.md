# songcrud

Zuri Cohort 2 Assignmnent

SID: I4G023342ZEO

## Week 4 Python Task: Pip, Virtual environments and intro to Django
## Question

Create a new Django project named “songcrud” and create an app in the project called “musicapp”. Your project must contain a requirements.txt file housing all the pinned dependencies from your project. Push the project to GitHub and submit your public GitHub repository link.

Note: Always create a virtual environment anytime you're working on a new Django project. You can get your requirements.txt file from your virtual environment


## Task Title: Week 5 Python Task: Django CRUD
We would be building a simple song CRUD application. In our models.py file inside the “musicapp” application we created, you are expected to add the following Models and Attributes.

 

Model: Artiste, Song, Lyric
Attributes for “Artiste” : first_name, last_name, age
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id
 

As you might have guessed, there is a relationship between all three Models. An Artiste can have multiple songs, and a song can have multiple lyrics.A song must only belong to one Artiste and a lyric must only belong to a song. You are to specify the foreignkey relationship yourself.

Also, the model field attributes should be specified by you. 

Push the task to GitHub when you finish and submit the GitHub repository link



## Task Title: Week 6 Python Task: Django REST Framework

## Question

Build a simple REST API to list all the songs in our database and all the artists. Your API should also be able to fetch a particular song, delete and update a particular song.Push your code to the same GitHub repository

 Note:  When you delete a particular song in the API, All lyrics of that song should be deleted. Also, updating a song simply means updating the song title or the date it was published

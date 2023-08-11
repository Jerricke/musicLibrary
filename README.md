# musicLibrary
MusicLibrary is a database for storying artists and their songs, as well as the additional feature of users who like the songs. This is a simplified immitation of what the backend of a music listening platform could look like! Where there are two many to many relationships between 2 sets of datas. The idea behind building this project is to create a simplified version of what I envision Spotify's backend would look like.

## Installation
Clone the repository and access it within your local files 
```
    $ git clone https://github.com/your-username/muiscLibrary.git

    $ cd musicLibrary
```

Install the required packages with
```
    $ pipenv instsall && pipenv shell
```

Navigate into the app directory and run these following commands
```
    $ cd lib 

    $ python3 seed.py

    $ python3 cli.py
```

## Usage
In the main menu you will have a list of options of to pick from, for example:
```
[?] Main Menu: Artists
 > Artists
   Songs
   Users
   Exit
```

By using the arrow keys you can navigate through the options and hitting enter would select the option you are currently hovering over. 

In Muisc Library, you can view the current existing list of artists as well as add more to the list. Hitting enter on an artist will further display the lists of songs that they have published as well as the option to delete said artist. Deleting an artist would also result in the deletion of all the songs associated with them.

Similar to the artist menu, the songs and users menu have built in functions as well. You can add and remove both songs and users. When creating a user, you are also able to "save" songs to their list by going through the user navigation menu.

For example:
```
                     User's name: Ashlee Davis 
                     User's age: 12 
                     User's Nationality: Guatemalan
====================================================================================================
[?] Select: Back
 > Back
   Saved Songs
   Save New Song
   Delete Saved Song
```
## Contributor 

### Jerrick Ee

Github: Jerricke
Email: eejerrickw@gmail.com


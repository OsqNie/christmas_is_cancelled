# Last Christmas

This piece of script is dedicated to keeping Last Christmas (or any associated music) from playing on common computers before December. It was first created to be run on a common room computer. Any attempt to put on Christmas music was replaced by _Kenny Loggins_ classic: "Danger Zone" from the Top Gun soundtrack. 

The script is from 2015 Ubuntu, and should run on most computers from that time.

The code can easily be modified to control any music and replace it with other - eg. make sure your store only plays pre-approved playlists or does not play offensive music.

# Installation and usage

First install the prequisite libraries:

```
https://github.com/hugosenari/mpris2
https://github.com/hugosenari/pydbusdecorator
```

Then, set the script to poll the player periodically. In it's simplest, you can set up a cronjob every 10 seconds or so to run the whole script. 

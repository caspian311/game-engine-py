# Game Engine

I really haven't thought this one through yet. Just wanted a project to throw code at this problem.

## To Play

### Install Dependencies

So this will install all 3rd party libraries as well as install the app as a library/python egg as well. So I strongly advise running this in a virtual environment.

```
$ pip install -r requirements.txt
$ pip install -e .
```

### Run the game

Then, you just run the game which I called `game`. ... That could change later.

```
$ game
```

## Development Notes

So, in general, I don't consider myself a Python developer. However, I do enjoy the language and this is helping me learn it. I'm growing as I go and this is more of a project for myself. So, unless I ask for it, I'm not accepting pull requests. But if you enjoy this type of problem, feel free to fork, plagerize, whatever - just have fun!

### Virtual Environment

This is more of a reminder for myself (future me has a terrible memory). 

To create a new virtual environment...
```
$ pip install venv
$ python -m venv <path-to-venv>
```

Generally, the <path-to-venv> could be anywhere: home directory, dot folder in home directory, ./venv in the repo.

To activate the virtual environment for that shell...
```
$ source <path-to-venv>/bin/activate
```

When you're done...
```
$ deactivate
```

### Tests/Linters/etc... 

Please make sure that all tests pass and that the coverage is reasonable.

```
$ coverage run -m pytest -v
$ coverage report --omit=tests/*
```

## Musings

The fun stuff...

### Attacking

So, I've been looking into just randomizing the damage and whatnot based on some range that seemed reasonable. But then I started doing some very light research on how like a D&D type style attack system would work. 

And (from my limited understanding) the D&D style is actually really straight forward. 
1. roll to see if you even get to hit them
   - this is a d20 + attack modifiers (if you're a knight, you get a big one. if you're not an attacker, you don't get much) against the defenders class modifiers (if they're armored or not)
   - if your attack is higher than their defense, then you hit
   - if you get a 20 on the dice roll, it's critical and damage is doubled
1. once an attack is established, you roll for your damage
   - based on weapon
   - add any modifiers
1. if the damage dealt is greater than remaining health, defender dies

For my game, I'm going to take a simplified version of this: 
1. players have an attack attribute and a defense attribute
1. if player attacks another player, the hit will always land
1. damage dealt is equal to the difference between the attack and defense points

So, it's a bit boring

### Graphics

Things for the future... maybe using curses to do some very basic GUI programming rather than just text.

### Python development

It's been a long time since I've programmed in anything, much less anything of substance in Python. I'm learning the tools (pytest, pylint, coverage, curses, etc.) as I go. I'm trying to feel out the painful parts and refactor as I go. Hopefully this doesn't become a nasty mess and I abandon it in a few weeks.

I really like having pylint. I don't know the Python standards and this is a good teacher. I turned off the warnings about code comments because I still see those as a code smell rather than a good thing. But maybe all this will change in the coming weeks.

I'm really enjoying being in Vim again. Just a good editor.

Anyways - it's all about having fun with it. And so far, it's doing that for me. :)

### Design patters

So I started out with just a simple loop over a custom iterator that generated Turns and the turn was either the player's turn or the baddies turn. That was fine enough to start with. But when I created a screen with a GUI that had to run in its own thread, I had to adjust things a bit. I went with a Command pattern (no strict adherance to true design patters so don't come at me for that). The commands can be executed to change the game's state. I also have a global Data structure that keeps track of that state. And finally, I created a background thread that moves things along. And this is where things start to get interesting. What does moving things along look like? Right now? It's just battle after battle until you die. At some point, I want to do more than just battle, but also explore. Which could give rise to other things like inventory as well as occassional fights and maybe even a boss fight at the end. And what is the end? End of the level? End of the dungeon? Should these players persist? All good questions that I toy with but take one thing at a time.

The commands also give me the ability to write unit tests around stuff. Especially given the global state of the data which gives a clear result of the command's execution. So tests are there. No end-to-end tests cause I don't want to write a screen reader for this.

...

So the commands and monitors got complicated quick and I had to redo a bunch of stuff. But I think it's better now. I still have an oddity where there's a link between the class that executes the commands and the class that contains all the commands. This is mainly because I wanted to error out if a bad command was given. But it also creates cyclic dependencies if I want commands to call other commands. So the commands change global state and the monitors watch the global state for changes and then fire off new commands. It's not terrible, but it's feels like a work-around. 

Now, there are some good things with the monitors. For one, I can have independent actions. So like the baddies attack the user regardless of whether or not the user does anything. I kinda like that. However, I am going to make it more turn based. Cause right now, you're constantly in a button mashing contest to stay alive. There's no chance to think about moves. But still, maybe this design has it's merits. We'll see.

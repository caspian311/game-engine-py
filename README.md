# Game Engine

I really haven't thought this one through yet. Just wanted a project to throw code at this problem.

## To Play

### Install Dependencies

```
$ pip install -r requirements.txt
```

### Run the game

```
$ python app.py
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

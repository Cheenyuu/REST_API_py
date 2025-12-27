# Developer Log for REST API

Command I've never used:
```
pip3 freeze > requirements.txt
```

So far, understanding how to consume an API is really straightforward. But almost immediately I am confused by everything that I'm being presented with.

Within the terminal I'm required to follow these steps:

```
python -m venv .venv
source .venv/bin/activate
```

I'm having an issue already with trying to run 'source .venv/bin/activate'

I'm getting an error: 

```
source : The term 'source' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the 
name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ source ./venv/bin/activate
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (source:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

The error is actually pretty simple though, it's just because he's using MacOS to write this, I'm on Windows powershell.
The correct code is

```
.venv\Scripts\Activate.ps1
```

If it gives you the error:

```
.venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled on this 
system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .venv\Scripts\Activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

Just run:

```
Set-ExecutionPolicy -ExecutionPolicy remoteSigned -Scope CurrentUser
```

This will allow you to run scripts that are generated using tools or tools created locally.

---

### Important Note: I will not be going over every single step of the tutorial within this devlog, only what I struggle with or what I may be confused by. For anyone who is reading this in order to learn how to write their own REST API, please watch the video that I linked in the rest-api-nodes.md within notes.

---

I installed flask and flask-sqlalchemy using pip3 while I was within my virtual env, however when trying to make a new application with 

```
from flask import flask
```

Pylance is not able to resolve.
Simple solution though, I just needed to change the interpreter from what I have normally to the interpreter within the virtual environment.

This is done easily just by opening the command palette and selecting the python interpreter.

I'm realizing now that powershell is not really great for developement just because it has completely different commands.
Like instead of 'export' it uses 

```
$env:FLASK_APP = "app.py"
```

which still makes sense but wow.

---

### Woohoo my first error!
```
(.venv) > flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: While importing 'application', an ImportError was raised:

Traceback (most recent call last):
  File "E:\Personal\REST\.venv\Lib\site-packages\flask\cli.py", line 245, in locate_app
    __import__(module_name)
    ~~~~~~~~~~^^^^^^^^^^^^^
  File "E:\Personal\REST\application.py", line 1, in <module>
    from flask import flask
ImportError: cannot import name 'flask' from 'flask' (E:\Personal\REST\.venv\Lib\site-packages\flask\__init__.py). Did you mean: 'Flask'?        

```

Really simple error honestly. I don't think I wanna always write when I get any kind of error, but this one is just special because it's my first one so I'm gonna include it.

---

### It's working!
So far, everything is going great and there is no issue.

---
When trying to create a database, I ran into a few issues:

```
(.venv) PS E:\Personal\REST> python
Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> from application import db
>>> db.create_all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    db.create_all()
    ~~~~~~~~~~~~~^^
  File "E:\Personal\REST\.venv\Lib\site-packages\flask_sqlalchemy\extension.py", line 900, in create_all
    self._call_for_binds(bind_key, "create_all")
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Personal\REST\.venv\Lib\site-packages\flask_sqlalchemy\extension.py", line 871, in _call_for_binds
    engine = self.engines[key]
             ^^^^^^^^^^^^
  File "E:\Personal\REST\.venv\Lib\site-packages\flask_sqlalchemy\extension.py", line 687, in engines
    app = current_app._get_current_object()  # type: ignore[attr-defined]
  File "E:\Personal\REST\.venv\Lib\site-packages\werkzeug\local.py", line 519, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.
```

RuntimeError: Working outside of application context. This means that Flask does not know which app is "current". 

Found solution:
```
(.venv) PS E:\Personal\REST> flask shell
Ctrl click to launch VS Code Native REPL
Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
App: application
Instance: E:\Personal\REST\instance
```

Running it in a flask shell makes things really easy, you just need to make sure you define what application you're using beforehand, but once you do that, you don't have to do a lot of importing at all.

---

```
>>> db.create_all()
>>> drink = Drink(name="Grape Soda", description="Tastes like grapes")
>>> drink
Grape Soda - Tastes like grapes
>>> db.session.add(drink)
>>> db.session.commit()
>>> Drink.query.all()
[Grape Soda - Tastes like grapes]
```

Just documenting some of the commands so I can come back and look at them without needing to scrub through the whole video. 

---

### Also to note: I will not be posting Caleb's code onto my repo. Honestly it just makes sense not to, if you want to follow his tutorial again, please watch the video it's very helpful. But to clarify, all of these things I'm running into so far is just from following his tutorial.

I'll probably need to install Postman soon...

---
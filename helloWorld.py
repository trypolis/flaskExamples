#helloWorld.py
#Flask classic "hello, world!" example.
#Copyright (C) 2020, Ty Gillespie. All rights reserved.
#This file is covered by the GNU General Public License Version 3.
#See the file LICENSE for more details.

"""To run:
$ python helloWorld.py
"""

from flask import Flask #We only use the flask.Flask class (for now).

#Create the app. We pass __name__, which will be "__main__".
app:Flask=Flask(__name__)

#Route directory (by default 127.0.0.1:5000/).
@app.route("/")
def helloWorld()->str:
	"""Simply return the text you want printed."""
	return "Hello, World!"

if __name__=="__main__":
	app.run()

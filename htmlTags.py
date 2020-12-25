#htmlTags.py
#Flask example with HTML tags for text.
#Copyright (C) 2020, Ty Gillespie. All rights reserved.
#This file is covered by the GNU General Public License Version 3.
#See the file LICENSE for more details.

"""To run:
$ python htmlTags.py
"""

from flask import Flask #We only use the flask.Flask class (for now).

#Create the app. We pass __name__, which will be "__main__".
app=Flask(__name__)

#Route directory (by default 127.0.0.1:5000/).
@app.route("/")
def test():
	"""Simply return the text you want printed (with your HTML tags inline)."""
	return "<h1>This is a test!</h1>"

if __name__=="__main__":
	app.run()

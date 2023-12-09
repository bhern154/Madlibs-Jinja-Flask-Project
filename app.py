from flask import Flask, request, render_template
from stories import Story, story
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

"""Simple Madlibs Game using Flask."""

@app.route('/')
def start_form():
    """Starter form."""
    prompt_list = story.prompts
    return render_template("form.html", prompts=prompt_list)

@app.route('/story')
def create_story():
    """Generate story from input."""
    args = {
       "place": request.args["place"],
       "noun": request.args["noun"],
       "verb": request.args["verb"],
       "adjective": request.args["adjective"],
       "plural_noun": request.args["plural_noun"],
    }

    return render_template("story.html", story_gen=story.generate(args))

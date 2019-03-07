from flask import Flask, render_template_string, config

app = Flask(__name__)

@app.route('/<name>')
def index(name):
	template = '<h1>hello {}!<h1>'.format(name)
	return render_template_string(template)

app.run()
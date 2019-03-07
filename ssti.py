from flask import Flask, render_template_string, config, request

app = Flask(__name__)

@app.route('/')
def index():
	name=request.args.get('name')
	template = '<h1>hello {}!<h1>'.format(name)
	print(template)
	return render_template_string(template)

app.run()
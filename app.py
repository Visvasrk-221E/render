from flask import Flask, render_template, url_for, redirect, Response
from datetime import datetime
import time
import os

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

@app.route('/')
def redirect_to_home():
	return redirect(url_for('home'))

@app.route('/home')
def home():
	subjects = {"biology" : "Topics based on general biology as well as grade 12 biology can be learnt from here.[Grade 12]",
		"cybersecurity" : "Topics based on cybersecurity, from school to college level or even masters can be learnt from here.[Basics]",
	}
	subject_count = len(subjects)
	crt_time = datetime.now()
	return render_template('index.html', time=crt_time, subjects=subjects, subject_count=subject_count)

@app.route('/subjects/<subject>')
def route_subject(subject):
	return redirect(url_for('subject'))

@app.route('/subjects/biology')
def biology():
	topics = {
	"organisms_and_populations" : "This topic is about how different organisms interact with each other in a population, the factors affecting it and study of ecology.[Ecology]",

	}
	topic_count = len(topics)
	return render_template('biology/index.html', topics=topics, topic_count=topic_count)

@app.route('/subjects/cybersecurity')
def cybersecurity():
	topics = {"cybersec0" : "This is the first step in learning cybersecurity. You are on right path to take the fundamentals, just step right in.[Basics]",}
	topic_count = len(topics)
	return render_template('cybersecurity/index.html', topics=topics, topic_count=topic_count)

@app.route('/subjects/biology/<topic>')
def biology_topic(topic):
	return redirect(url_for('topic'))

@app.route('/subjects/cybersecurity/<topic>')
def cybersecurity_topic(topic):
	return redirect(url_for('topic'))

@app.route('/subjects/biology/organisms_and_populations')
def organisms_and_populations():
	return render_template('biology/organisms_and_populations.html')

@app.route('/subjects/cybersecurity/cybersec0')
def cybersec0():
	return render_template('cybersecurity/cybersec0.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=port)



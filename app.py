from flask import Flask, render_template, url_for, redirect, Response, send_from_directory
from datetime import datetime
import time
import os

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
docsdir = os.path.join(app.static_folder, "documents")


@app.route('/dochub/<path:filename>')
def download_file(filename):
	return send_from_directory('static/documents', filename, as_attachment=True)

@app.route('/')
def redirect_to_home():
	return redirect(url_for('home'))

@app.route('/home')
def home():
	docnum = len([f for f in os.listdir(docsdir)])
	subjects = {"biology" : "Topics based on general biology as well as grade 12 biology can be learnt from here.[Grade 12]",
		"cybersecurity" : "Topics based on cybersecurity, from school to college level or even masters can be learnt from here.[Basics]",
	}
	subject_count = len(subjects)
	crt_time = datetime.now()
	return render_template('index.html', time=crt_time, subjects=subjects, subject_count=subject_count, docnum=docnum)

@app.route('/dochub')
def dochub():
	return render_template('documents/index.html')

@app.route('/subjects/<subject>')
def route_subject(subject):
	return redirect(url_for('subject'))

@app.route('/subjects/biology')
def biology():
	docnum = len([f for f in os.listdir(docsdir) if "[bio]" in f])
	topics = {
	"organisms_and_populations" : "This topic is about how different organisms interact with each other in a population, the factors affecting it and study of ecology.[Ecology]",
	}
	topic_count = len(topics)
	return render_template('biology/index.html', topics=topics, topic_count=topic_count, docnum=docnum)

@app.route('/subjects/cybersecurity')
def cybersecurity():
	topics = {
	"cybersec0" : "This is the first step in learning cybersecurity. You are on right path to take the fundamentals, just step right in.[Basics]",
	"basic_tools" : "Know the basic tools of cybersecurity. Learn how to use Nmap, Burpsuite, Telnet, connect with CLI, etc.[Basics, Tools]",
	}
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

@app.route('/subjects/cybersecurity/basic_tools')
def basic_tools():
	tool_dict = {
		"nmap" : "Network Mapper, shortly known as Nmap, is a command line tool for checking and surfing open ports...[Tools]",
	}
	return render_template('cybersecurity/basic_tools.html', tool_dict=tool_dict)

@app.route('/subjects/cybersecurity/basic_tools/<tool_name>')
def render_basic_tools(tool_name):
	return redirect(url_for('tool_name'))


@app.route('/subjects/cybersecurity/basic_tools/nmap')
def nmap():
	return render_template('cybersecurity/basic_tools/nmap.html')

@app.route('/dochub/biodoc')
def biodoc():
	unacademydocs = [f for f in os.listdir(docsdir) if "[bio]" and "[unacademy]" in f]
	qbdocs = [f for f in os.listdir(docsdir) if "[bio]" and "[qb]" in f]
	gendocs = [f for f in os.listdir(docsdir) if "[bio]" and "[gen]" in f]
	doccount = len(unacademydocs) + len(qbdocs) + len(gendocs)
	return render_template('documents/biodoc.html',unacademydocs=unacademydocs, qbdocs=qbdocs, gendocs=gendocs)

@app.route('/dochub/compdoc')
def compdoc():
	netdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[net]" in f] #Networking
	hackdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[hack]" in f] #Hacking
	pydocs = [f for f in os.listdir(docsdir) if "[comp]" and "[pydoc]" in f] #Python documents and documentations
	gendocs = [f for f in os.listdir(docsdir) if "[comp]" and "[gen]" in f] # general documents
	cdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[cdoc]" in f] #C and C++ language documents
	jsdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[jsdoc]" in f] #Javascript documents
	javadocs = [f for f in os.listdir(docsdir) if "[comp]" and "[javadoc]" in f] # javadocuments
	fsdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[fsdoc]" in f] #file systems and os documents
	doccount = len([f for f in os.listdir(docsdir) if "[comp]" in f])
	return render_template('documents/compdoc.html', netdocs=netdocs, hackdocs=hackdocs, pydocs=pydocs, gendocs=gendocs, cdocs=cdocs, jsdocs=jsdocs, javadocs=javadocs, fsdocs=fsdocs)

@app.route('/dochub/weapdoc')
def weapdoc():
	docs = [f for f in os.listdir(docsdir) if "[weap]" in f]
	return render_template('documents/weapdoc.html', docs=docs)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=port)



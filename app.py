import psycopg2
import os
from flask import Flask, request, render_template, redirect, url_for, Response, jsonify
import hashlib

conn=psycopg2.connect(
  database="wt2",
  user="postgres",
  host="/var/run/postgresql",
  password="password"
)

cur = conn.cursor()

music_dir = '/home/chittaranjan/Documents/3rd Year/6_WT/Project/static/music'

app = Flask(__name__)


@app.route('/')
@app.route('/home/<userName>')
def index(userName = None):
	if not userName:		# not logged in
		#music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
		#music_files_number = len(music_files)
		songsDict = dict()
		f = open("./static/MusicData.csv")
		for line in f:
			vals = line.strip().split(",")
			songsDict[vals[0]] = vals[1:]
		print songsDict
		f.close()	
		return render_template("index.html",music_files_number = len(songsDict),music_files = songsDict.keys(), songsDict = songsDict)
	else:	
		'''				# logged in
		music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
		music_files_number = len(music_files)
		return render_template("index.html",
						title = 'Home',
						music_files_number = music_files_number,
						music_files = music_files,
						userName = userName)
	
		songsDict = dict()
		f = open("./static/MusicData.csv") #add MusicData.csv in static
		for line in f:
			vals = line.strip().split(",")
			songsDict[vals[2]] = vals[3:6]
	
		f.close()	
		# recommended songs
		'''
		q = "select * from users where name='"+userName+"';"
		cur.execute(q)
		row = cur.fetchone()	#assuming usernames have to be unique, so only one result
		age, location = row[2], row[3]	#indices according to user table
		
		#age,location = 25,"India"
		
		f=open("./static/MusicData.csv") #add MusicData.csv in static
		reco = dict() #similar to songsDict
		for line in f:			
			vals = line.strip().split(",")
			if int(age)>=int(vals[4]) and int(age)<=int(vals[5]) and location==vals[6]:	#indices according to MusicData.csv
				reco[vals[0]] = vals[1:]
				
		return render_template("index.html",
						title = 'Home',
						music_files_number = len(reco),
						music_files = reco.keys(),
						userName = userName, songsDict = reco) #passing recommended songs also


	
@app.route('/sign/')
def form():
	return render_template("signup.html")

@app.route('/checkValidity/<string:userName>')
def checkValidity(userName):
	q = "select * from users where name='"+userName+"';"
	cur.execute(q)
	rows = cur.fetchall()
	if not rows:
		resp = Response("YES", mimetype='text/xml')
		resp.headers['Cache-control'] = 'no-cache'
		return resp
	else:
		return Response("NO",mimetype='text/xml')


@app.route('/submissionthrottling')
def search():
	term = request.args.get("term")
	f=open("./static/MusicData.csv")
	response = dict()
	response.update({'data':[]})
	for line in f:
		if term in line:
			response['data'].append(line.strip().split(",")[0])
	f.close()
	if len(response['data']) > 5:
		response['data'] = response['data'][:6]
	response = jsonify(response['data'])
	response.headers.add('Access-Control-Allow-Origin','*')
	
	return response
	
@app.route('/result')
def searchresult1():
	val = request.args.get("search") 

	allSongMatches = []
	f=open("./static/MusicData.csv")
	details = dict()
	for line in f:
		vals = line.strip().split(",")
		if val.strip() == vals[0]:		#exact song match
			lyrics = open("./static/lyrics/"+vals[-1].strip()+".txt").readlines()
			details["albumname"]=vals[1]
			details["genre"] = vals[2]
			details["artist"] = vals[3]
			details["count"] = vals[-3]
			details["musicname"] = vals[-1]
			details["language"]=vals[-2]
			return render_template("songdata.html", lyrics = lyrics, songname = vals[0], details = details)
		elif val in vals[1] or val in vals[2] or val in vals[3] or val in vals[-2]:
			allSongMatches.append(vals)			
	f.close()
	
	return render_template("multiplesearchresults.html", music_files_number = len(allSongMatches), allSongMatches = allSongMatches)


@app.route('/login/',methods=['POST'])	
def login():
	name = request.form['username']
	pwd = request.form['password']
	q = "select password from users where name='"+name+"';"
	cur.execute(q)
	rows = cur.fetchall()
	#print(rows) [('e2fc714c4727ee9395f324cd2e7f331f',)]
	if(rows[0]):
		if(rows[0][0] == hashlib.md5(pwd).hexdigest()):
			return redirect(url_for('index',userName=name))
			#return index()#return render_template("index.html",title="Home",music_files_number=3,music_files=music_files)
		else:
			return "<b>Error</b>";	
	else:
		return "<b> HACKER! </b>"		
@app.route('/register/',methods=['POST'])	
def register():
    name = request.form['username']
    pwd = request.form['password']
    age = request.form['age']
    location = request.form['location']
    q = "insert into users(name,password,age,location) values('"+name+"','"+hashlib.md5(pwd).hexdigest()+"','"+str(age)+"','"+location+"');"
    cur.execute(q)
    conn.commit()
    return redirect(url_for('form'))










@app.route('/increment')
def incr():
	name = request.args.get("name")
	num = 0
	newfile = ""
	f = open("./static/MusicData.csv",'r')
	for line in f:
		line = line.strip().split(",")
		if line[-1] == name:
			print "EQUALITY OF", line[-1], name
			line[-3] = str(int(line[-3]) + 1)
			num = int(line[-3])
		line = ",".join(line)
			
		newfile += line + "\n"	
	f.close()
	g = open("./static/MusicData.csv",'w')
	g.write(newfile)
	g.close()
	return str(num)
	
@app.route('/getCount')
def getCount():	
	num = 0
	name = request.args.get("name")
	f = open("./static/MusicData.csv",'r+')
	for line in f:
		line = line.strip().split(",")
		if line[-1] == name:
			num = line[-3]
			break
	f.close()
	return name+":"+str(num)
	
	
	
	
	
	
	
	
	
	
	
@app.route('/<filename>')
def song(filename):
    return """<audio class="audio-player" controls autoplay>
                <source src='static/music/"""+filename+"""' type='audio/mp3'>
                Your browser does not support this audio format.
        </audio>
"""
                        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

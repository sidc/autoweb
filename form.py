from bottle import route, run, request, Bottle, template
from bottle import static_file
from bottle import post
import bottle_mysql


app = Bottle()

# Connecting with database
plugin = bottle_mysql.Plugin(dbuser='assignment', dbpass='assignment', dbname='assignment')
app.install(plugin)


## Serving static files
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

## Utiltiy for checking points on the assignments 
@app.route('/points')
def getScore():
    return static_file('points.html',root='./templates')

@app.post('/points')
def getScore(db):
    uniqname = str(request.forms.get('uniqname'))
    umid = str(request.forms.get('umid'))
    
    query =  ('SELECT uniqname, assign1Points as "Assignment #1" , assign2Points as "Assignment #2", assign3Points as "Assignment #3", assign4Points as "Assignment #4", assign6Points as "Assignment #6" from assign where uniqname="%s" and umid="%s"' % (uniqname,umid))    
    db.execute(query)
    row = db.fetchone()

    print row
    if row:
        output = template('templates/points', row=row)
        return output
    else:
        return "Sorry but we couldn't find a matching uniqname and UM id. Please ensure that you didn't include extra spaces and  used small letters"


@app.route('/')
def index():
    return static_file("index.html", root="./templates")

## Get Code Academy achievement points
@app.route('/codeacademy')
def codeacademy():
    return static_file("codeacademy.html", root="./templates")

@app.post('/codeacademy')
def submit_codeacademy(db):
    uniqname = str(request.forms.get('uniqname'))
    umid = str(request.forms.get('umid'))
    caUser = str(request.forms.get('caUser'))
    
    query =  ('SELECT id from assign where uniqname="%s" and umid="%s"' % (uniqname,umid))    
    db.execute(query)
    row = db.fetchone()

    if not row:
        return "Sorry. We couldn't find a matching uniqname and UM id. Please ensure that you didn't include extra spaces and  used small letters"

    import codeacademy
    (log,points) = codeacademy.grade(caUser)

    query = ('UPDATE assign set assign1Points=%d, assign2Points=%d, assign3Points=%d, assign6Points=%d  where id=%d' % (points['assign1Points'],points['assign2Points'],points['assign3Points'],points['assign6Points'],row['id']))
    print query
    db.execute(query)

    return ('</br> '.join(['Test %i: %s' % (n+1, log[n]) for n in xrange(len(log))]))


## Route to Assignment 4
@app.route('/assignment4')
def assignment4():
    return static_file("assignment4.html", root="./templates")

@app.post('/assignment4')
def submit_assignment4(db):
    uniqname = str(request.forms.get('uniqname'))
    umid = str(request.forms.get('umid'))
    caUser = str(request.forms.get('caUser'))
    siteURL= str(request.forms.get('siteURL'))

    query =  ('SELECT id from assign where uniqname="%s" and umid="%s"' % (uniqname,umid))    
    db.execute(query)
    row = db.fetchone()

    print row
    if not row:
        return "Sorry. We couldn't find a matching uniqname and UM id. Please ensure that you didn't include extra spaces and  used small letters"

    import assignment4
    (log,points) = assignment4.grade(siteURL)

    query = ('UPDATE assign set  assign4URL="%s", assign4Points=%d where id=%d' % (siteURL,points,row['id']))
    print query
    db.execute(query)

    return ('</br> '.join(['Test %i: %s' % (n+1, log[n]) for n in xrange(len(log))]))


# Starting the server
#run(app, host='localhost', port=8080, debug=True, reloader=True)
app.run(server='paste',port=80)

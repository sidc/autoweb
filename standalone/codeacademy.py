import urllib2

def checkCSV(studentCSVFile):
    import csv
    print 'uniqname','ca name'
    with open(studentCSVFile,'rb') as studentCSV:
        reader = csv.reader(studentCSV,delimiter=',')
        for row in reader:
            print row[0],' - ',row[2]

########## Utility for printing points for a particular assignment ##############
def gradeCSV(studentCSVFile):
    import csv
    with open(studentCSVFile,'rb') as studentCSV:
        reader = csv.reader(studentCSV,delimiter=',')
        for row in reader:
            try:
                studentGrade = grade(row[2])
                print row[0],',',studentGrade[1]['assign1Points']
            except:
                print row[0],',',0


######### Utility for evaluating CA achievements of a student ############
def grade(caUser):
    response = urllib2.urlopen('http://www.codecademy.com/users/%s/achievements' % (caUser))
    html = response.read()
    #print html

    log = list()
    points = dict()
    points['assign1Points'] = 0
    points['assign2Points'] = 0
    points['assign3Points'] = 0
    points['assign6Points'] = 0

    ########### Define the rules for grading here #################
    ########### I have done the assign one here #############3
    if (("HTML Basics" in html) and 
        ("Build Your Own Webpage" in html) and 
        ("HTML Basics II" in html) and 
        ("HTML Basics III" in html) and
        ("Social Networking Profile" in html)): 
        points['assign1Points'] = 50
        log.append("You have completed first five HTML tutorials | Assignment 1 Points: 50")
    else:
        log.append("You have not yet completed first five HTML tutorials| Assignment 1 Points: 0")

    if "CSS: An Overview" in html and "CSS Selectors" in html: 
        points['assign2Points'] = 50
        log.append("You have completed CSS: An Overview and CSS Selectors | Assignment 2 Points: 50")
    else:
        log.append("You have not completed CSS: An Overview and CSS Selectors | Assignment 2 Points: 0")

    if "CSS Positioning" in html:
        points['assign3Points'] = 50
        log.append("You have completed CSS Positioning | Assignment 3 Points: 50")
    else:
        log.append("You have not completed CSS Positioning | Assignment 3 Points: 0")        

    return (log,points)

def main():
    ############ CSV file for input #############
    ########## uniqname, name, codeacademy username, x, y, z ....
    #### We are interested in 0th and 2nd column only
    studentCSVFile = 'si539.csv'
    #### Function to print uniqname and CA usernames
    #checkCSV(studentCSVFile)

    #### Funtion for grading ###########
    gradeCSV(studentCSVFile)

if __name__ == '__main__':
    main()

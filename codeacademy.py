import urllib2


def grade(caUser):
    response = urllib2.urlopen('http://www.codecademy.com/users/%s/achievements' % (caUser))
    html = response.read()
    print html

    log = list()
    points = dict()
    points['assign1Points'] = 0
    points['assign2Points'] = 0
    points['assign3Points'] = 0
    points['assign6Points'] = 0

    if "Basics III" in html: 
        points['assign1Points'] = 50
        log.append("You have completed HTML Basic, HTML Basic II & HTML Basic III | Assignment 1 Points: 50")
    else:
        log.append("You have not completed HTML Basic, HTML Basic II & HTML Basic III | Assignment 1 Points: 0")

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




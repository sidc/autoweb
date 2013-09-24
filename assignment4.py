from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#from xvfbwrapper import xvfb
#from pyvirtualdisplay import Display

# visitedPage = list()
# stack = list()
# log = list()
# score = 0
# numPages = 0

def grade(pageURL):
    global score, numPages, log, stack, visitedPage

    visitedPage = list()
    stack = list()
    log = list()
    score = 0
    numPages = 0

    #display = Xvfb()
    
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    # Create a new instance of the Firefox driver
    #driver = webdriver.Firefox()
    driver = webdriver.PhantomJS(service_log_path='/var/log/phantomjs/ghostdriver.log')

    stack.append(pageURL)
    numPages = 1

    
    while stack and len(visitedPage) < 5:
        checkPageForAssign (driver)
        print score
    
    driver.quit()
    #display.stop()
    print log
 
    return (log,score)


def checkPageForAssign(driver):
    global score, log, numPages


    pageURL = stack.pop()

    if(pageURL is None):
        return
    # go to the page
    visitedPage.append(pageURL)
    try: 
        driver.get(pageURL)
        score += 1 # URL worked free Points
        log.append("---Page: "+pageURL+" works "+ " | Cumulative Points: "+str(score))
    except:
        log.append("Loading "+pageURL+"failed. Please retry submitting a valid URL")
        return 

    # Points +1 If page has title
    title = driver.title
    if title is None:
        log.append("The page has no title" + " | Cumulative Points: "+str(score))
    else:
        score += 1
        log.append("Page has the title :"+title + " | Cumulative Points: "+str(score))
        


    # Points 
    #     +1 If page has header  or 
    #     +2 If page has nav and header or
    #     +3 If nav inside header
    header = hasTag(driver,"header")
    if header is not None:
        navbar = hasTag(header,"nav",2)

    if 'navbar' not in locals() or navbar is None:
        navbar = hasTag(driver,"nav")


    # Points
    #   +1 if no list inside nav
    if navbar is not None:
        print "Nav tag ", 
        listTag = hasTag(navbar,"li",-1)
        links = navbar.find_elements_by_tag_name("a")
        for link in links:
            href = link.get_attribute("href")
            processHref = processURL(href)
            print processHref
            if(processHref not in visitedPage and processHref not in stack):
                stack.append(processHref)
                numPages = numPages + 1

    # Points +1 if no table
    table = hasTag(driver,"table",-1) 

    # Points +1 if has footer
    footer = hasTag(driver,"footer") 

    # Points +1 if page has atleast one image
    image = hasTag(driver,"img")

    # Points +1 if page has atleast one link
    link = hasTag(driver,"a")

    log.append("---Finished testing "+pageURL + "| Cumulative Points : "+str(score))


def hasTag(driver,tag,value=1):

    global score, log

    try:
        hasTag = driver.find_element_by_tag_name(tag)
        print "has tag", tag
        if value > 0 and value < 50:
            score += value
        log.append("has tag "+tag+" | Cumulative Points: "+str(score))
        print score
        return hasTag
    except NoSuchElementException:
        if value < 0 and value < 50:
            score -= value
        print "doesn't have tag ", tag
        log.append("doesn't have tag "+tag+" | Cumulative Points: "+str(score))
        print score 
        return None

def processURL(url):
    from urlparse import urlparse
    o = urlparse(url)
    return(o.scheme + "://" + o.netloc + o.path)

if __name__ == '__main__':
    grade("file:///home/sidharth/workspace/assignment/ca-cssEx1b.html")

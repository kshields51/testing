'''
Use this to find Python-based Selenium tools. It's all on one page so you can just CTRL + F what you want.
'''


# Using Browser tools for inspecting elements and the page DOM

# Finding an element using the findElement method
'''
driver.find_element_by_id(<elementID>)
    returns: an instance of a WebElement
    If not found: thors an NoSuchElementFound exception

Other variants (some explained in below sections): 

    driver.find_element_by_name(<element name>)
    
    driver.find_element_by_class_name(<element class>)

    driver.find_element_by_tag_name(<htmltagname>)

    driver.find_element_by_link_text(<linktext>)

    driver.find_element_by_partial_link_text(<htmltagname>)

    driver.find_elements_by_css_selector(<cssselector>) # not sure why they have s there

    driver.find_elements_by_xpath(<xpathqueryepxression>) # not sure why they have s there
    
'''

#Chaining
'''
You can chain together WebElements to find child elements. Not sure if the following example is good but at least
it shows the syntax.

Ex: 

div = driver.find_element_by_tagname('div')
button = div.find_element_by_tagname('button')

'''

# Finding elements using the findElements method
'''
find_elements_by_tag_name(<tagname>)
returns multiple elements as a list of WebElements # https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id


'''
# Finding links
'''
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti') # https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text

These return an element that contains the whole word Continue or just part of the word. If nothing
is found then it raises a NoSuchElementException.
'''

# Finding elements by tag name
'''
driver.find_element_by_tag_name(<htmltagname>)

'''

# Finding element using CSS selectors

# Finiding elements using XPath

'''
Special Characters
    / either defines an absolute path if used at the beginning of a statement or defines the relationship between two things if
    used in the middle
        /html will select the root html
        html/body/table / designates that table is a descendent of body

    // non absolute path
        //table will select all table elements no matter where they are in the document
        //tr//td selects all td elements

    . represents the current node

    .. represents parent of the current node
        //table/.. will return the parent of table

    @ represents an attribute
        //@id selects all elements with an id attribute no matter where it is in the document


Base Method

    driver.find_element_by_xpath(<xpathqueryepxression>)
'''

# Finding elements using tag text contents
'''
# Finding elements using tag text contents
Predicates
    A predicate is embedded in square brackets and is used to find specific nodes or a node that 
    contains a specific value

    here is an example showing how we can select elements by matching part of thier attributes
    something I always struggled to do in Pyquery

    driver.find_element_by_xpath(input[starts-with(@id, 'ctrl')]) matches ctrl-22 and ctrl-12

    There is also ends-with() and contains()

    Here is the most generic way to match a specific word with all attributes regardless of what they are
    driver.find_element_by_xpath("//input[@*=''username]")

'''

# Finding elements using CSS selectors

'''
This is the part that is truely like PyQuery here are a bunch of examples:

Base
    driver.find_element_by_css_selector(<cssselector>)
Examples

    Absolute Path
        driver.find_element_by_css_selector('html body div div form input')

    Relative Path
        driver.find_element_by_css_selector('input')

    Class selector
        driver.find_element_by_css_selector('input.login')
        
        Variant multiple selectors
            driver.find_element_by_css_selector('input.login.clickable') hits something that has two selectors attached to it
    
    Id selector
        driver.find_element_by_css_selector('input#login')
    
    attributes
        driver.find_element_by_css_selector('input[name=username])
    
        Deep example images
            driver.find_element_by_css_selector('img[alt='Previous']')

        see book for matching multiple attributes

        matching elements as long as they have certain attributes
            driver.find_elements_by_css_selector('img[alt]')
        
        excluding results
            driver.find_elements_by_css_selector('img:not([alt])')
        
        selecting multiple
         different elements , acts as or
            driver.find_element_by_css_selector('div, p')
    



'''

# Using JQuery selectors

# had some trouble running requirements.txt this helped 
# https://stackoverflow.com/questions/61419086/fatal-error-in-launcher-unable-to-create-process-using-file-path1-file-path2
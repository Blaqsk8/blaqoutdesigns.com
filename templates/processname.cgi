!/usr/etc/python3

import cgi

def htmlTop():
    print("""Content-type: text/html\n\n
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="utf-8" />
                    <title>My server-side template</title>
                </head>
                <body>""")
                
def htmlTail():
    print("""</body>
        </html>""")
        
def getData():
    #formData now contains every piece of data submitted by the form.
    formData = cgi.FieldStorage()
    # getvalue() will get value corresponding to the nme input
    firstName = formData.getvalue('firstname')
    return firstName
        
#main program
if __name__ == "__main__":
    try:
        htmlTop()
        firstName = getData()
        print('Hello %s, how are you?' % firstName)
        htmlTail()
    except:
        cgi.print_exception()

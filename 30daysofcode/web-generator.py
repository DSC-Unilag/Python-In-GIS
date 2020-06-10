name, desc = input('Enter your name:>>>  '), input('Briefly describe yourself: >>>  ')

html = f'<html>\n\
    <head>\n\
    </head>\n\
    <body>\n\
        <center>\n\
            <h1>{name}</h1>\n\
        </center>\n\
        <hr/>\n\
            {desc}\n\
        <hr/>\n\
    </body>\n\
</html>'

with open(name+'.html', 'w') as f:
    f.write(html)

'''
Functional implementation
def web(name, desc):
    html = f'<html>\n\
    <head>\n\
    </head>\n\
    <body>\n\
        <center>\n\
            <h1>{name}</h1>\n\
        </center>\n\
        <hr/>\n\
            {desc}\n\
        <hr/>\n\
    </body>\n\
    </html>'

    with open(name+'.html', 'w') as f:
        f.write(html) 
'''
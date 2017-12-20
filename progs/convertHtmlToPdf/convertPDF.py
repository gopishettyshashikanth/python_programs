import pdfkit
#pdfkit.from_url('http://google.com', 'out.pdf')


#pdfkit.from_url('1.html', 'out.pdf')


options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}
pdfkit.from_url('1.html', 'micro.pdf', options=options)




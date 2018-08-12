from app import app
from flask import render_template, request, redirect

alphabet = {
	'I':1,
	'V':5,
	'X':10,
	'L':50,
	'C':100,
	'D':500,
	'M':1000
}
def isRomanNumber(s):

	for t in s:
		if t in alphabet:
			pass
		else:
			return False
	return True

def arabic_to_roman(s):
	pass


def roman_to_arabic(input_text, ):
    input_text = input_text.upper()
    res = 0
    for d in range(len(input_text)):
        try:
            if alphabet[input_text[d]] >= alphabet[input_text[d+1]] :
                res += alphabet[input_text[d]]
            else:
                res -= alphabet[input_text[d]]
        except IndexError:
            res += alphabet[input_text[d]]
    return res 


@app.route('/', methods= ['POST', 'GET'])
def index():
    if request.method == 'POST' and len(request.form['inText'])>0:
        try:
            inStr = int(request.form['inText'])
            return render_template('index.html', result = 123456789 )
        except:
            if isRomanNumber(request.form['inText'].upper()):
                return render_template('index.html', result = roman_to_arabic(request.form['inText']) )
            else:
                return render_template('index.html', result = 'NaN' )
        return render_template('index.html', result = request.form['inText'])
    else:
        return render_template('index.html')

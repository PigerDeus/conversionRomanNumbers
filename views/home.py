from app import app
from flask import render_template, request, redirect

alphabet = {
	'I':1,
    'IV':4,
	'V':5,
    'IX':9,
	'X':10,
    'XL':40,
	'L':50,
    'XC':90,
	'C':100,
    'CD':400,
	'D':500,
    'CM':900,
	'M':1000
}
def isRomanNumber(s):

	for t in s:
		if t in alphabet:
			pass
		else:
			return False
	return True

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

# Sort dictyonary 'alphabet' by values
# Create string from remainder of division
# and create string roman number by module
def arabic_to_roman(input_number):
    num = int(input_number)
    alf_r = sorted(alphabet.values(), reverse = True)
    res = ''
    for k in alf_r:
        if num //k !=0:
            res += get_key(alphabet, k)* (num // k)
        num %= k
            
    return res


def roman_to_arabic(input_text):
    input_text = input_text.upper()
    res = 0
    i = 0
    while i < len(input_text):
        s1 = alphabet[input_text[i]]
        if (i+1 < len(input_text)):
            s2 = alphabet[input_text[i+1]]
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res




@app.route('/', methods= ['POST', 'GET'])
def index():
    if request.method == 'POST' and len(request.form['inText'])>0:
        if request.form['inText'].isdigit():
            inStr = int(request.form['inText'])
            return render_template('index.html', result = arabic_to_roman(request.form['inText']) )
    
        elif isRomanNumber(request.form['inText'].upper()):
            return render_template('index.html', result = roman_to_arabic(request.form['inText']) )
        else:
            return render_template('index.html', result = 'NaN' )
    else:
        return render_template('index.html')

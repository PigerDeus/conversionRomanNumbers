from app import app, db
from flask import render_template, request
from datetime import datetime
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


def is_roman_number(s):
    count_dict = {
        'symbol':'M',
        'count': 0
    }
    i = 0

    # Checking the duplication of smaller ones before large
    while i < len(s):
        s1 = alphabet[s[i]]
        if i+1 < len(s):
            s2 = alphabet[s[i+1]]
            if s1 <= s2:
                if i + 2 < len(s):
                    if s1 < alphabet[s[i+2]]:
                        return False
                    elif s1 < s2 and s1 >= alphabet[s[i+2]]:
                        return False
                    # elif s2 <= alphabet[s[i+2]]:
                    #     return False    
                    # pass                      
        i += 1

    #check for repetition and match the alphabet
    for t in s:
        if t in alphabet:
            if t == count_dict['symbol']:
                count_dict['count'] += 1
                if count_dict['count'] > 3:
                   return False
            else:
                count_dict['symbol'] = t
                count_dict['count'] = 1
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
    num = int(input_number.strip())
    alf_r = sorted(alphabet.values(), reverse = True)
    res = ''
    for k in alf_r:
        if num //k !=0:
            res += get_key(alphabet, k)* (num // k)
        num %= k
            
    return res


def roman_to_arabic(input_text):
    input_text = input_text.strip().upper()
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
    dict_res = {
                    'res': '',
                    'history': db.numb_db.find().sort('datetime', -1).limit(10),
                    'in': '',
                }
    if request.method == 'POST' and len(request.form["inText"])>0:
        input_text = request.form["inText"]
        dict_res['in'] = input_text
        # input number is arabic
        if input_text.isdigit():
            if int(input_text) > 3999 or int(input_text)< 0:
                dict_res['res'] = 'Введенное число не находиться в диапазоне от 0 до 3999'
                return render_template('index.html', result =  dict_res )
            req = db.numb_db.find_one({'arabic_value':  input_text.strip()})
            # value is in the database -> return value from db
            if req:
                dict_res['res'] = req['roman_value']
                return render_template('index.html', result = dict_res )
            # value isn't in the database -> search value, 
            # add value in db
            else:
                res = arabic_to_roman(input_text)
                item_db = {
                'roman_value': res,
                'arabic_value': input_text.strip(),
                'datetime': datetime.now()
                }
                db.numb_db.insert_one(item_db)
                dict_res['res'] = res
            return render_template('index.html', result = dict_res )
        # input number is roman
        elif is_roman_number(input_text.upper()):
            req = db.numb_db.find_one({'roman_value':  input_text.strip().upper()})
            if req:
                dict_res['res'] = req['arabic_value']
                return render_template('index.html', result = dict_res )
            else:
                res = roman_to_arabic(input_text)
                if res < 0 or res > 3999:
                   return render_template('index.html', result = 'Введенное число не находиться в диапазоне от 0 до 3999' )
                item_db = {
                'roman_value': input_text.strip(),
                'arabic_value': res,
                'datetime': datetime.now()
                }
                db.numb_db.insert_one(item_db)
                dict_res['res'] = res
                return render_template('index.html', result = dict_res )
        # the value entered is not an Arabic or Roman number
        else:
            dict_res['res'] = 'Введенная строка не являеться допустимым числом'
            return render_template('index.html', result = dict_res )
    else:
        dict_res['res'] = ''
        return render_template('index.html', result = dict_res )

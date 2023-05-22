from django import template

 
register = template.Library() 

@register.filter(name='multiply')
def multiply(value, arg):
    return str(value) * arg

@register.filter(name='filter_message')
def filter_message(message: str):
    variants = ['отстой', 'говно', 'тварь', 'дурак', 'чмо']
    ln = len(variants)
    filtred_message = ''
    string = ''
    string2 = ''
    pattern = ' * '
    for i in message:
        string += i
        string2 = string.lower()
        
        flag = 0
        for j in variants:
            if not string2 in j:
                flag += 1
            if string2 == j:
                filtred_message += pattern
                flag -= 1
                string = ''
                
        if flag == ln:
            filtred_message += string
            string = ''
            
    if string2 != '' and string2 not in variants:
        filtred_message += string
    elif string2 != '':
        filtred_message += pattern
        
    return filtred_message
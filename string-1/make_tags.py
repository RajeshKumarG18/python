# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
    result = ''
    opening_tag = ''
    closing_tag = ''
    opening_tag += '<'
    
    for i in tag:               
        opening_tag += i
    opening_tag += '>'
    closing_tag += '</'
    
    for j in tag:
        closing_tag += j
    closing_tag += '>'
    result += opening_tag
    result += word
    result += closing_tag
    return result
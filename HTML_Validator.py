#!/bin/python3
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    s = Stack()
    tags = _extract_tags(html)
    balanced = True
    index = 0
    while index < len(tags) and balanced:
        symbol = tags[index] 
        if symbol[1] != '/':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if symbol[2:len(symbol)] != top[1:len(top)]:
                        balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    if html.find('>') == -1:
        return tags
    for i in range(len(html) - 1):
        temp_word = ""
        if html[i] == '<':
            counter = i
            while html[counter] != ">" and counter <  len(html) - 1:
                temp_word += html[counter]
                counter += 1
            tags.append(temp_word + '>')
    return tags



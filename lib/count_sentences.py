#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("MyString must be initialized with a string value.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
     if not isinstance(new_value, str):
        raise ValueError("MyString must have a string value.")
     self._value = new_value


    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split the value using period, question mark, and exclamation mark as delimiters
        sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self._value) if sentence]
        return len(sentences)
       

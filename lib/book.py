#!/usr/bin/env python3

# book.py

# book.py

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count

    @property
    def title(self):
        return self._title

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        try:
            int(value)  # Attempt to convert to an integer
        except ValueError:
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    
        
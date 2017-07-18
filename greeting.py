#!/usr/bin/python

class Greeting:

    'Basic class used to display a greeting message.'

    def __init__(self, name):

        self.name = name

    def sayHello(self):

        print "Hello, " + self.name + "!"


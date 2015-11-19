import urllib2
import lxml.html as lh
from lxml import etree
import requests

class Grade_DATA(object):
    """ Docstring for page_data """
    year = ""
    location = ""
    first_n = ""
    last_n = ""
    title = ""
    gross_p = ""
    reg_p = ""
    overtime_p = ""
    other_p = ""

    def __init__(self,yr,loc,fn,ln,t,gp,rp,ovp,op):
        self.year = yr
        self.location = loc
        self.first_n = fn
        self.last_n = ln
        self.title = t
        self.gross_p = gp
        self.reg_p = rp
        self.overtime_p = ovp
        self.other_p = op

def build_grade_data():
    all_obj = []
    return all_obj

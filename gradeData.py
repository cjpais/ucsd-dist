import urllib2
import lxml.html as lh
from lxml import etree
import requests

class Grade_DATA(object):
    """ Docstring for page_data """
    term_code = ""
    sub_code = ""
    cor_code = ""
    cor_title = ""
    inst = ""
    gpa = ""
    perc_a = ""
    perc_b = ""
    perc_c = ""
    perc_d = ""
    perc_f = ""
    perc_w = ""
    # we can also find out the % who did p/np vs %
    perc_p = ""
    perc_np = ""

    def __init__(self,tc,sc,cc,ct,ins,g,pa,pb,pc,pd,pf,pw,pp,pnp):
        self.term_code = tc
        self.sub_code = sc
        self.cor_code = cc
        self.cor_title = ct
        self.inst = ins
        self.gpa = g
        self.perc_a = pa
        self.perc_b = pb
        self.perc_c = pc
        self.perc_d = pd
        self.perc_f = pf
        self.perc_w = pw
        self.perc_p = pp
        self.perc_np = pnp

def build_grade_data():
    all_obj = []
    print "Gathering data"
    for i in range(1,14956):
        if (i % 10 == 0):
            print "%d pages gathered" % i
        webstring = "https://as.ucsd.edu//gradeDistribution/view/id/%d" % i
        doc = lh.parse(urllib2.urlopen(webstring))
        data = []
        for elt in doc.iter('td'):
            text = elt.text_content()
            data.append(text)
        all_obj.append(Grade_DATA(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13]))
    print "finished gathering data"
    return all_obj

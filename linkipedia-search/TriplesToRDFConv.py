# coding: utf-8

import rdflib
import re
# import urlparse

__author__ = 'Booma Sowkarthiga'

from StringIO import StringIO
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS, FOAF
from rdflib.namespace import Namespace
import codecs
# from urlparse import urlparse

# RDFS.label
# # = rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#label')

# FOAF.knows
# # = rdflib.term.URIRef(u'http://xmlns.com/foaf/0.1/knows')


# contents = '''\
# subject1\tpredicate1\tobject1
# subject2\tpredicate2\tobject2'''
# file_object = open("jsontest1.txt")
# file_object = open("work1.txt")
# tabfile = StringIO(file_object)
file_object = codecs.open("work1.txt", "r", "utf-8")
tabfile = file_object
# urn = rdflib.Namespace('http://example.namespace/ex1/prop#')

graph = rdflib.Graph()
graph.bind("rdfs", RDFS.uri)

from rdflib.extras.infixowl import Class
from rdflib import BNode
urn = Namespace('http://example.namespace/ex1/prop#')
for line in tabfile:
    subgraph = Graph()
    triple = line.split('\t')                # triple is now a list of 3 strings
    triple[2] = triple[2].strip('\n')
    print triple
    if triple[1] in ('rdfs:comment'):
        newtriple = (urn[triple[0]], RDFS.comment, Literal(triple[2]))
    elif triple[1] in ('rdfs:label'):
        newtriple = (urn[triple[0]], RDFS.label, Literal(triple[2]))
    else:
        newtriple = (urn[triple[0]], urn[triple[1]], urn[triple[2]])
    graph.add(newtriple)

graph.serialize(destination='outputtest7.xml', format='xml')
print graph.serialize(format='xml')

f1 = open("outputtest8.xml","w")
f= open('outputtest7.xml','r')
for line in f.readlines():
	if re.search('\S',line):
		f1.write(line)




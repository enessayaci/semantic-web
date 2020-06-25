import owl as owl
import rdflib
import json
from flask import Flask, render_template, jsonify, request
from rdflib.plugins.sparql import prepareQuery
from rdflib.graph import Graph
def stringFilter(s):
    start = "("
    end = ""
    return s[s.find(start) + len(start):s.rfind(end)]
def search(key):

    g = Graph()
    result = g.parse('mydataset.rdf')



    sorgum = prepareQuery('''
                                              SELECT ?personName ?companyName ?workedOn  WHERE
                                             {
                                               ?employee ontology:workedFor ?company.
                                               ?company ontology:companyName  ?companyName.
                                               ?company ontology:workedOn ?workedOn.
                                               ?employee ontology:personName ?personName
                                                FILTER (?workedOn="''' + key + '''"^^xsd:string)
                                      
                                               }''',
                          initNs={"ontology": 'http://localhost:8080/mydataset/'})

    queryResults = []
    counter = 0

    for i in result.query(sorgum):
        a=stringFilter(i[0])
        b=stringFilter(i[1])
        c = stringFilter(i[2])
        element = [a,[b]]
        for elem in queryResults:
            if a == elem[0]:
                elem[1].append(b)
                counter=1

        if counter !=1:
            queryResults.append(element)
        counter = 0




    return queryResults


import json

from flask import request, make_response, jsonify
from flask_restplus import Resource

from .api import API

'''
    Version
'''
@API.route('/about/version')
class version(Resource):
    def get(self):
        return 'v1.0.0'

from Lib import TermSearch

term_search_en = TermSearch('en')
term_search_es = TermSearch('es')

'''
    Search
'''
@API.route('/SearchSymptoms')
@API.route('/search/symptoms')
class search_symptoms(Resource):
    def get(self):
        query = request.args.get('q') or ''
        if query.strip() == '': return [], 200
        print(query)

        qlow = query.lower()
        lang = request.args.get('lang') or 'en'
        rows = request.args.get('rows') or 10
        rows = int(rows)

        if lang == 'en':
            print('Using english language')
            if qlow.startswith('hp:'):
                resp = term_search_en.search_symptoms_ids(qlow, rows)
            else:
                resp = term_search_en.search_symptoms(query, rows)
        else:
            print('Using spanish language')
            if qlow.startswith('hp:'):
                resp = term_search_es.search_symptoms_ids(qlow, rows)
            else:
                resp = term_search_es.search_symptoms(query, rows)

        return resp, 200

@API.route('/SearchDiseases')
@API.route('/search/diseases')
class search_diseases(Resource):
    def get(self):
        query = request.args.get('q') or ''
        if query.strip() == '': return [], 200
        print(query)

        qlow = query.lower()
        lang = request.args.get('lang') or 'en'
        rows = request.args.get('rows') or 10
        rows = int(rows)

        if lang == 'en':
            print('Using english language')
            if qlow.startswith('orpha:'):
                resp = term_search_en.search_diseases_ids(qlow, rows)
            else:
                resp = term_search_en.search_diseases(query, rows)
        else:
            print('Using spanish language')
            if qlow.startswith('orpha:'):
                resp = term_search_es.search_diseases_ids(qlow, rows)
            else:
                query = query.replace('sindrome', 'síndrome')
                if len(query.strip().split(' ')) == 1:
                    resp = term_search_es.search_diseases_prefix(query, 'síndrome', rows)
                else:
                    resp = term_search_es.search_diseases(query, rows)

        return resp, 200

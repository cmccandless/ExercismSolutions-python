#!/usr/bin/env python3.6
from functools import wraps
import json


def json_io(func):
    @wraps(func)
    def dec(self, url, payload=None):
        if payload is not None and isinstance(payload, str):
            payload = json.loads(payload)
        return json.dumps(func(self, url, payload), indent=2)
    return dec


def update_db(func):
    @wraps(func)
    def dec(self, *args, **kwargs):
        if self.db is None:
            self.db = {}
        elif not isinstance(self.db, dict):
            raise TypeError('database must be a dictionary')
        if 'users' not in self.db:
            self.db['users'] = []
        return func(self, *args, **kwargs)
    return dec


class RestAPI(object):
    def __init__(self, database=None):
        self.db = database

    def __balance_db__(self):
        for user in self.db['users']:
            balance = 0
            for other in self.db['users']:
                other_name = other['name']
                if user['name'] == other_name:
                    continue
                owed = user['owed_by'].pop(other_name, 0)
                owes = user['owes'].pop(other_name, 0)
                delta = owed - owes
                if delta > 0:
                    user['owed_by'][other_name] = delta
                elif delta < 0:
                    user['owes'][other_name] = -delta
                balance += delta
            user['balance'] = balance

    @update_db
    @json_io
    def get(self, url, payload=None):
        if url == '/users':
            if payload is None:
                return self.db
            else:
                return {
                    'users': [
                        u for u in self.db['users']
                        if u['name'] in payload['users']
                    ]
                }

    @update_db
    @json_io
    def post(self, url, payload):
        if url == '/add':
            user = {
                'name': payload['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0
            }
            self.db['users'].append(user)
            return user
        elif url == '/iou':
            lender_name = payload['lender']
            borrower_name = payload['borrower']
            for user in self.db['users']:
                if user['name'] == lender_name:
                    user['owed_by'][borrower_name] = (
                        user['owed_by'].get(borrower_name, 0) +
                        payload['amount']
                    )
                    lender = user
                elif user['name'] == borrower_name:
                    user['owes'][lender_name] = (
                        user['owes'].get(lender_name, 0) +
                        payload['amount']
                    )
                    borrower = user
            self.__balance_db__()
            return {
                'users': sorted([lender, borrower], key=lambda u: u['name'])
            }

import json
import unittest
from json import loads
from subdomainslookup import Response, ErrorMessage, Result


_json_response_ok = '''{
    "search":"gmail.com",
    "result":{
        "count":8,
        "records":[
            {
                "domain":"alt1.smtp.gmail.com",
                "firstSeen":1571374592,
                "lastSeen":1592164815
            },
            {
                "domain":"alt118.gmail.com",
                "firstSeen":1553876927,
                "lastSeen":1592164709
            },
            {
                "domain":"imap.gmail.com",
                "firstSeen":1571394086,
                "lastSeen":1595857361
            },
            {
                "domain":"mta-sts.gmail.com",
                "firstSeen":1571402941,
                "lastSeen":1592203333
            },
            {
                "domain":"pop.gmail.com",
                "firstSeen":1571399508,
                "lastSeen":1595857437
            },
            {
                "domain":"smtp-relay.gmail.com",
                "firstSeen":1571375257,
                "lastSeen":1595857445
            },
            {
                "domain":"smtp.gmail.com",
                "firstSeen":1571375229,
                "lastSeen":1595526061
            },
            {
                "domain":"www.gmail.com",
                "firstSeen":1586736000,
                "lastSeen":1595857483
            }
        ]
    }
}'''

_json_response_error = '''{
    "code": 403,
    "messages": "Access restricted. Check credits balance or enter the correct API key."
}'''


class TestModel(unittest.TestCase):

    def test_response_parsing(self):
        response = loads(_json_response_ok)
        parsed = Response(response)
        self.assertEqual(parsed.search, response['search'])
        self.assertIsInstance(parsed.result, Result)
        self.assertIsInstance(parsed.result.records, list)
        self.assertEqual(
            parsed.result.records[0].domain,
            response['result']['records'][0]['domain'])
        self.assertEqual(
            parsed.result.records[0].first_seen.timestamp(),
            int(response['result']['records'][0]['firstSeen']))
        self.assertEqual(
            parsed.result.records[0].last_seen.timestamp(),
            int(response['result']['records'][0]['lastSeen']))

        self.assertEqual(
            parsed.result.records[2].domain,
            response['result']['records'][2]['domain'])
        self.assertEqual(
            parsed.result.records[2].first_seen.timestamp(),
            int(response['result']['records'][2]['firstSeen']))
        self.assertEqual(
            parsed.result.records[2].last_seen.timestamp(),
            int(response['result']['records'][2]['lastSeen']))

    def test_error_parsing(self):
        error = loads(_json_response_error)
        parsed_error = ErrorMessage(error)
        self.assertEqual(parsed_error.code, error['code'])
        self.assertEqual(parsed_error.message, error['messages'])

    def test_comparing_two_models(self):
        model1 = Response(json.loads(_json_response_ok))
        model2 = Response(json.loads(_json_response_ok))
        self.assertEqual(model1, model2)

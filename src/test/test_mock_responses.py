import unittest
import json
from src.test.base import BaseTestCase


def sowing_form(self):
    return self.client.post(
        '/sowing_form/',
        data=json.dumps(dict(
            date='2021-03-16',
            time='2021-03-16T19:21:33.196Z',
            plot=0,
            crop='string',
            quantity=0,
            time_to_harvest='string',
            harvest_duration='string',
            expected_yield='string',
            note='string'
        )),
        content_type='application/json'
    )


class TestSowingForm(BaseTestCase):

    def test_sowing_form(self):
        """ Test for mock response received for sowing form """
        with self.client:
            # user registration
            api_response = sowing_form(self)
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction completed")
            self.assertEqual(api_response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

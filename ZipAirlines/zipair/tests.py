from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


# Create your tests here.

correct_data = [
    {
        "id": 1,
        "passengers": 10
    },{
        "id": 2,
        "passengers": 20
    },{
        "id": 3,
        "passengers": 30
    },{
        "id": 4,
        "passengers": 40
    },{
        "id": 5,
        "passengers": 50
    },{
        "id": 6,
        "passengers": 60
    },{
        "id": 7,
        "passengers": 70
    },{
        "id": 8,
        "passengers": 80
    },{
        "id": 9,
        "passengers": 90
    },{
        "id": 10,
        "passengers": 100
    }
]

correct_output = [
    {
        "id": 1,
        "passengers": 10,
        "fuel_consumption_per_minute": 0.02,
        "max_flight_time": 10000
    },
    {
        "id": 2,
        "passengers": 20,
        "fuel_consumption_per_minute": 0.5945177444479562,
        "max_flight_time": 672.8142326036423
    },
    {
        "id": 3,
        "passengers": 30,
        "fuel_consumption_per_minute": 0.938889830934488,
        "max_flight_time": 639.0526132366489
    },
    {
        "id": 4,
        "passengers": 40,
        "fuel_consumption_per_minute": 1.1890354888959125,
        "max_flight_time": 672.8142326036423
    },
    {
        "id": 5,
        "passengers": 50,
        "fuel_consumption_per_minute": 1.3875503299472804,
        "max_flight_time": 720.6945783638671
    },
    {
        "id": 6,
        "passengers": 60,
        "fuel_consumption_per_minute": 1.553407575382444,
        "max_flight_time": 772.49526718998
    },
    {
        "id": 7,
        "passengers": 70,
        "fuel_consumption_per_minute": 1.6967281192442507,
        "max_flight_time": 825.1174623212952
    },
    {
        "id": 8,
        "passengers": 80,
        "fuel_consumption_per_minute": 1.8235532333438687,
        "max_flight_time": 877.4078928675217
    },
    {
        "id": 9,
        "passengers": 90,
        "fuel_consumption_per_minute": 1.9377796618689758,
        "max_flight_time": 928.8981794059661
    },
    {
        "id": 10,
        "passengers": 100,
        "fuel_consumption_per_minute": 2.042068074395237,
        "max_flight_time": 979.3992791314288
    }
]

short_data = [
    {
        "id": 1,
        "passengers": 10
    }
]

dict_data = {
    "id": 1,
    "passengers": 10
}

wrong_id = [
    {
        "id": 1,
        "passengers": 10
    },{
        "id": 2,
        "passengers": 20
    },{
        "id": 3,
        "passengers": 30
    },{
        "id": 'wrong_id',
        "passengers": 40
    },{
        "id": 5,
        "passengers": 50
    },{
        "id": 6,
        "passengers": 60
    },{
        "id": 7,
        "passengers": 70
    },{
        "id": 8,
        "passengers": 80
    },{
        "id": 9,
        "passengers": 90
    },{
        "id": 10,
        "passengers": 100
    }
]

wrong_pass = [
    {
        "id": 1,
        "passengers": 10
    },{
        "id": 2,
        "passengers": 20
    },{
        "id": 3,
        "passengers": 30
    },{
        "id": 4,
        "passengers": 40
    },{
        "id": 5,
        "passengers": 50
    },{
        "id": 6,
        "passengers": 60
    },{
        "id": 7,
        "passengers": 70
    },{
        "id": 8,
        "passengers": 80
    },{
        "id": 9,
        "passengers": "wrong_password"
    },{
        "id": 10,
        "passengers": 100
    }
]


class AssessmentTestCase(TestCase):
    def test_assess_airplanes_correct(self):
        client = APIClient()
        request = client.post('/assess', correct_data, format='json')
        assert request.status_code == 200, 'Request with correct data should have 200 status_code'
        assert request.data == correct_output, 'Request with correct data has wrong output'

    def test_assess_airplanes_short(self):
        client = APIClient()
        request = client.post('/assess', short_data, format='json')
        assert request.status_code == 400, 'Request with less than 10 data should have 400 status_code'

    def test_assess_airplanes_dict(self):
        client = APIClient()
        request = client.post('/assess', dict_data, format='json')
        assert request.status_code == 400, 'Request with dictionary data should have 400 status_code'

    def test_assess_airplanes_wrong_data(self):
        client = APIClient()
        request = client.post('/assess', wrong_id, format='json')
        assert request.status_code == 400, 'Request with wrong id should have 400 status_code'
        request = client.post('/assess', wrong_pass, format='json')
        assert request.status_code == 400, 'Request with wrong passengers should have 400 status_code'
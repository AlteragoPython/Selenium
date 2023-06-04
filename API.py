import requests

def test_response_content():
    url = 'https://api.punkapi.com/v2/beers/8'
    response = requests.get(url)
    beer_data = response.json()[0]
    assert beer_data["name"] == 'Fake Lager', f"Expected name Fake Lager, but got {beer_data['name']}"
    assert beer_data["abv"] == 4.7, f"Expected abv 4.7, but got {beer_data['abv']}"
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_delete_status_code():
    url = 'https://api.punkapi.com/v2/beers/8'
    response = requests.delete(url)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    response_data = response.json()
    expected_message = 'No endpoint found that matches \'/v2/beers/8\''
    assert response_data["message"] == expected_message, f"Expected message '{expected_message}', but got {response_data['message']}"
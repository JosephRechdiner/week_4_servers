import json

SINGLE_DATA = {
    "url": "",
    "method": "",
    "stats": {
        "total_requests_received": 1,
        "avg_handling_time": 0
    }
}

JSON_ENDPOINT_PATH = "data/endpoints.json"


def create_first_url_data(url, method):
    result = SINGLE_DATA
    result["url"] = url
    result["method"] = method
    return SINGLE_DATA



def write_to_json(path, data):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=3)
    except Exception:
        raise Exception("not found")

def load_from_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data
    except Exception:
        raise Exception("not found")
    
json_data = load_from_json(JSON_ENDPOINT_PATH)


def get_json_data_by_url(url, method):
    for data in json_data:
        if data["url"] == url and data["methd"] == method:
            return data
    return None

def updating_url_data_in_json(url, method, time):
    url_data = get_json_data_by_url(url, method)
    if url_data is None:
        url_data = create_first_url_data(url, method, time)
    else:
        url_data["stats"]["total_requests_received"] += 1
        url_data["stats"]["avg_handling_time"] = (url_data["stats"]["avg_handling_time"] + time ) / url_data["stats"]["total_requests_received"]

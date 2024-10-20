import requests
import pytest
from src.constants import SentimentLabel
from src.data_models import SimpleModelRequest

@pytest.mark.parametrize(
        "review",
        [
            "This product is awesome.",
            "I don't think I like this one - I am not sure yet.",
            "This product stinks - waste of money.",
            "I don't love this one but it is okay.",
            "Absolute trash.",
            "This is great - exactly what I needed!"
        ],
)

def test_predict_endpoint_with_different_reviews(predict_url, review):
    body = SimpleModelRequest(review=review).model_dump()
    response = requests.post(predict_url, json=body)
    response_json = response.json()
    print(response_json)

    assert response.status_code == 200
    assert response_json["label"] in [label.value for label in SentimentLabel]
    assert 0 <= response_json["score"] <= 1
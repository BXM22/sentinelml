from src.features import extract_features


def test_simple_url():
    f = extract_features("https://www.example.com")
    assert f["url_length"] == 23
    assert f["domain_length"] == 15
    assert f["digits_in_url"] == 0
    assert f["digits_in_domain"] == 0
    assert f["dot_count"] == 2
    assert f["hyphen_count"] == 0
    assert f["has_at"] == 0
    assert f["has_ip"] == 0

def test_suspicious_url():
    f = extract_features("https://paypal-checkout.com/checkout?token=1234567890")
    assert f["url_length"] == 53
    assert f["domain_length"] == 19
    assert f["digits_in_url"] == 10
    assert f["digits_in_domain"] == 0
    assert f["dot_count"] == 1
    assert f["hyphen_count"] == 1
    assert f["has_at"] == 0
    assert f["has_ip"] == 0

def test_ip_url():
    f = extract_features("https://192.168.1.1:8080/login")
    assert f["url_length"] == 30
    assert f["domain_length"] == 16
    assert f["digits_in_url"] == 12
    assert f["digits_in_domain"] == 12
    assert f["dot_count"] == 3
    assert f["hyphen_count"] == 0
    assert f["has_at"] == 0
    assert f["has_ip"] == 1

def test_at_symbol():
    assert extract_features("http://paypal.com@evil.com/login")["has_at"] == 1

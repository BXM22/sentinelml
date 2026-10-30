# pytest.ini sets pythonpath, so "src." imports work
from src.features import extract_features


def test_simple_url():
    # a normal, harmless URL: no digits, no hyphens, no "@", not an IP
    f = extract_features("https://www.example.com")
    assert f["url_length"] == 23  # len("https://www.example.com")
    assert f["domain_length"] == 15  # len("www.example.com")
    assert f["digits_in_url"] == 0
    assert f["digits_in_domain"] == 0
    assert f["dot_count"] == 2  # www . example . com
    assert f["hyphen_count"] == 0
    assert f["has_at"] == 0
    assert f["has_ip"] == 0

def test_suspicious_url():
    # lookalike name with a hyphen and a long numeric token in the query string
    f = extract_features("https://paypal-checkout.com/checkout?token=1234567890")
    assert f["url_length"] == 53
    assert f["domain_length"] == 19  # "paypal-checkout.com"
    assert f["digits_in_url"] == 10  # the 10 digits in the token
    assert f["digits_in_domain"] == 0  # the digits are not in the domain
    assert f["dot_count"] == 1
    assert f["hyphen_count"] == 1  # the hyphen in paypal-checkout
    assert f["has_at"] == 0
    assert f["has_ip"] == 0

def test_ip_url():
    # domain is a raw IP address with a port
    f = extract_features("https://192.168.1.1:8080/login")
    assert f["url_length"] == 30
    assert f["domain_length"] == 16  # "192.168.1.1:8080" (port counts)
    assert f["digits_in_url"] == 12  # 8 digits in the IP + 4 in the port
    assert f["digits_in_domain"] == 12
    assert f["dot_count"] == 3
    assert f["hyphen_count"] == 0
    assert f["has_at"] == 0
    assert f["has_ip"] == 1  # matches the "digits, dots, optional :port" pattern

def test_at_symbol():
    # the real host is evil.com; "paypal.com@" is just a decoy before the "@"
    assert extract_features("http://paypal.com@evil.com/login")["has_at"] == 1

import re  # regular expressions, used to recognise an IP address
import urllib.parse as urlparse  #splits urls into parts


def extract_features(url):
    """Turn one URL string into a dict of 8 numbers a model can learn from."""
    #get domain safely
    if "://" not in url:  # urlparse only finds the domain if a scheme (http://) is present
        url = "http://" + url  # add a default scheme so bare "example.com" still parses
    domain = urlparse.urlparse(url).netloc #extracts domain from url

    #features
    digits_in_url = sum(c.isdigit() for c in url)  # count every digit character in the whole URL
    digits_in_domain = sum(c.isdigit() for c in domain)  # same, but only inside the domain
    dot_count = domain.count(".")  # many dots can mean stacked subdomains like a.b.c.evil.com
    hyphen_count = domain.count("-")  # hyphens are common in lookalike names like paypal-login.com
    # the whole domain must be only digits and dots, with an optional :port, to count as an IP
    has_ip = int(bool(re.fullmatch(r"[\d.]+(:\d+)?", domain)))

    return{
        "url_length": len(url),  # characters in the whole URL
        "domain_length": len(domain),  # characters in the domain (port included)
        "digits_in_url": digits_in_url,
        "digits_in_domain": digits_in_domain,
        "dot_count": dot_count,
        "hyphen_count": hyphen_count,
        "has_at": int("@" in url),  # 1 if "@" appears; browsers ignore everything before it, which hides the real host
        "has_ip": has_ip,  # 1 if the domain is an IP address instead of a name
    }

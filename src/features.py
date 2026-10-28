import re
import urllib.parse as urlparse  #splits urls into parts


def extract_features(url):
    #get domain safely
    if "://" not in url:
        url = "http://" + url
    domain = urlparse.urlparse(url).netloc #extracts domain from url

    #features
    digits_in_url = sum(c.isdigit() for c in url)
    digits_in_domain = sum(c.isdigit() for c in domain)
    dot_count = domain.count(".")
    hyphen_count = domain.count("-")
    has_ip = int(bool(re.fullmatch(r"[\d.]+(:\d+)?", domain)))

    return{
        "url_length": len(url),
        "domain_length": len(domain),
        "digits_in_url": digits_in_url,
        "digits_in_domain": digits_in_domain,
        "dot_count": dot_count,
        "hyphen_count": hyphen_count,
        "has_at": int("@" in url),
        "has_ip": has_ip,
    }
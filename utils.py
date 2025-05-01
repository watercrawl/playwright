from urllib.parse import urlparse


def parse_proxy_env(uri):
    parsed = urlparse(uri)
    server = f"{parsed.scheme}://{parsed.hostname}:{parsed.port}"
    username = parsed.username
    password = parsed.password
    return server, username, password

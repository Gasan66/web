def app(environ, start_response):
    query_strings = environ['QUERY_STRING']
    # data = str(query_strings).encode()
    data2 = query_strings.replace('&','\n').encode()
    # for query_string in query_strings:
    #     data2 += (query_string + '\n').encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(query_strings)))
    ])
    return [data2]

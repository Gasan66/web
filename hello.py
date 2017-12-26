def app(environ, start_response):
    query_strings = environ['QUERY_STRING']
    # data = str(query_strings).encode()
    data2 = [bytes(i + '\n', 'ascii') for i in query_strings.split('&')]
    # for query_string in query_strings:
    #     data2 += (query_string + '\n').encode()
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data2)))
    ])
    return [data2]


def wsgi_application(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return body

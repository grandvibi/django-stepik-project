bind="0.0.0.0:8080"
pythonpath="/home/box/web"


def wsgi_application(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = [x + '\n'for x in env['QUERY_STRING'].split('&')]
    #body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return body

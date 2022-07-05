#	웹 서버 응용 프로그램을 만들려면? ― wsgiref
"""
웹 브라우저 주소 창으로 두 수를 입력받아 곱한 다음 그 결과를 반환하는 WSGI 프로그램을 만들려면 어떻게 해야 할까?
http://52.78.8.100:8088/?a=3&b=4
예를 들어 서버의 IP 주소가 52.78.8.100 이고 8088 포트로 아파치 웹 서버를 운영할 때 이처럼 URL을 요청하면 브라우저에 다음과 같은 결과가 출력되도록 WSGI 프로그램을 작성해야 한다.
"""
from urllib import parse

def application(environ, start_response):
    params = parse.parse_qs(environ['QUERY_STRING'])
    a = params.get('a', [0])[0]
    b = params.get('b', [0])[0]
    result = int(a) * int(b)

    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    return [f'Result:{result}'.encode('utf-8')]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    with make_server('', 8088, application) as httpd:
        print("Serving on port 8088...")
        httpd.serve_forever()
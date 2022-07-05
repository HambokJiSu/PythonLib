#	웹 페이지에서 원하는 텍스트만 뽑으려면? ― html.parser
#	https://docs.python.org/ko/3/library/html.parser.html
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_strong = False

    def handle_starttag(self, tag, attrs):
        if tag == 'strong':  # <strong> 태그 시작
            self.is_strong = True

    def handle_endtag(self, tag):
        if tag == 'strong':  # </strong> 태그 닫힘
            self.is_strong = False

    def handle_data(self, data):
        if self.is_strong:  # <strong>~</strong> 구간인 경우
            print(data)     # 데이터를 출력


with open(r'markup_lang\html_sample1.html') as f:
    parser = MyHTMLParser()
    parser.feed(f.read())
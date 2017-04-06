# encoding = utf-8
class HtmlOutput(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open("output.html", 'w', encoding='utf-8') as f:
            f.write("<html>")
            f.write("<body>")
            f.write("<table border='1' cellspacing='1' cellpadding='1'>")
            for x in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>" % x['title'])
                f.write("<td>%s</td>" % x['summary'])
                f.write("<td><a href='%s'>%s</a></td>" % (x['url'], x['url']))
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")


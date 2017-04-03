import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
print template_dir
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape= True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
		
	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


class MainPage(Handler):
	def get(self):
		self.render("translate.html")
	def post(self):
		items = self.request.get("text")
		output = rotFunc(items)
		self.render("translate.html", text=output)


app = webapp2.WSGIApplication([('/', MainPage)], debug = True)

def rotFunc(items):
	output = ""
	for c in items:
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			output += (chr((ord(c)+13-ord('a'))%26 + ord('a')))
		elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
			output += (chr((ord(c)+13-ord('A'))%26 + ord('A')))
		else:
			output += (c)

	return 	output


from google.appengine.ext import webapp

register = webapp.template.create_template_register()

@register.filter
def firstline(value):
  # return the first line of value.
  # If value is a single line, just return it, unchanged.
  if value.count("\n") == 0:
    return value
  else:
    return value.split("\n")[0]

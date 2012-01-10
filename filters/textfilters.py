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

@register.filter
def line_breaks_to_br(value):
  # convert line breaks to '<br/>'
  return value.replace("\n", "<br/>")

@register.filter
def lines_as_ps(value):
  # convert lines to html <p>
  lines = value.split("\n")
  ps = ["<p>" + s + "</p>" for s in lines]
  return "\n".join(ps)

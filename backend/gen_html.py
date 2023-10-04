from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

template = env.get_template("product-detail.html")

# template.render(**{
#     "name": "here"
# })

out_str = template.render(**{
    "name": "here"
})

f = open('abc.html', 'w')
f.write(out_str)
f.close()

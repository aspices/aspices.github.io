import json

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

product_list = json.load(open('app/product-list.json'))


# template = env.get_template("product-detail.html")
#
# out_str = template.render(**{
#     "name": "here"
# })
#
# f = open('abc.html', 'w')
# f.write(out_str)
# f.close()

def gen_product_list():
    template = env.get_template("product-list.html")
    out_str = template.render(data=product_list)

    f = open('../products/index.html', 'w')
    f.write(out_str)
    f.close()


def gen_product_detail():
    template = env.get_template("product-detail.html")

    for (product_key, product) in product_list.items():
        related_list = []
        for related_key in product.get('related_list'):
            related_list.append(product_list[related_key])
        out_str = template.render(
            current_product=product, related_list=related_list
        )
        f = open('../products/{}.html'.format(product.get('key')), 'w')
        f.write(out_str)
        f.close()


gen_product_list()
gen_product_detail()

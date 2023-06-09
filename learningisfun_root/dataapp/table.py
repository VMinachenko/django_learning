import django_tables2 as tables

class PackagesTable(tables.Table):
    package_name = tables.Column(attrs={"td": {"class": "package-name"}})
    stars = tables.Column(attrs={"th": {"class": "stars-header"}, "td": {"class": "stars-cell"}}, order_by=("stars"))
    forks = tables.Column(attrs={"td": {"class": "forks"}})

    class Meta:
        template_name = 'base.html'
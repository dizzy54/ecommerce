from django.conf.urls import url


from .views import ProductDetailView, ProductListView, VariationListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    # url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]

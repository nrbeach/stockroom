"""
URL configuration for stockroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from stockroom import settings
from web import views as web_views
from web.forms import NewCategoryForm
from web.forms import NewComponentForm
from web.forms import NewInterfaceForm
from web.forms import NewLocationForm
from web.models import Category
from web.models import Component
from web.models import Interface
from web.models import Location

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", web_views.index),
    path(
        "new/",
        web_views.new_component,
        {"url": "/new/"},
        name="new",
    ),
    path(
        "new/category/",
        web_views.generic_new_item,
        {"cls": Category, "form_cls": NewCategoryForm, "url": "/category/"},
        name="category",
    ),
    path(
        "new/location/",
        web_views.generic_new_item,
        {"cls": Location, "form_cls": NewLocationForm, "url": "/location/"},
        name="location",
    ),
    path(
        "new/interface/",
        web_views.generic_new_item,
        {"cls": Interface, "form_cls": NewInterfaceForm, "url": "/interface/"},
        name="interface",
    ),
    path(
        "category/",
        web_views.generic_list_all,
        {"cls": Category, "url": "/category/", "fieldname": "category"},
        name="category",
    ),
    path(
        "location/",
        web_views.generic_list_all,
        {"cls": Location, "url": "/location/", "fieldname": "location"},
        name="location",
    ),
    path(
        "interface/",
        web_views.generic_list_all,
        {"cls": Interface, "url": "/interface/", "fieldname": "interfaces"},
        name="interface",
    ),
    path(
        "edit/<uuid:uuid>",
        web_views.generic_edit_item,
        {"cls": Component, "files": True},
        name="edit",
    ),
    path(
        "location/edit/<uuid:uuid>",
        web_views.generic_edit_item,
        {"cls": Location, "files": False},
        name="edit_location",
    ),
    path(
        "category/edit/<uuid:uuid>",
        web_views.generic_edit_item,
        {"cls": Category, "files": False},
        name="edit_category",
    ),
    path(
        "interface/edit/<uuid:uuid>",
        web_views.generic_edit_item,
        {"cls": Interface, "files": False},
        name="edit_interface",
    ),
    path("edit/<uuid:uuid>/delete", web_views.generic_delete_item, {"cls": Component}),
    path(
        "category/edit/<uuid:uuid>/delete",
        web_views.generic_delete_item,
        {"cls": Category},
    ),
    path(
        "location/edit/<uuid:uuid>/delete",
        web_views.generic_delete_item,
        {"cls": Location},
    ),
    path(
        "interface/edit/<uuid:uuid>/delete",
        web_views.generic_delete_item,
        {"cls": Interface},
    ),
    path(
        "detail/<uuid:uuid>",
        web_views.generic_detail,
        {"cls": Component, "params": {"pk": None}, "title": ""},
        name="detail",
    ),
    path(
        "category/<uuid:uuid>",
        web_views.generic_detail,
        {"cls": Category, "params": {"category": None}, "title": "Category"},
    ),
    path(
        "location/<uuid:uuid>",
        web_views.generic_detail,
        {"cls": Location, "params": {"location": None}, "title": "Location"},
    ),
    path(
        "interface/<uuid:uuid>",
        web_views.generic_detail,
        {"cls": Interface, "params": {"interfaces": None}, "title": "Interface"},
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

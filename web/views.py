from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from web.forms import EditCategory
from web.forms import EditComponent
from web.forms import EditInterface
from web.forms import EditLocation
from web.forms import NewComponentForm
from web.models import Category
from web.models import Component
from web.models import Interface
from web.models import Location


def generic_detail(request, uuid, cls, params, title):
    for k in params.keys():
        params[k] = uuid
    if request.method == "GET":
        if cls is not Component:
            components = Component.objects.filter(**params)
            name = cls.objects.filter(id=uuid)[0]
            return render(
                request,
                "web/detail.html",
                {
                    "components": components,
                    "context": {"title": title, "name": name, "uuid": uuid},
                },
            )
        component = get_object_or_404(cls, **params)
        return render(
            request,
            "web/component_detail.html",
            {"component": component, "context": {"uuid": uuid}},
        )


def index(request):
    components = Component.objects.all()
    return render(request, "web/index.html", {"components": components})


def generic_list_all(request, cls, url, fieldname):
    objects = cls.objects.all()
    counts = []
    for object in objects:
        c = Component.objects.filter(**{fieldname: object}).count()
        counts.append((object.pk, object.name, c))
    return render(
        request,
        "web/list_all.html",
        {
            "objects": objects,
            "counts": counts,
            "context": {"url": url, "cls": url.replace("/", "").capitalize()},
        },
    )


def new_component(request, url):
    if request.method == "POST":
        form = NewComponentForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data:
                interfaces = form.cleaned_data.pop("interfaces")
                c = Component(**form.cleaned_data)
                c.save()
                c.interfaces.set(interfaces)
                return HttpResponseRedirect("/")
        return render(request, "web/invalid_form.html", {form: "form"})

    else:
        form = NewComponentForm()
    return render(
        request, "web/form_simple.html", {"form": form, "context": {"url": url}}
    )


def generic_new_item(request, cls, form_cls, url, files=False):
    # TODO I need to revert this to a component specific view to handle many to many.
    # Save the base object, then add each many to many relation, or perhaps scrap the interface relation entirely?
    # TODO I may be able to use `form.is_multipart()` to remove the files parameter
    if request.method == "POST":
        form = form_cls(request.POST, request.FILES if files else None)
        if form.is_valid():
            if form.cleaned_data:
                c = cls(**form.cleaned_data)
                c.save()
                return HttpResponseRedirect("/")
        return render(request, "web/invalid_form.html", {form: "form"})

    else:
        form = form_cls()
    return render(
        request, "web/form_simple.html", {"form": form, "context": {"url": url}}
    )


def generic_edit_item(request, uuid, cls, files):
    dispatch = {
        Component: EditComponent,
        Location: EditLocation,
        Category: EditCategory,
        Interface: EditInterface,
    }
    dispatch_form = dispatch[cls]
    c = get_object_or_404(cls, pk=uuid)
    if request.method == "GET":
        url = request.path_info.strip(str(uuid))
        form = dispatch_form(instance=c)
        return render(
            request,
            "web/form_simple.html",
            {"form": form, "context": {"pk": c.pk, "url": url}},
        )
    elif request.method == "POST":
        form = dispatch_form(request.POST, request.FILES if files else None, instance=c)
        if form.is_valid():
            form.save()
            url = request.path_info.replace("/edit", "")
            return HttpResponseRedirect(url)
        return render(request, "web/invalid_form.html", {"form": form})


def generic_delete_item(request, uuid, cls):
    if request.method == "POST":
        c = get_object_or_404(cls, pk=uuid)
        c.delete()
    return index(request)

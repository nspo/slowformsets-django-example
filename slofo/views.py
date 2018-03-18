from django.shortcuts import render
from slofo.forms import *
from django.forms import inlineformset_factory
from django.shortcuts import redirect

def author_update(request, author_id=None):
    if author_id is None:
        author = Author()
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=1, can_delete=False)
    else:
        author = Author.objects.get(pk=author_id)
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=1, can_delete=True)

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author, prefix="main")
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('/author/'+str(form.instance.pk))
    else:
        form = AuthorForm(instance=author, prefix="main")
        formset = BookInlineFormSet(instance=author, prefix="nested", queryset=Book.objects.prefetch_related("publisher").filter(author=author.pk))

    return render(request, "author_update.html", {"form": form, "formset": formset})
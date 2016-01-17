from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django CRUD Example</h1>
    <a href="/books_cbv/">Class Based Views</a><br>
    <a href="/books_fbv/">Function Based Views</a><br>
    <a href="/books_fbv_user/">Function Based Views with User Access</a><br>
    <a href="/books_pc_formset/">Parent/Child using Formset</a><br>
    <a href="/books_pc_formset2/">Parent/Child using Formset and Foreign Key</a><br>
    <a href="/books_pc_multi_view/">Parent/Child using multiple views</a><br>
    """
    return HttpResponse(html)

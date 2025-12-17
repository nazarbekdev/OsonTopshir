from django.shortcuts import render

def landing(request):
    documents = [
        {
            "title": "Kurs ishi",
            "icon": "document-text",
        },
        {
            "title": "Mustaqil ish",
            "icon": "clipboard-document",
        },
        {
            "title": "Tezis",
            "icon": "pencil-square",
        },
        {
            "title": "Slayd",
            "icon": "presentation-chart-bar",
        },
        {
            "title": "Essay",
            "icon": "document",
        },
        {
            "title": "Ma’ruza matni",
            "icon": "book-open",
        },
    ]

    return render(request, "landing.html", {
        "documents": documents
    })


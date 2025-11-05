from django.http import HttpResponse

def list_singers():
    singers = [
        {'id': 1, 'name': 'Океан Ельзи', 'genre': 'Рок', 'lead_singer': 'Святослав Вакарчук', 'slug': 'okean-elzy'},
        {'id': 2, 'name': 'Бумбокс', 'genre': 'Рок, Хіп-хоп', 'lead_singer': 'Андрій Хливнюк', 'slug': 'bumboks'}
    ]
    return singers

def popular_singers(request):
    html_content = """
        <h1>Популярні співаки України</h1>
        <ul>
    """
    for singer in list_singers():
        html_content += f"<li><strong>{singer['name']}</strong> - {singer['genre']} (Вокаліст: {singer['lead_singer']})</li>"
    html_content += """
        </ul>
    """
    return HttpResponse(html_content, content_type='text/html; charset=utf-8')
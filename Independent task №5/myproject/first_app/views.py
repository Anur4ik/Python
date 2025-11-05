from django.http import HttpResponse

def info_list():
    info = [
        {'id': 1, 'name': 'Олександр', 'surname': 'Котасов', 'year': '19', 'group': 'ІСД-32','email':'st8483500@stud.duikt.edu.ua'},
    ]
    return info

def table(request):
    html_content = """
        <h1>Інформація про мене </h1>
      <table border="1" cellpadding="5">           
        <tr><th>ID</th>
                    <th>Ім’я</th>
                    <th>Прізвище</th>
                    <th>Вік</th>
                    <th>Група</th>
                    <th>Email</th>
        </tr>
    """
    for info in info_list():
        html_content += f"""
                  <tr>
                      <td>{info['id']}</td>
                      <td>{info['name']}</td>
                      <td>{info['surname']}</td>
                      <td>{info['year']}</td>
                      <td>{info['group']}</td>
                      <td>{info['email']}</td>
                  </tr>
          """
    html_content += """
     </table>
    """
    return HttpResponse(html_content, content_type='text/html; charset=utf-8')
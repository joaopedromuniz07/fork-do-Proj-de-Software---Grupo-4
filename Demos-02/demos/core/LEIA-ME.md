# Calendário eleitoral – como colocar no site (Python + Django + HTML + CSS)

Sem JavaScript. Os dados e a situação de cada data ("Concluído", "Em andamento",
"Próxima data") são calculados em Python, na view.

## Arquivos e onde colocar
| Arquivo | Onde vai |
|---|---|
| `calendario_dados.py` | pasta do app (junto com `views.py`) |
| `calendario.html` | pasta de templates (junto com `login.html`, `salvos.html`) |
| `calendario.css` | `static/core/css/` (junto com `salvos.css`) |
| `test_calendario.py` | opcional: teste automático (ver passo 5) |

## 1. View (`views.py`)
No topo:
```python
from .calendario_dados import montar_fases
```
Junto com as outras views:
```python
def calendario(request):
    return render(request, 'core/calendario.html', {'fases': montar_fases()})
```
Se o seu `login.html` está em `core/templates/` (sem a subpasta `core`), use
`'calendario.html'`.

## 2. Rota (`urls.py` do app)
```python
path('calendario/', views.calendario, name='calendario'),
```

## 3. Link para a página
Por exemplo, no rodapé do `index.html`:
```html
<a href="{% url 'calendario' %}">Calendário eleitoral</a>
```

## 4. Como testar
`python manage.py runserver` e abra `/calendario/`.
(Não abre no Live Server, por causa do `{% static %}` e do `{% url %}`.)

## 5. Teste automático (opcional)
Copie `test_calendario.py` para a pasta do app (ou cole o conteúdo no `tests.py`)
e rode `python manage.py test`. Ele confere que, em 5/11/2026, a próxima data é a
justificativa do 1º turno, que o 2º turno aparece como concluído e que a página
abre sem `<script>`.

## Como editar as datas
Tudo está em `calendario_dados.py`, na lista `FASES`: início, fim (ou `None`),
texto exibido, título, descrição e `destaque` (True para marcos importantes).
Para outra eleição, troque os eventos.

## Fonte e o que conferir
- Fonte principal: página do TSE "Eleições 2026: confira as principais datas do
  calendário eleitoral" (a tela cita o link; conferido em 5/11/2026).
- A posse de senadores e deputados em 1º de fevereiro de 2027 NÃO está nessa
  página do TSE. Vem de reportagem (NSC Total). Confira na Constituição e na
  resolução do TSE antes de usar como oficial; depois remova a nota no fim da
  página (no `calendario.html`) e o trecho "(Fonte secundária...)" do evento.

## Git
Mensagem sugerida: `Sprint 7: cria tela de calendário eleitoral`
Evidência do card: link para `calendario.html` no GitHub.

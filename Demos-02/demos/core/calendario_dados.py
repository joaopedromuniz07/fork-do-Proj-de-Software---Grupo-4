"""
Dados do calendário eleitoral 2026 e cálculo da situação de cada data.

Fonte principal: página do TSE "Eleições 2026: confira as principais datas
do calendário eleitoral". Conferido em 5 de novembro de 2026.

Para editar uma data, altere o texto e as datas abaixo. Para outra eleição,
troque os eventos de FASES.
"""

from datetime import date


# Cada evento: início, fim (None se for um único dia), rótulo exibido,
# título, descrição e se é um marco importante (destaque).
FASES = [
    {
        'titulo': 'Preparação',
        'descricao': 'De janeiro a julho: regras, filiações e prazos para quem pretende se candidatar.',
        'eventos': [
            {
                'inicio': date(2026, 1, 1),
                'fim': None,
                'rotulo': '1º de janeiro',
                'titulo': 'Pesquisas de opinião eleitoral',
                'texto': 'Passa a ser obrigatório registrar na Justiça Eleitoral as pesquisas sobre a eleição.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 3, 5),
                'fim': date(2026, 4, 3),
                'rotulo': '5 de março a 3 de abril',
                'titulo': 'Janela partidária',
                'texto': 'Deputados federais, estaduais e distritais podem trocar de partido sem perder o mandato por infidelidade.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 4, 4),
                'fim': None,
                'rotulo': '4 de abril',
                'titulo': 'Filiação, domicílio e desincompatibilização',
                'texto': 'Último dia para fixar domicílio eleitoral e ter a filiação partidária aprovada. Presidente, governadores e prefeitos que queiram disputar outro cargo precisam renunciar até esta data.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 5, 7),
                'fim': None,
                'rotulo': '7 de maio',
                'titulo': 'Fechamento do cadastro eleitoral',
                'texto': 'Último dia para pedir primeiro título, transferência ou revisão de dados antes da eleição.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 7, 4),
                'fim': None,
                'rotulo': '4 de julho',
                'titulo': 'Restrições a agentes públicos',
                'texto': 'Começam limites a nomeações, demissões sem justa causa, contratações e participação em inaugurações de obras.',
                'destaque': False,
            },
        ],
    },
    {
        'titulo': 'Candidaturas e campanha',
        'descricao': 'De julho a setembro: partidos escolhem candidatos, a Justiça Eleitoral recebe os registros e a campanha começa.',
        'eventos': [
            {
                'inicio': date(2026, 7, 20),
                'fim': date(2026, 8, 5),
                'rotulo': '20 de julho a 5 de agosto',
                'titulo': 'Convenções partidárias',
                'texto': 'Os partidos decidem coligações e escolhem quem será candidato.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 8, 15),
                'fim': None,
                'rotulo': '15 de agosto',
                'titulo': 'Registro de candidaturas',
                'texto': 'Último dia para partidos, federações e coligações pedirem o registro das candidaturas na Justiça Eleitoral.',
                'destaque': True,
            },
            {
                'inicio': date(2026, 8, 16),
                'fim': None,
                'rotulo': '16 de agosto',
                'titulo': 'Início da propaganda eleitoral',
                'texto': 'A campanha pode começar nas ruas e na internet.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 8, 28),
                'fim': date(2026, 10, 1),
                'rotulo': '28 de agosto a 1º de outubro',
                'titulo': 'Horário eleitoral gratuito (1º turno)',
                'texto': 'Propaganda dos candidatos no rádio e na TV.',
                'destaque': False,
            },
        ],
    },
    {
        'titulo': 'Votação',
        'descricao': 'Os dois dias de voto de 2026.',
        'eventos': [
            {
                'inicio': date(2026, 10, 4),
                'fim': None,
                'rotulo': '4 de outubro',
                'titulo': 'Votação do 1º turno',
                'texto': 'Das 8h às 17h (horário de Brasília). Cargos em disputa: presidente, governadores, senadores, deputados federais, estaduais e distritais.',
                'destaque': True,
            },
            {
                'inicio': date(2026, 10, 9),
                'fim': date(2026, 10, 23),
                'rotulo': '9 a 23 de outubro',
                'titulo': 'Horário eleitoral gratuito (2º turno)',
                'texto': 'Propaganda no rádio e na TV para os cargos que tiveram segundo turno.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 10, 25),
                'fim': None,
                'rotulo': '25 de outubro',
                'titulo': 'Votação do 2º turno',
                'texto': 'Realizado onde nenhum candidato alcançou a maioria necessária no 1º turno.',
                'destaque': True,
            },
        ],
    },
    {
        'titulo': 'Depois da eleição',
        'descricao': 'Resultados oficiais, justificativas e posse dos eleitos.',
        'eventos': [
            {
                'inicio': date(2026, 11, 3),
                'fim': None,
                'rotulo': '3 de novembro',
                'titulo': 'Reabertura do cadastro eleitoral',
                'texto': 'Voltam os atendimentos presenciais e os serviços online, incluindo a certidão de quitação eleitoral.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 12, 3),
                'fim': None,
                'rotulo': '3 de dezembro',
                'titulo': 'Justificativa do 1º turno',
                'texto': 'Prazo para justificar a ausência no 1º turno sem penalidade.',
                'destaque': False,
            },
            {
                'inicio': date(2026, 12, 18),
                'fim': None,
                'rotulo': 'Até 18 de dezembro',
                'titulo': 'Diplomação dos eleitos',
                'texto': 'Data-limite para a Justiça Eleitoral entregar o diploma aos eleitos. Os tribunais regionais podem marcar datas anteriores.',
                'destaque': True,
            },
            {
                'inicio': date(2027, 1, 5),
                'fim': None,
                'rotulo': '5 de janeiro de 2027',
                'titulo': 'Posse do presidente e vice-presidente',
                'texto': 'Cerimônia no Congresso Nacional.',
                'destaque': True,
            },
            {
                'inicio': date(2027, 1, 6),
                'fim': None,
                'rotulo': '6 de janeiro de 2027',
                'titulo': 'Posse dos governadores e vices',
                'texto': 'Cerimônias nas Assembleias Legislativas.',
                'destaque': True,
            },
            {
                'inicio': date(2027, 1, 8),
                'fim': None,
                'rotulo': '8 de janeiro de 2027',
                'titulo': 'Justificativa do 2º turno',
                'texto': 'Prazo final para justificar a ausência no 2º turno.',
                'destaque': False,
            },
            {
                'inicio': date(2027, 2, 1),
                'fim': None,
                'rotulo': '1º de fevereiro de 2027',
                'titulo': 'Posse de senadores e deputados',
                'texto': 'Senadores e deputados federais tomam posse no Congresso Nacional; deputados estaduais e distritais, em geral na mesma data, conforme a Constituição estadual. (Fonte secundária, ver nota no fim da página.)',
                'destaque': False,
            },
        ],
    },
]


def montar_fases(hoje=None):
    """
    Devolve as fases com a situação de cada evento em relação a `hoje`:
    'concluido', 'agora' (período em andamento) ou 'proximo' (a primeira
    data que ainda vai acontecer). Eventos mais distantes ficam sem situação.
    """
    if hoje is None:
        hoje = date.today()

    proximo_marcado = False
    fases = []

    for fase in FASES:
        eventos = []

        for evento in fase['eventos']:
            item = dict(evento)
            fim = evento['fim'] or evento['inicio']

            if fim < hoje:
                item['status'] = 'concluido'
                item['status_texto'] = 'Concluído'
            elif evento['inicio'] <= hoje <= fim:
                item['status'] = 'agora'
                item['status_texto'] = 'Em andamento'
            elif not proximo_marcado:
                item['status'] = 'proximo'
                item['status_texto'] = 'Próxima data'
                proximo_marcado = True
            else:
                item['status'] = ''
                item['status_texto'] = ''

            eventos.append(item)

        fases.append({
            'titulo': fase['titulo'],
            'descricao': fase['descricao'],
            'eventos': eventos,
        })

    return fases

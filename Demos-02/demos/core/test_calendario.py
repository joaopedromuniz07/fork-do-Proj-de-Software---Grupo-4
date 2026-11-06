from datetime import date

from django.test import TestCase
from django.urls import reverse

from .calendario_dados import montar_fases


class CalendarioTests(TestCase):

    def test_status_apos_o_segundo_turno(self):
        fases = montar_fases(date(2026, 11, 5))
        eventos = [e for f in fases for e in f['eventos']]

        votacao = [e for e in eventos if e['titulo'] == 'Votação do 2º turno'][0]
        proxima = [e for e in eventos if e['status'] == 'proximo']

        self.assertEqual(votacao['status'], 'concluido')
        self.assertEqual(len(proxima), 1)
        self.assertEqual(proxima[0]['titulo'], 'Justificativa do 1º turno')

    def test_periodo_em_andamento(self):
        fases = montar_fases(date(2026, 9, 10))
        eventos = [e for f in fases for e in f['eventos']]
        horario = [e for e in eventos if 'Horário eleitoral gratuito (1º' in e['titulo']][0]
        self.assertEqual(horario['status'], 'agora')

    def test_pagina_abre(self):
        resposta = self.client.get(reverse('calendario'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Calendário eleitoral 2026')
        self.assertNotContains(resposta, '<script')

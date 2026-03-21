import re

with open("index.html", "r") as f:
    html = f.read()

# --- 1. Section 2: Numbers ---
html = html.replace(
    '45.6px;color:var(--ink);letter-spacing:-.04em;margin-bottom:3px">30–50</div>',
    '45.6px;color:var(--ink);letter-spacing:-.04em;margin-bottom:3px">10–20</div>'
)
html = html.replace(
    'embaixadores ativos · primeiras 4 semanas</div>',
    'embaixadoras ativas nesta fase de 30 dias</div>'
)
html = html.replace(
    '<div class="mr"><span class="mr-l">Prospectar para fechar 30</span><span class="mr-v">150–300 abordagens</span></div>',
    '<div class="mr"><span class="mr-l">Prospecção base nos 30 dias</span><span class="mr-v">Até 300 contatos</span></div>'
)
html = html.replace(
    '<div class="mr"><span class="mr-l">Ritmo de prospecção diária</span><span class="mr-v">5–8 contatos/dia</span></div>',
    '<div class="mr"><span class="mr-l">Ritmo de prospecção diária</span><span class="mr-v">10 contatos/dia</span></div>'
)

# --- 2. Funnel Math ---
# Find the exact funnel block
old_fnl = r"""          <div class="fn"><span class="fn-n">50</span><span class="fn-l">Embaixadores recrutados</span><span class="fn-s">Base total</span></div>
          <div class="fn-arr">↓</div>
          <div class="fn"><span class="fn-n">10</span><span class="fn-l">Creators postando com consistência</span><span class="fn-s">20% ativos</span></div>
          <div class="fn-arr">↓</div>
          <div class="fn"><span class="fn-n">5</span><span class="fn-l">Convertendo usuários reais</span><span class="fn-s">10% conversão</span></div>
          <div class="fn-arr">↓</div>
          <div class="fn fn-on"><span class="fn-n">3</span><span class="fn-l">Parceiros de alta performance</span><span class="fn-s">Canal sustentável</span></div>
        </div>
      </div>
      <div class="hl-b"><p>50 creators × 10k reach médio = potencial de <strong>200k–500k impressões</strong> coordenadas no lançamento. Sem ads.</p></div>"""

new_fnl = """          <div class="fn"><span class="fn-n">300</span><span class="fn-l">Perfis prospectados</span><span class="fn-s">Dias 8–20</span></div>
          <div class="fn-arr">↓</div>
          <div class="fn"><span class="fn-n">15+</span><span class="fn-l">Embaixadoras fechadas</span><span class="fn-s">~5% aceitação</span></div>
          <div class="fn-arr">↓</div>
          <div class="fn"><span class="fn-n">25</span><span class="fn-l">Usuárias por parceira</span><span class="fn-s">Pós-lançamento</span></div>
          <div class="fn-arr">↓</div>
          <div class="fn fn-on"><span class="fn-n">300+</span><span class="fn-l">Usuárias qualificadas</span><span class="fn-s">Canal validado</span></div>
        </div>
      </div>
      <div class="hl-b"><p>Trabalhando com um orçamento de US$ 1.000 para prêmios e bônus nos 30 dias. O foco não é <strong>explodir</strong> na internet, mas atrair uma <strong>base engajada inicial sustentável.</strong></p></div>"""

html = html.replace(old_fnl, new_fnl)


# --- 3. Phases ---
old_phases = re.search(r'<div class="ph" id="ph1">.*?</p>\s*</div>\s*</div>\s*</div>', html, re.DOTALL).group(0) # This won't work perfectly due to greedy search.

# Better replacing blocks individually
def repl_between(html_str, start_tag, end_tag, new_content):
    pattern = re.compile(re.escape(start_tag) + r'.*?' + re.escape(end_tag), re.DOTALL)
    return pattern.sub(start_tag + new_content + end_tag, html_str)

html = repl_between(html, '<div class="ph" id="ph1">', '</div>\n  </div>\n\n  <div class="ph" id="ph2">', """
    <div class="ph-hd ph-hd1"><div><div class="ph-num">Fase 01</div><div class="ph-title">Estruturação — Preparação Invisível</div></div><div class="ph-right"><div class="ph-period">Dias 1–7</div><div class="ph-pbar"><div class="ph-pbar-fill" id="ph1-bar" style="width:0%"></div></div><div class="ph-pct" id="ph1-pct">0%</div></div></div>
    <div class="ph-body">
      <p>Você não anuncia publicamente. Você organiza a base. Fechar a narrativa do aplicativo e formatar os materiais de parceiros e links.</p>
      <div class="ph-cols">
        <div class="ph-grp"><h4>Setup obrigatório</h4>
          <ul class="cl" data-sec="s3">
            <li class="ci"><div class="ci-box"></div><span class="ci-text"><strong>Página simples ao ar</strong> — headline: O jeito simples de rastrear nutrição com IA</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text"><strong>Kit embaixadora pronto</strong> — PDF enxuto contendo os links, propostas e o app beta</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text"><strong>CRM formatado</strong> para iniciar as abordagens aos 300 contatos</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text"><strong>Códigos de comissão</strong> ativos e sistema de tracking pronto</span></li>
          </ul>
        </div>
      </div>
    """)

html = repl_between(html, '<div class="ph" id="ph2">', '</div>\n  </div>\n\n  <div class="ph" id="ph3">', """
    <div class="ph-hd ph-hd2"><div><div class="ph-num">Fase 02</div><div class="ph-title">Recrutamento e Onboarding</div></div><div class="ph-right"><div class="ph-period">Dias 8–20</div><div class="ph-pbar"><div class="ph-pbar-fill" id="ph2-bar" style="width:0%"></div></div><div class="ph-pct" id="ph2-pct">0%</div></div></div>
    <div class="ph-body">
      <p>Montar o time de parceiras. A rotina é contatar 10 perfis por dia ativamente, criar vínculos, fazer follow-up e já liberar acesso.</p>
      <div class="ph-cols">
        <div class="ph-grp"><h4>Rotina de Parcerias</h4>
          <ul class="cl" data-sec="s3">
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Prospectar 10 novos perfis por dia usando o fluxo de 3 passos</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Onboarding das parceiras no WhatsApp e envio dos manuais e acessos</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Garantir que as embaixadoras que fecharam, iniciem os seus testes do produto</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Fechamento do calendário da "janela coordenada" de postagens com todas</span></li>
          </ul>
        </div>
      </div>
    """)

html = repl_between(html, '<div class="ph" id="ph3">', '</div>\n  </div>\n\n  <div class="ph" id="ph4">', """
    <div class="ph-hd ph-hd3"><div><div class="ph-num">Fase 03</div><div class="ph-title">Aquecimento e Lançamento Coordenado</div></div><div class="ph-right"><div class="ph-period">Dias 21–30</div><div class="ph-pbar"><div class="ph-pbar-fill" id="ph3-bar" style="width:0%"></div></div><div class="ph-pct" id="ph3-pct">0%</div></div></div>
    <div class="ph-body">
      <p>Dias 21 a 27: conteúdo sutil de "primeiras impressões". Dias 28 a 30: EXPLOSÃO coordenada, postagens combinadas nas mesmas horas gerando FOMO em massa.</p>
      <div class="ph-cols">
        <div class="ph-grp"><h4>Aquecimento (Dias 21-27)</h4>
          <ul class="cl" data-sec="s3">
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Creators postam stories do estilo "Estou testando uma nova forma de bater macros..."</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Perfil oficial entra no ar com material de demonstração de fundo</span></li>
          </ul>
        </div>
        <div class="ph-grp"><h4>Lançamento em Massa (Dias 28-30)</h4>
          <ul class="cl" data-sec="s3">
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Publicação principal simultânea de todas as (+15) embaixadoras ativas juntas</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Time do app repostando as ações oficiais o dia inteiro, respondendo directs e dúvidas</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Sistemas premiando as primeiras ativações de usuários VIPs</span></li>
          </ul>
        </div>
      </div>
    """)

html = repl_between(html, '<div class="ph" id="ph4">', '</div>\n  </div>\n\n  <div class="g-funnel', """
    <div class="ph-hd ph-hd4"><div><div class="ph-num">Fase 04</div><div class="ph-title">Continuidade</div></div><div class="ph-right"><div class="ph-period">Dias 31+</div><div class="ph-pbar"><div class="ph-pbar-fill" id="ph4-bar" style="width:0%"></div></div><div class="ph-pct" id="ph4-pct">0%</div></div></div>
    <div class="ph-body">
      <p>Um lançamento orgânico bem feito vive de constância, não apenas dos primeiros 3 dias de posts e euforia.</p>
      <div class="ph-cols">
        <div class="ph-grp"><h4>Métricas e Otimização</h4>
          <ul class="cl" data-sec="s3">
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Dobrar os esforços apenas com as parceiras do Top 3 Leaderboard de vendas</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Coletar depoimentos espontâneos de UX das novas cadastradas ativas no app</span></li>
            <li class="ci"><div class="ci-box"></div><span class="ci-text">Otimizar os fluxos da página free p/ premium convertendo base já instalada</span></li>
          </ul>
        </div>
      </div>
    """)

# --- 4. Section 4: Timeline ---
html = html.replace(
    'Dias 1–14 · Semanas 1–2',
    'Dias 1–7'
)
html = html.replace(
    'Montar landing page com CTA "Garantir acesso antecipado". Definir narrativa central. Produzir vídeo demo de 30–60s. Criar kit do embaixador completo. Definir estrutura de comissão e rastreamento. Configurar CRM de prospecção.',
    'Construção oculta do terreno: fechar narrativas e benefícios. Landing page de atração com foco no registro simplificado com IA. Kit Embaixador e tracking prontas.'
)

html = html.replace(
    '<div class="tl-it"><div class="tl-dot f"></div><div class="tl-per">Dias 15–35 · Semanas 3–5</div><div class="tl-nm">Recrutamento de embaixadores</div><div class="tl-desc">Prospectar 150–300 perfis qualificados. Executar método 3 passos. Meta: 10 abordagens por dia, 10 fechamentos por semana. Onboarding e acesso antecipado ao app. Compartilhar kit completo.</div></div>',
    '<div class="tl-it"><div class="tl-dot f"></div><div class="tl-per">Dias 8–20</div><div class="tl-nm">Recrutamento de Parceiras</div><div class="tl-desc">Pesquisa dura dos targets (300 contatos). Rotina de 10 conversas diárias. Fechamento do ecossistema de comissionadas entregando códigos, acessos VIPs de onboarding e diretrizes da Data Zero.</div></div>'
)

html = html.replace(
    '<div class="tl-it"><div class="tl-dot f"></div><div class="tl-per">Dias 30–50 · Semanas 5–7</div><div class="tl-nm">Conteúdo de pré-lançamento</div><div class="tl-desc">Embaixadores publicam sequência: Post 1 (teste) → Post 2 (experiência) → Post 3 (antecipação de acesso). Perfil oficial: bastidores e demos. Lista de espera em crescimento ativo.</div></div>',
    '<div class="tl-it"><div class="tl-dot f"></div><div class="tl-per">Dias 21–27</div><div class="tl-nm">Aquecimento Orgânico</div><div class="tl-desc">Primeiras opiniões (Primeiras Impressões reais). Creators ativam publicações sobre estarem utilizando a solução nas próprias dietas. Antecipação leve do link ao público VIP.</div></div>'
)

html = html.replace(
    '<div class="tl-it"><div class="tl-dot f"></div><div class="tl-per">Dias 50–57 · Semana 8</div><div class="tl-nm">Impulso de Lançamento</div><div class="tl-desc">Todos os embaixadores postam na janela de 3–5 dias. Sequência: teaser (-5) → anúncio (-3) → contagem regressiva (-1) → lançamento (0) → prova social (+1) → resultados (+3). Preço de fundador e referral ativos.</div></div>',
    '<div class="tl-it"><div class="tl-dot f"></div><div class="tl-per">Dias 28–30</div><div class="tl-nm">Janela de Lançamento em Massa</div><div class="tl-desc">A onda avassaladora de pico coletivo na comunicação de influenciadoras. Campanhas centralizadas de indicação onde todas publicam coordenadamente seus reviews garantindo as 500 aquisições validadas imediatas.</div></div>'
)

html = html.replace(
    '<div class="tl-it"><div class="tl-dot"></div><div class="tl-per">Dia 58+ · Contínuo</div>',
    '<div class="tl-it"><div class="tl-dot"></div><div class="tl-per">Dia 31+ · Contínuo</div>'
)

html = html.replace(
    '<div><div style="font-family:var(--display);font-weight:800;font-size:36px;color:var(--ink);letter-spacing:-.03em">500–3k</div><div style="font-size:14.4px;color:var(--ink70)">Usuários ativos iniciais</div></div>',
    '<div><div style="font-family:var(--display);font-weight:800;font-size:36px;color:var(--ink);letter-spacing:-.03em">300–500</div><div style="font-size:14.4px;color:var(--ink70)">Usuárias base da ativação</div></div>'
)

html = html.replace(
    '<div><div style="font-family:var(--display);font-weight:800;font-size:36px;color:var(--ink);letter-spacing:-.03em">200k–500k</div><div style="font-size:14.4px;color:var(--ink70)">Impressões no lançamento</div></div>',
    '<div><div style="font-family:var(--display);font-weight:800;font-size:36px;color:var(--ink);letter-spacing:-.03em">20–40</div><div style="font-size:14.4px;color:var(--ink70)">Feedbacks / Parcerias ativas validando alcance</div></div>'
)

# --- 5. Tabela Mestra ---
old_table = re.search(r'<tbody>\s*<tr class="tr-week".*?</tr>\s*</tbody>', html, re.DOTALL).group(0)

new_table = """<tbody>
        <tr class="tr-week" data-sec="s4" onclick="toggleWeek(this)"><td><div class="week-cb"></div></td><td><strong>Sem</strong> D1–7</td><td><span class="pill p-dk" style="font-size:12px">Fase 1</span></td><td>Narrativa, scripts e vídeos listos</td><td>Montar lista 300 contatos/CRM e códigos de ativação</td><td>Página Oficial On</td><td>Setup inicial impecável</td></tr>
        <tr class="tr-week" data-sec="s4" onclick="toggleWeek(this)"><td><div class="week-cb"></div></td><td><strong>Sem</strong> D8–14</td><td><span class="pill p-b" style="font-size:12px">Fase 2</span></td><td>Suporte do App e Refinamento VIP</td><td>Prospecção agressiva 10/day, onboarding iniciais</td><td>Zero apelos. Creators testando a ferramenta caladas</td><td>Fechamentos Iniciais</td></tr>
        <tr class="tr-week" data-sec="s4" onclick="toggleWeek(this)"><td><div class="week-cb"></div></td><td><strong>Sem</strong> D15–20</td><td><span class="pill p-b" style="font-size:12px">Fase 2</span></td><td>Avaliação do Onboarding</td><td>Meta final atigida: 10-20 Creators. Briefing do Pico 30</td><td>Primeiros sinais curiosos: "testando algo novo..."</td><td>10-20 Embaixadoras Ativas</td></tr>
        <tr class="tr-week" data-sec="s4" onclick="toggleWeek(this)"><td><div class="week-cb"></div></td><td><strong>Sem</strong> D21–27</td><td><span class="pill p-o" style="font-size:12px">Fase 3</span></td><td>Serviços de Referral Prontos</td><td>Alinhamento da Janela de Massa com todo o esquadrão</td><td>Primeiras impressões fortes. Demos do uso próprio</td><td>Maturidade do Funil</td></tr>
        <tr class="tr-week tr-launch" data-sec="s4" onclick="toggleWeek(this)"><td><div class="week-cb"></div></td><td><strong>Sem</strong> D28–30</td><td><span class="pill p-g" style="font-size:12px;background:var(--g500);color:white">LANÇAMENTO!</span></td><td>Respostas ativas, estabilidade, bônus</td><td>Publicações de TODAS na mesma janela temporal</td><td>Stories, reviews pesados, incentivos, urgência real cruzada</td><td><strong>300 a 500 usuárias ativas</strong></td></tr>
        <tr class="tr-week" data-sec="s4" onclick="toggleWeek(this)"><td><div class="week-cb"></div></td><td><strong>S+</strong> D31+</td><td><span class="pill p-p" style="font-size:12px">Momentum</span></td><td>Acompanhamento baseadas em retenções D7/D30</td><td>Otimização nas Top parceiras (Premiar TOP 3 lideres)</td><td>Reviews estendidos, reposts contínuos e UGC</td><td>Scale/Growth da base</td></tr>
      </tbody>"""

html = html.replace(old_table, new_table)

with open("index.html", "w") as f:
    f.write(html)
print("Changes applied locally")

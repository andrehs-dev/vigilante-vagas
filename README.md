# Vigilante Vagas

Robô que monitora sites de concurso público e notifica quando aparece uma vaga nova com os requisitos desejados.

## Objetivos

Economizar tempo de concurseiros que precisam checar múltpilos sites manualmente todos os dias.

## Como Funciona

1. Varre sites de concurso em busca de vagas
2. Filtra pelos termos/configurações do usuário
3. Notifica via Telegram/WhatsApp quando encontra uma nova vaga.
4. Evita repetir notificaçẽos da mesma vaga

## Stack

- Python 3 + requests + BeautifulSoup
- JSON para armazanamento local
- (futuro) SQLite paramúltiplos assinantes

## Instalações
''' bash
git clone <url-do-repo>
cd vigilante-vagas
pip install requests
beautifulsooup4

## RoadMap
[x] Estrutura inicial do projeto
[ ] Varredura funcional de 1 site
[ ] Filtro por termo de busca
[ ] Notoficação via Telegram
[ ] Multiplos assinantes com SQLite
[ ] PAinel web para cadastro

## Licença
MIT
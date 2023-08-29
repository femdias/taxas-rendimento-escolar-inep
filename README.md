# Taxas de Rendimento Escolar - INEP (1996-2005 e 2007-2022)

### Introdução

Analisar o rendimento escolar (taxas de aprovação, reprovação e abandono) é fundamental para elaborar e avaliar políticas públicas educacionais. Infelizmente, o INEP apenas disponibiliza os dados de forma agregada por municípios a partir de 2007 (disponíveis [aqui](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar)). Além disso, calcular essas taxas por meio dos microdados do Censo Escolar é muito difícil, pois as variáveis mudam muito de ano a ano (acreditem, eu tentei).

Dado isso, abri uma solicitação através da Lei de Acesso à Informação pedindo a disponibilização das bases de rendimento escolar de 1995 a 2007. A solicitação foi acatada e o Ministério da Educação, que disponibilizou tabelas com as taxas de rendimento de 1996 a 2005 e de 2007. Segundo eles, esse dado não existe para 2006, já que houve uma alteração na metodologia do Censo Escolar.

### Conteúdo do Repositório

Esse repositório contém os dados das taxas de rendimento (aprovação, reporvação e abandono) por município, localização (Rural ou Urbana) e rede (Estadual, Municipal, Federal ou Privada) de 2007 a 2022, que é publicamente disponivel no site do INEP, e de 1996 a 2005, que foi obtido por meio da Lei de Acesso a Informação. Além disso, contém um código em Python que concatena todas essas bases (cada uma tem formatação ligeiramente diferente) e uma planilha de resultado final desse código.  

### Solicitação e resposta

A solicitação foi a seguinte (Nº 23546.070230/2023-79):
"Prezados,

Estou elaborando um estudo acadêmico no qual analiso o rendimento escolar da educação básica em Manaus, comparando com outras cidades brasileiras. Para isso, preciso da taxa de aprovação, reprovação e abandono por município, ano escolar e dependência administrativa, porém, essa informação por município só está disponível publicamente a partir de 2007 (disponíveis em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar). Mesmo utilizando os microdados do Censo Escolar, muitos anos não contém essas variáveis.

Analisar o rendimento escolar é fundamental para a elaboração de políticas escolares e estudos científicos. Dito isto, solicito uma tabela, em que cada aba é um ano (de 1995 até 2007), e em cada linha seja um município e sua respectiva dependência administrativa, informando as taxa de aprovação, reprovação e abandono para cada ano escolar, do primeiro ano do fundamental até o último de ensino médio (como base, vocês podem utilizar o formato das tabelas de taxas de rendimento, disponíveis no link do parágrafo anterior).

Agradeço a atenção."


E a resposta:
" Prezado(a) Senhor(a),
  Em atendimento ao pedido de informação registrado sob o protocolo nº 23546-070230/2023-79, segue resposta elaborada pela unidade responsável:
  Disponibilizamos em repositório de arquivos em nuvem, as Taxas de rendimento (aprovação, reprovação e abandono) por município, referentes ao período de  1996 a 2007. Cabe esclarequer que a divulgação das taxas de rendimento de 1995 foi realizada no Censo da Educação Básica de 1996. 
Além disso, devido às mudanças metodológicas que ocorreram na coleta do Censo Escolar, que foram implementadas em 2007, não foram calculadas as taxas de rendimento para o ano de 2006.  Dessa forma, estão disponíveis os dados referentes aos períodos de 1996 a 2005 e 2007.
Para baixar os arquivos, acesse o seguinte endereço: https://inepgovbr-my.sharepoint.com/:u:/g/personal/dadosabertos_deed_inep_gov_br/EY5XMfR46bpNtrJaLt6jUnUBOvK2QAV_u3_NHgNy0V8UlQ?e=Wh2u4R"

  Caso queira solicitar mais informações, é necessário registrar uma nova demanda no Fala.Br pelo endereço https://falabr.cgu.gov.br para que corram os prazos de atendimento previstos pela Lei de Acesso à Informação.

  Quando for negado o pedido de acesso à informação, o Decreto nº 7.724, de 16 de maio de 2012, estabelece que se resguarda ao interessado a possibilidade de apresentação de recurso, no prazo de 10 (dez) dias.

  Atenciosamente,

Ouvidoria do Inep 
Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira
Edifício Villa Lobos – Sede do Inep, térreo
Setor de Indústrias Gráficas, quadra 04, lote 327
CEP: 70610-908 – Brasília/DF
https://www.gov.br/acessoainformacao/pt-br/falabr"

Agradeço ao Pedro Veloso, do Todos pela Educação, por toda a ajuda nesse processo!

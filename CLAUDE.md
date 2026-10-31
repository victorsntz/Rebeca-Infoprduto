# Infoproduto Rebeca: memória do projeto

Este arquivo é lido sozinho no começo de cada conversa. Ele resume tudo o que já foi feito, pra não precisar explicar de novo.

## Quem é quem

- **Victor**: designer de marcas e dono de agência. É quem conversa aqui. Marido da Rebeca.
- **Rebeca Fortunato**: a autora. Instagram **@rebecafortunato__** (com dois underlines no fim). Conta dela no app: rebrodriguesvieira@gmail.com.

## Como falar com o Victor

- Português simples e natural, como se explicasse pra uma criança. Pode ser técnico, desde que venha com exemplo.
- Sem travessão. Sem cara de IA. Sem fórmula pronta tipo "não é sobre X, é sobre Y".
- Humor rápido, criativo e um pouco provocante quando couber.
- Textos pra colar na Kiwify, no Instagram ou no WhatsApp vão **em texto puro dentro da conversa**, pronto pra copiar e colar. Nada de mandar só o arquivo.
- Mexer pouco no que ele já aprovou. Mudança pequena e certeira.
- Ele se preocupa com custo. Nada de vários agentes pra desenhar uma arte. Arte se faz direto, simples, em HTML/SVG.
- Arte pronta: renderizar o PNG, conferir olhando a imagem, mandar com SendUserFile. Se forem várias, mandar num .zip.

## O produto

- **De Tola a Virtuosa · 40 dias no deserto**: caderno devocional imprimível, mais landing page, mais app de membros.
- Domínio: **detolaavirtuosa.com** (landing na raiz, app em /app, PDFs em /dist).
- Venda na Kiwify por **R$ 47**: https://pay.kiwify.com.br/6IGmfcv
- Presente pra uma amiga (**R$ 27**). Aparece como order bump na compra e também pode ser comprado depois, quantas vezes quiser: https://pay.kiwify.com.br/l2of2hZ
- Sem boleto. Ele foi tirado da Kiwify e do site.
- Suporte: contato@detolaavirtuosa.com
- Versículo âncora: Provérbios 14:1.

## Onde fica cada coisa no repositório

| Pasta | O que é |
|---|---|
| `site/index.html` | Landing page |
| `site/app/` | App de membros: app.js, store.js, config.js, app.css, content.json |
| `site/app/supabase/` | schema.sql e a função `checkout-webhook` |
| `src/` | Gerador do caderno em PDF (build.py, content.py, styles.css) |
| `dist/` | PDFs prontos |
| `kiwify/aula-comece-aqui.html` | HTML da aula "Comece aqui" da área de membros da Kiwify |
| `insta/` | Posts de Instagram (HTML + script de render + PNGs) |
| `insta/DIRECAO-VISUAL.md` | Direção visual tirada das referências do Victor. **Ler antes de qualquer arte.** |
| `insta/referencias/` | Imagens de referência que o Victor mandou |
| `insta/gen/` | Imagens geradas ou recortadas usadas nas artes |
| `insta/fonts/` | Caveat, Dancing Script, Playfair Display (itálico 500 e negrito 700) |

## Publicar o site

- Publicar é **fazer push na `main`**.
- A ação `sync.yml` monta a branch `publicar` com o conteúdo de `site/` e os PDFs. A Hostinger serve essa branch.
- Só `site/` e `dist/*.pdf` vão pro ar. CLAUDE.md, `insta/` e `kiwify/` nunca são publicados.
- O trabalho do dia a dia fica na branch `claude/optimistic-ritchie-fdj2qf`. Quando mexer em `site/`, levar pra `main` pra publicar.

## App de membros e Supabase

- Projeto Supabase `stcskyelzuynfnmdrnth`, plano grátis.
- Tabelas: `members`, `profiles`, `entries`, `prep`, `gifts`. Funções: `claim_gift` e `ping`.
- **Webhook**: a Kiwify manda a compra pra função `checkout-webhook` (dois webhooks, um por produto, os dois com `?token=`).
  - Compra aprovada libera o acesso.
  - Reembolso ou chargeback só desliga o acesso.
  - Compra só do presente não mexe na conta da compradora, apenas cria o código de convite.
  - Reembolso do presente cancela o convite. Se a amiga já tinha resgatado, ela perde o acesso e vê "Seu convite foi cancelado".
- **Supabase dorme** depois de uns dias parado e o app mostra "Sem conexão". Por isso existe a ação `manter-acordado.yml`, que chama `rpc/ping` a cada 2 dias. Se o erro voltar, restaurar o projeto pelo MCP do Supabase.
- **Liberar acesso na mão**: inserir em `members` com `email` em minúsculo, `active=true`, `provider='manual'` e um `provider_ref` que explique o motivo.
  - Já foram liberadas assim as 3 compradoras que compraram enquanto o Supabase dormia (`provider_ref='kiwify-confirmada-manual'`).
  - A conta da Rebeca também (`provider_ref='acesso-autora'`).
- Login é sempre pela própria pessoa: "Criar conta" ou "Esqueci a senha". **Nunca criar nem passar senha pra ninguém.**
- Vídeos das aulas: `site/app/config.js`, campo `VIDEOS`. Basta colar o link do YouTube (não listado). O app converte pro player sozinho.
  - Já tem: `aula_inaugural` e `conhecendo_caderno`.
  - Faltam: `como_imprimir` e `como_usar_site`.
- No app tem o botão "Presenteie uma amiga" na lateral (o presente pulsa de leve) e, no Início, a escolha entre usar pelo celular ou impresso.

## Kiwify

- Área de membros: um módulo **"Comece aqui"** com uma aula, usando o HTML de `kiwify/aula-comece-aqui.html`. O conteúdo vai em texto pra colar.
- As aulas em vídeo ficam só dentro do app, não na Kiwify.

## Instagram

- Posts de 1080x1350. Cada arte tem um `nome.html` e um `nome.js` em `insta/`.
- Pra renderizar: `cd insta && node nome.js`. O script usa Playwright (`require('playwright')`).
- O que já existe:
  - `post-*` (topo de funil)
  - `virtuosa-*` e `lirio-*` (atributos da mulher virtuosa)
  - `mapa-virtuosa-*`, `olhos-em-jesus-*`, `adesivos-*`, `medo-paz-*`, `aquarela-*`, `timoteo-*`, `amor-*`, `pavao-*`, `misericordia-*`, `onca-*` e `onca-foto-*`
  - `achadinhos-base-*` (bases da Shopee)
- O que o Victor já ensinou nos ajustes:
  - Pouca coisa na arte. Quando lota, ele reclama.
  - Nada infantil. Nada de vetor chapado nem clipart. Aquarela tem que parecer aquarela de verdade.
  - Variar as artes de uma série (cor, com ou sem detalhe). Não fazer todas iguais.
  - Só o @rebecafortunato__ como assinatura, sem o nome do produto.
  - Topo de funil não vende o caderno.
  - O @ costuma ir em cima.
  - Fonte que ele gosta: Playfair Display. A serif da marca é a Caslon.
- Gerar imagem: o conector Figma (`generate_image`) funcionou antes, mas estava desconectado na última vez. Quem reconecta é o Victor, nas configurações de conectores do claude.ai.
- O terminal não baixa nada de figma.com nem de supabase.co. Pra baixar uma imagem, rodar a ação `baixar-imagem.yml` (campos `urls`, `nomes` e `pasta`) e depois dar `git pull`.

## Achadinhos da Shopee (em andamento)

- Ideia: colagem de produtos fofos de decoração de Natal com links de afiliada, no estilo "Achadinhos de Natal que eu compraria pra minha casa na Shopee".
- Bases prontas em `insta/achadinhos-base-1..3.png`: rosê, bordô e sálvia. Fundo de tecido listrado com bordado, fonte Playfair Display e 9 espaços tracejados pros produtos.
- A Rebeca se cadastrou no programa de afiliados e está esperando aprovação. Ela recebe pelo ShopeePay, e por isso o cadastro não pede conta bancária.
- Próximo passo: o Victor manda os prints e os links. Aí é recortar os produtos, montar na base escolhida e escrever a DM com os links numerados. Uma página `/achadinhos` no site também é opção.

## Pendências

1. Links dos vídeos `como_imprimir` e `como_usar_site`.
2. Achadinhos: escolher a cor da base e esperar os links da Shopee.
3. Confirmar se alguma das 3 compradoras recuperadas comprou o presente. Se comprou, criar o código em `gifts` na mão.
4. Nome do produto: o Victor acha que "tola" pode estar pesado e vai testar com enquete nos stories. Se trocarem o nome, muda site, app, caderno e Kiwify. Isso só acontece se ele decidir.

## Cuidados

- Nunca repetir CPF, telefone ou senha que apareçam em print ou mensagem.
- Antes de push, dar `git pull --rebase`, porque as ações do GitHub também fazem commit na branch.

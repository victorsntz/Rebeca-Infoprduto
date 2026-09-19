# De Tola a Virtuosa · 40 dias no deserto

Infoproduto da Rebeca Fortunato pra mulheres: um caderno prático de corpo, alma e espírito em quatro provas de dez dias. Este repositório tem as três peças do produto, com a mesma identidade e o mesmo conteúdo:

| Peça | Onde | O que é |
|---|---|---|
| Caderno (PDF) | `dist/de-tola-a-virtuosa.pdf` | 72 páginas em A5 deitado, só frente, pra imprimir e encadernar |
| Landing page | `site/index.html` | Página de vendas que a cliente abre antes do checkout |
| Área de membros | `site/app/` | Versão online do caderno, com login, dia a dia e progresso salvo |

O texto inteiro vive em um lugar só: `src/content.py`. O build gera o HTML do caderno e o `content.json` que o app lê. Mudou uma frase, um desafio ou um versículo, roda o build e as duas versões ficam iguais.

## Como validar

**Caderno.** Abra o PDF. Pra ver rápido no navegador, `dist/de-tola-a-virtuosa.html`.

**Landing page e app.** Precisa de um servidor local porque o app carrega o `content.json`:

```bash
npx http-server site -p 8765
# landing: http://localhost:8765/
# app:     http://localhost:8765/app/
```

O app sem servidor configurado roda em **modo demonstração**: cria qualquer e-mail e senha, escolhe a data do dia 1 e tudo fica salvo no navegador. Pra testar o meio da travessia, coloque o dia 1 alguns dias no passado.

## Como gerar o PDF de novo

```bash
./build.sh
```

Precisa de `python3` e de um Chromium ou Chrome (`CHROME=/caminho/do/chrome ./build.sh` se não estiver no PATH). Sai o HTML, o PDF e o `site/app/content.json`.

## Como ligar o app de verdade (Supabase)

1. Crie um projeto em supabase.com e rode `site/app/supabase/schema.sql` no SQL Editor.
2. Em Authentication, deixe e-mail e senha ativos.
3. Cole a URL e a chave `anon` em `site/app/config.js`.
4. Pra liberar o acesso de quem comprou, faça deploy da função `site/app/supabase/functions/checkout-webhook` e aponte o webhook da plataforma de pagamento pra ela. Compra aprovada ativa, reembolso ou cancelamento bloqueia. Pra testar sem checkout, insira o e-mail na tabela `members` na mão (tem o exemplo no fim do `schema.sql`).
5. Cole os links dos vídeos (aula inaugural, como imprimir, como usar o site) e o link do checkout no mesmo `config.js`.

Na landing, troque o preço de exemplo e coloque a URL do checkout em `CHECKOUT_URL`, no fim do `site/index.html`.

## Hospedar

É tudo estático. Sobe a pasta `site/` em qualquer lugar (Vercel, Netlify, Hostinger, GitHub Pages) e o PDF junto. O caminho do PDF dentro do app está em `config.js`.

## Estrutura

```
src/content.py           todo o texto do caderno (provas, desafios, leituras, páginas)
src/build.py             monta o HTML do caderno e exporta o content.json
src/styles.css           estilo de impressão do caderno (A5 paisagem)
fonts/                   Libre Caslon Display e Text (licença OFL)
dist/                    HTML e PDF gerados
site/index.html          landing page
site/assets/brand.css    identidade compartilhada (cores, fontes, botões, chips)
site/assets/img/         mockups tirados do próprio PDF
site/app/                área de membros (index, app.js, app.css, store.js, config.js)
site/app/supabase/       schema.sql e a função do webhook do checkout
arquivo/100-dias/        a primeira versão, de 100 dias, guardada pra referência
build.sh                 gera tudo
```

## Identidade

| Uso | Cor |
|---|---|
| Rubi (espírito, marca, prova 3) | `#8E2A3A` |
| Dourado (mente, prova 2) | `#B8975B` |
| Sálvia (corpo, prova 1) | `#7A8C74` |
| Ameixa (prova 4) | `#4B2C3C` |
| Creme (fundo) | `#F9F5EE` |

Títulos em Libre Caslon (Display nos grandes, Text nos demais), texto corrido em Times New Roman. O ícone é um coração em chamas, em vetor, nas cores rubi e dourado.

## Pendências pra Rebeca

- Conferir cada citação bíblica com a versão que ela usa.
- Foto e bio dela na landing (tem um texto de exemplo no lugar).
- Frase da contracapa do caderno (tem uma sugestão).
- Gravar a aula inaugural e os dois vídeos curtos.
- Preço, parcelamento e link do checkout.

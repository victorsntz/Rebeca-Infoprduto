# De Tola a Virtuosa · 100 dias

Caderno prático pra imprimir (A4, retrato), feito pra mulheres que querem sair do modo "tola" e virar a mulher virtuosa de Provérbios 31. Corpo, alma e espírito, todo dia, por 100 dias.

## O que tem dentro

- **Abertura (17 páginas):** carta de boas-vindas, como usar, tola x virtuosa, identidade, corpo/alma/espírito, glossário de virtudes, feminilidade, autoconhecimento, propósito, limites e princípios, regras inegociáveis, quadro dos sonhos, carta pro futuro, retrato do dia 1 e mapa dos 100 dias.
- **4 fases:** Fundamento (1 a 30), Construção (31 a 60), Consolidação (61 a 90), Fechamento (91 a 100). Cada fase abre com um versículo, um compromisso assinado e um tracker de hábitos.
- **10 blocos de 10 dias**, um por virtude: temperança, fé, prudência, fortaleza, paciência, bondade, fidelidade, humildade, alegria e paz, amor e esperança. Cada bloco tem abertura (definição, versículo, tola x virtuosa, metas de corpo, mente e espírito) e revisão.
- **100 páginas diárias:** leitura bíblica, desafio prático, checklist de corpo, mente e espírito, virtude em ação, gratidão, maior dificuldade do dia, uma linha pra Deus, amanhã eu vou.
- **Fechamento:** retrato do dia 100 lado a lado com o dia 1, "E agora?", notas livres, contracapa.

Total: 149 páginas.

## Estrutura do projeto

```
src/content.py   todo o texto (blocos, desafios, leituras, páginas)
src/build.py     monta o HTML a partir do conteúdo
src/styles.css   estilo de impressão (A4, cores, fontes)
fonts/           Cormorant Garamond e Jost (licença OFL)
dist/            HTML e PDF gerados
build.sh         gera tudo
```

## Como gerar o PDF

```bash
./build.sh
```

Precisa de `python3` e de um Chromium ou Chrome (`CHROME=/caminho/do/chrome ./build.sh` se não estiver no PATH).

## Como editar

Texto: `src/content.py`. Visual: `src/styles.css`. Estrutura das páginas: `src/build.py`. Rode o build de novo e o PDF sai atualizado.

## Paleta

| Uso | Cor |
|---|---|
| Rubi (espírito, marca) | `#8E2A3A` |
| Dourado (mente, fase 2) | `#B8975B` |
| Sálvia (corpo, fase 1) | `#7A8C74` |
| Ameixa (fase 4) | `#4B2C3C` |
| Creme (fundo) | `#F9F5EE` |

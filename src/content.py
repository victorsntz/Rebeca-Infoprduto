# -*- coding: utf-8 -*-
"""
Conteúdo do caderno "De Tola a Virtuosa: 40 dias no deserto".
Tudo que é texto vive aqui. O build.py só monta as páginas.
"""

TITULO = "De Tola a Virtuosa"
SUBTITULO = "40 dias no deserto"
TAGLINE = "Um caderno prático de corpo, alma e espírito"
AUTORA = "Rebeca Fortunato"
FOOT = "De Tola a Virtuosa · Rebeca Fortunato"

VERSICULO_CAPA = {
    "texto": "Mulher virtuosa, quem a achará? O seu valor muito excede o de rubis.",
    "ref": "Provérbios 31:10",
}

CONTRACAPA = {
    "frase": "Feito por uma mulher que também está saindo de tola pra virtuosa, pra mulheres que decidiram fazer o mesmo.",
    "versiculo": "Dai-lhe do fruto das suas mãos, e louvem-na nas portas as suas obras.",
    "ref": "Provérbios 31:31",
}

# ---------------------------------------------------------------------------
# As 4 provas de 10 dias (a jornada do deserto)
# ---------------------------------------------------------------------------
BLOCOS = [
    {
        "num": 1, "inicio": 1, "fim": 10, "cor": "salvia",
        "lugar": "Saída",
        "chamada": "Largar o Egito",
        "virtude": "Temperança",
        "sub": "Domínio próprio",
        "mulher": "Rute",
        "mulher_desc": "Deixou Moabe, a terra que conhecia, pra seguir Deus sem garantia nenhuma. \"Aonde quer que tu fores, irei eu.\"",
        "mulher_ref": "Rute 1:16",
        "resumo": "Ninguém chega no deserto sem antes sair de algum lugar. Nestes dez dias você larga o Egito: os hábitos que te escravizam sem você perceber. Celular na cama, comida por ansiedade, sono jogado fora, boca sem freio. Temperança é pegar as rédeas de volta.",
        "definicao": "Temperança é comer o que basta, falar o que basta e parar quando precisa. A mulher sem domínio próprio é como cidade sem muro: qualquer coisa entra.",
        "versiculo": "Como cidade derribada, sem muro, assim é o homem que não pode conter o seu espírito.",
        "ref": "Provérbios 25:28",
        "versiculo_lugar": "Dize aos filhos de Israel que marchem.",
        "ref_lugar": "Êxodo 14:15",
        "tola": "espera ter vontade pra começar.",
        "virtuosa": "começa, e a vontade vem depois. Ou não vem, e ela faz mesmo assim.",
        "metas": {
            "corpo": "2 litros de água por dia. Uma fruta antes de qualquer doce.",
            "mente": "Celular fora do quarto. Primeira hora do dia sem tela.",
            "espirito": "10 minutos de Palavra e oração no mesmo horário, todo dia.",
        },
    },
    {
        "num": 2, "inicio": 11, "fim": 20, "cor": "dourado",
        "lugar": "Sinai",
        "chamada": "Ouvir quem você é",
        "virtude": "Fé",
        "sub": "Identidade",
        "mulher": "Maria",
        "mulher_desc": "Ouviu o impossível e respondeu: \"eis aqui a serva do Senhor\". Depois guardou tudo no coração.",
        "mulher_ref": "Lucas 1:38",
        "resumo": "No Sinai, Deus não deu regras primeiro. Ele disse quem Ele era e quem o povo era: \"vos trouxe a mim\". Nestes dez dias você para de se definir pelo que sente de manhã e passa a se definir pelo que Deus falou. Filha. Escolhida. Menina dos olhos dele.",
        "definicao": "Fé é confiar no que Deus disse antes de ver acontecer. Quem acredita no que Ele diz sobre ela age diferente sem precisar se forçar.",
        "versiculo": "Ora, a fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem.",
        "ref": "Hebreus 11:1",
        "versiculo_lugar": "Vós tendes visto como vos levei sobre asas de águias e vos trouxe a mim.",
        "ref_lugar": "Êxodo 19:4",
        "tola": "se define pelo que sentiu hoje de manhã.",
        "virtuosa": "se define pelo que Deus falou, e o que ela sente vai atrás.",
        "metas": {
            "corpo": "Manter a prova 1 e caminhar 20 minutos, 3 vezes na semana.",
            "mente": "Versículos de identidade colados no espelho, lidos em voz alta ao acordar.",
            "espirito": "Orar em voz alta uma vez por dia. Memorizar 2 versículos.",
        },
    },
    {
        "num": 3, "inicio": 21, "fim": 30, "cor": "rubi",
        "lugar": "Deserto",
        "chamada": "Continuar quando cansa",
        "virtude": "Fidelidade",
        "sub": "Paciência e constância",
        "mulher": "Ana",
        "mulher_desc": "Anos de espera, provocação e silêncio. Ela continuou orando até Deus responder. E quando respondeu, ela cumpriu o que prometeu.",
        "mulher_ref": "1 Samuel 1",
        "resumo": "Aqui separa quem fez uma dieta de quem mudou de vida. O povo murmurou no deserto porque cansou de repetir. O segredo desta prova é chato de propósito: fazer no dia 25 com a mesma seriedade do dia 5. Deus usou 40 anos de deserto pra humilhar e provar. Você tem dez dias.",
        "definicao": "Fidelidade é fazer no escuro o que você prometeu na luz. Paciência é esperar sem azedar. Quem é fiel no pouco recebe o muito.",
        "versiculo": "Quem é fiel no pouco, também é fiel no muito.",
        "ref": "Lucas 16:10",
        "versiculo_lugar": "Te lembrarás de todo o caminho pelo qual o Senhor teu Deus te guiou no deserto estes quarenta anos, para te humilhar, para te provar.",
        "ref_lugar": "Deuteronômio 8:2",
        "tola": "promete grande e entrega quando lembra.",
        "virtuosa": "promete pequeno e entrega sempre.",
        "metas": {
            "corpo": "Repetir o treino do dia 5 e anotar a diferença.",
            "mente": "Cumprir a rotina completa nos 10 dias, com ou sem vontade. Zero fofoca.",
            "espirito": "Ler a Bíblia no mesmo horário todos os dias. Sem exceção.",
        },
    },
    {
        "num": 4, "inicio": 31, "fim": 40, "cor": "ameixa",
        "lugar": "Jordão",
        "chamada": "Entrar na promessa",
        "virtude": "Coragem",
        "sub": "Propósito",
        "mulher": "Ester",
        "mulher_desc": "Entrou na sala do rei tremendo, sabendo que podia morrer. Entrou mesmo assim. \"Para tal tempo como este.\"",
        "mulher_ref": "Ester 4:14",
        "resumo": "O Jordão é a última margem antes da promessa. E promessa exige coragem: a conversa adiada, o projeto parado, o propósito que você sabe qual é e vem fingindo que não. Nestes dez dias você atravessa, fecha a carta e decide o que vem depois.",
        "definicao": "Coragem não é ausência de medo. É fazer com medo. E propósito é o que dá direção pro medo: você atravessa porque sabe pra onde vai.",
        "versiculo": "Não te mandei eu? Esforça-te, e tem bom ânimo; não temas, nem te espantes; porque o Senhor teu Deus é contigo, por onde quer que andares.",
        "ref": "Josué 1:9",
        "versiculo_lugar": "Santificai-vos, porque amanhã fará o Senhor maravilhas no meio de vós.",
        "ref_lugar": "Josué 3:5",
        "tola": "evita a conversa, o treino e a decisão porque dói.",
        "virtuosa": "sente a mesma dor e vai mesmo assim.",
        "metas": {
            "corpo": "Aumentar o treino: mais peso, mais tempo ou mais um dia na semana.",
            "mente": "Ter a conversa que está sendo evitada. Terminar um projeto parado.",
            "espirito": "Escrever o propósito em uma frase e contar pra alguém.",
        },
    },
]

# ---------------------------------------------------------------------------
# Desafios diários (40)
# ---------------------------------------------------------------------------
DESAFIOS = [
    # Prova 1: Saída · Temperança
    "Um copo de água ao acordar, antes do café. Depois, 3 copos de manhã, 3 à tarde e 1 à noite. São 2 litros, contados.",
    "Deixe o celular fora do quarto esta noite. Compre um despertador de verdade se precisar.",
    "Arrume o canto da casa que te incomoda há semanas. Só um: uma gaveta, a pia, a mesa. Dez minutos.",
    "Caminhe 20 minutos hoje. Sem fone. Só você e o que passa na sua cabeça.",
    "Coma uma fruta antes de qualquer doce hoje. Se ainda quiser o doce depois, pode.",
    "Saia de casa hoje sem obrigação nenhuma: um café, uma praça, uma livraria. Sozinha ou com uma amiga. Sem pressa e sem foto.",
    "Diga não a uma coisa hoje. Pequena. Só pra lembrar que você consegue.",
    "Passe o dia inteiro sem reclamar em voz alta. Se escapar, recomece a contagem.",
    "Faça a lista de compras da semana antes de ir ao mercado. Vá sem fome e compre só o que está na lista.",
    "Separe uma sacola com o que você não usa há um ano: roupa, sapato, bolsa. Doe esta semana.",
    # Prova 2: Sinai · Fé
    "Escreva três versículos sobre quem você é e cole no espelho do banheiro.",
    "Ore em voz alta hoje, mesmo que só por dois minutos. Ouvir a própria voz falando com Deus muda alguma coisa.",
    "Se arrume pro seu dia, mesmo sem compromisso: cabelo feito, uma maquiagem, perfume, um salto confortável.",
    "Jejue de redes sociais por 24 horas. Use o tempo que sobrar na Palavra.",
    "Mande uma mensagem de encorajamento pra três mulheres hoje: um versículo e uma frase sua. Sem esperar resposta.",
    "Peça perdão a Deus por algo que você vem escondendo. Depois deixe lá.",
    "Faça uma lista de dez orações que Deus já respondeu na sua vida.",
    "Acorde 30 minutos mais cedo e use esse tempo com Deus antes de qualquer tela.",
    "Memorize um versículo hoje. Repita até conseguir dizer sem olhar.",
    "Faça 15 minutos de silêncio. Sem música, sem tela, sem falar. Só Deus e você.",
    # Prova 3: Deserto · Fidelidade
    "Repita hoje o hábito mais difícil dos últimos 20 dias. Sem negociar.",
    "Cumpra o que você prometeu a alguém e ainda não fez.",
    "Abra uma planilha grátis ou o bloco de notas e escreva: o que entra no mês, as contas fixas, o que sobra. Escolha um gasto pra cortar e um valor pra guardar.",
    "Antes de responder qualquer coisa que te irritar hoje, conte até dez e respire.",
    "Deixe a casa aconchegante hoje: cama limpa, uma vela, uma flor, música baixa. Casa com amor se sente na porta.",
    "Faça uma comida especial pra alguém e sirva na mesa posta, sem celular. Só conversa. Pode ser um bolo.",
    "Faça uma coisa por quem divide a casa com você, sem que ninguém peça. Se for casada, especialmente pelo seu marido. Se tem filhos, por eles também.",
    "Ligue pra sua mãe, sua avó ou alguém que te criou. Só pra ouvir.",
    "Perdoe uma pessoa por escrito. Não precisa enviar. Precisa soltar.",
    "Pergunte a três pessoas próximas: 'em que eu preciso melhorar?'. Só ouça e anote.",
    # Prova 4: Jordão · Coragem
    "Tenha a conversa que você vem evitando. Com mansidão e firmeza.",
    "Reserve uma hora só pra você hoje: faça as unhas, lave o cabelo com calma, hidrate a pele. Sem culpa e sem celular.",
    "Escreva um medo que te trava e o que a Bíblia diz sobre ele.",
    "Dia de obrigações: resolva hoje as três pendências que você vem empurrando. A conta, o e-mail, a consulta que precisa marcar.",
    "Compre, ou separe do armário, a peça-chave que falta no seu visual: uma camisa boa, um sapato, um batom. Use hoje.",
    "Diga 'eu te amo' pra três pessoas hoje, olhando nos olhos.",
    "Escreva seu propósito em uma frase e leia em voz alta pra alguém.",
    "Perdoe a si mesma pelos dias em que falhou. Deus já perdoou.",
    "Faça o retrato do dia 40. Compare com o dia 1 com honestidade.",
    "Abra a carta que você escreveu antes do dia 1. Leia em voz alta. Agradeça.",
]

# ---------------------------------------------------------------------------
# Plano de leitura (40)
# ---------------------------------------------------------------------------
LEITURAS_TEMA = [
    # Prova 1: Saída · Temperança
    "O dia em que o povo saiu do Egito", "A mulher sem domínio próprio é cidade sem muro", "Corpo como sacrifício vivo, mente renovada",
    "Disciplina de quem corre pra ganhar", "O retrato da mulher virtuosa", "Casa construída sobre a rocha",
    "Seu corpo é templo", "A árvore plantada junto ao rio", "Fruto do Espírito contra as obras da carne", "Rute deixa Moabe",
    # Prova 2: Sinai · Fé e identidade
    "Deus diz quem o povo é antes das regras", "Formada de modo assombroso", "Escolhida antes da fundação do mundo",
    "Feitura dele, criada pra boas obras", "Pedra viva, geração eleita", "A galeria dos que creram",
    "Maria ouve o impossível e diz sim", "Nada nos separa do amor de Deus", "Ele conhece a nossa estrutura", "Fé provada gera paciência",
    # Prova 3: Deserto · Fidelidade
    "Por que Deus leva ao deserto", "O povo murmura e cansa de repetir", "Ana ora anos sem resposta",
    "O cântico de Ana quando a resposta veio", "Fiel no pouco, fiel no muito", "Quem governa o próprio espírito",
    "Correr com paciência a carreira", "Não cansar de fazer o bem", "A língua é fogo", "Sede de Deus em terra seca",
    # Prova 4: Jordão · Coragem e propósito
    "Sê forte e corajosa", "Atravessando o Jordão", "Ester decide entrar", "Ester entra e é ouvida",
    "Planos de paz, futuro e esperança", "Prosseguir para o alvo", "O que olho nenhum viu",
    "Sem amor, nada disso vale", "Quem começou a obra vai completar", "Ele faz novas todas as coisas",
]

LEITURAS = [
    # Saída
    "Êxodo 14:10-31", "Provérbios 25", "Romanos 12", "1 Coríntios 9:24-27", "Provérbios 31",
    "Mateus 7:24-29", "1 Coríntios 6:12-20", "Salmo 1", "Gálatas 5:16-26", "Rute 1",
    # Sinai
    "Êxodo 19:1-8", "Salmo 139", "Efésios 1", "Efésios 2", "1 Pedro 2:1-12",
    "Hebreus 11", "Lucas 1:26-56", "Romanos 8", "Salmo 103", "Tiago 1",
    # Deserto
    "Deuteronômio 8", "Números 11:1-15", "1 Samuel 1", "1 Samuel 2:1-11", "Lucas 16:1-13",
    "Provérbios 16", "Hebreus 12", "Gálatas 6", "Tiago 3", "Salmo 63",
    # Jordão
    "Josué 1", "Josué 3", "Ester 4", "Ester 5", "Jeremias 29:1-14",
    "Filipenses 3", "1 Coríntios 2", "1 Coríntios 13", "Filipenses 1", "Apocalipse 21:1-7",
]

assert len(DESAFIOS) == 40, len(DESAFIOS)
assert len(LEITURAS) == 40, len(LEITURAS)

# ---------------------------------------------------------------------------
# Página do dia: opções de marcar
# ---------------------------------------------------------------------------
CHECKLIST = {
    "corpo": ["2 litros de água", "Movi o corpo", "Comi de verdade", "Dormi 7h ou mais"],
    "mente": ["Li 10 minutos", "Sem tela na 1ª hora", "Freei um pensamento"],
    "espirito": ["Orei", "Li a Palavra", "Obedeci em uma coisa"],
}
SENTI = ["Grata", "Em paz", "Cansada", "Ansiosa", "Irritada", "Triste"]
PESOU = ["Tela", "Língua", "Comparação", "Preguiça", "Comida", "Ansiedade", "Briga", "Cansaço", "Dinheiro", "Nada"]
VIRTUDE_OPCOES = ["Apareceu", "Em parte", "Faltou"]

# ---------------------------------------------------------------------------
# Páginas de abertura
# ---------------------------------------------------------------------------
CARTA = {
    "titulo": "Antes de começar",
    "paragrafos": [
        "A tola e a virtuosa moram na mesma mulher. Têm as mesmas mãos, a mesma casa, o mesmo dia de 24 horas. Uma derruba, a outra edifica. E o que decide qual das duas acorda amanhã é o que você faz hoje. Ninguém nasce virtuosa. A gente escolhe, um dia de cada vez. Se você está com este caderno na mão, já começou a escolher. E eu não escrevi isto já sendo virtuosa: enquanto você faz o desafio, eu estou fazendo do lado de cá. Bem-vinda.",
        "Isto não é um livro pra ler. É um caderno pra usar. Todo dia, por 40 dias, você vai marcar, riscar, errar e continuar. Ele vai ficar amassado, com marca de café e letra feia. Ótimo. Caderno limpo é caderno que ninguém usou.",
        "Por que 40? Porque na Bíblia o deserto dura 40. Jesus, Moisés, Elias, o dilúvio, Nínive. Deserto não é castigo. É o lugar onde Deus fala, forma e prepara pra promessa. E Daniel pediu uma prova de 10 dias pra mostrar o que Deus faz com quem obedece. Aqui são quatro provas de 10 dias. Uma travessia inteira.",
        "A ideia é simples: somos espírito, alma e corpo, e tudo anda junto. Dormir mal vira irritação. Irritação vira palavra dura. Palavra dura vira distância de quem você ama e de Deus. Por isso você vai cuidar dos três ao mesmo tempo: beber água e orar, treinar e perdoar, organizar a casa e renovar a mente. O Evangelho se vive na pia da cozinha.",
        "\"Tola\" aqui não é xingamento. É diagnóstico. A tola de Provérbios não é burra. É distraída de si mesma, do que fala, do que come, de quem deixa entrar. Todas nós começamos tolas em alguma área. A diferença é quem decide sair.",
        "Não existe 40 dias perfeitos. Existe 40 dias vividos. Perdeu um dia? Marque \"pulei\" e vire a página. Se der, faça o desafio junto com o do dia seguinte. Se não der, siga. Deus não está contando suas falhas. Está esperando você na próxima.",
    ],
    "assinatura": "Vamos. Do dia 1 ao dia 40.",
}

COMO_USAR = {
    "titulo": "Como usar",
    "regras": [
        ("Preencha as primeiras páginas antes do dia 1.", "Identidade, propósito, limites, regras, quadro dos sonhos, carta e retrato. Uma tarde."),
        ("Leia a abertura da prova antes dos 10 dias.", "Ela diz qual virtude você vai treinar e quais metas cumprir."),
        ("Uma página por dia. Um minuto pra marcar.", "Escrever é bônus pros dias com fôlego."),
        ("A maior dificuldade é a pergunta mais importante.", "Ela mostra onde Deus está trabalhando em você."),
        ("A cada 10 dias, revisão.", "Quinze minutos. Compare, ajuste, agradeça."),
        ("Perdeu um dia? Marque \"pulei\" e siga.", "Se der, faça dois desafios no dia seguinte. Se não der, tudo bem. Não desista, não recomece do zero."),
    ],
    "manha": ["Um copo de água antes de tudo.", "Louvor ou silêncio, sem tela.", "Leitura de hoje, caneta na mão.", "Ler o desafio e decidir quando fazer."],
    "noite": ["Marcar as caixinhas com honestidade.", "Circular como me senti e o que pesou.", "Uma gratidão, uma dificuldade, um amanhã.", "Celular fora do quarto."],
}

TOLA_VIRTUOSA = {
    "titulo": "Tola ou virtuosa?",
    "versiculo": "Toda mulher sábia edifica a sua casa; mas a tola derruba-a com as suas próprias mãos.",
    "ref": "Provérbios 14:1",
    "intro": "Provérbios coloca duas mulheres lado a lado o livro inteiro. Uma edifica, a outra derruba. E o detalhe que assusta: as duas têm as mesmas mãos. A diferença é o que cada uma faz todo dia, quando ninguém está olhando.",
    "contrastes": [
        ("espera ter vontade.", "cria rotina."),
        ("se compara.", "se examina."),
        ("derruba a casa com a boca.", "edifica a casa com as mãos."),
        ("quer tudo em uma semana.", "planta e espera."),
        ("reage.", "responde."),
        ("corre atrás de ser vista.", "é achada."),
        ("culpa.", "assume."),
        ("chora e para.", "chora e continua."),
    ],
    "pergunta": "Em qual linha eu mais me reconheci hoje?",
}

IDENTIDADE = {
    "titulo": "Quem Deus diz que você é",
    "intro": "Tudo neste caderno nasce daqui. Virtude, feminilidade, disciplina, relacionamentos: tudo brota de identidade. Quem sabe quem é age diferente sem precisar se forçar.",
    "versiculos": [
        ("Menina dos olhos dele", "Aquele que tocar em vós toca na menina do seu olho.", "Zacarias 2:8"),
        ("Feita de modo assombroso", "De um modo assombroso e tão maravilhoso fui feito.", "Salmo 139:14"),
        ("Obra dele, com propósito", "Somos feitura sua, criados em Cristo Jesus para as boas obras.", "Efésios 2:10"),
        ("Filha", "Deu-lhes o poder de serem feitos filhos de Deus.", "João 1:12"),
        ("Força e dignidade", "A força e a dignidade são os seus vestidos, e ri-se do dia futuro.", "Provérbios 31:25"),
        ("Nova criatura", "As coisas velhas já passaram; eis que tudo se fez novo.", "2 Coríntios 5:17"),
    ],
    "pergunta1": "Quem eu sou hoje, sem filtro:",
    "pergunta2": "Quem Deus diz que eu sou, com as minhas palavras:",
}

CORPO_ALMA_ESPIRITO = {
    "titulo": "Corpo, alma e espírito",
    "versiculo": "Todo o vosso espírito, e alma, e corpo, sejam plenamente conservados irrepreensíveis para a vinda de nosso Senhor Jesus Cristo.",
    "ref": "1 Tessalonicenses 5:23",
    "intro": "A gente vive separando. Fé é domingo, corpo é academia, cabeça é terapia. A Bíblia não separa. O que você faz com um mexe nos outros dois. Um só hábito derruba os três. E um só hábito, feito com fidelidade, levanta os três. O alvo é um só: glorificar a Deus em tudo. Em casa, na igreja, no trabalho, nos relacionamentos. Por isso o fruto do Espírito vale pra todas as áreas, não só pro domingo.",
    "pilares": [
        ("Corpo", "salvia", "Templo do Espírito Santo. Você cuida dele porque não é seu.", "Água · Sono · Comida de verdade · Movimento", "Glorificai, pois, a Deus no vosso corpo.", "1 Coríntios 6:20"),
        ("Alma", "dourado", "Mente, vontade e emoções. Renova-se pensando diferente.", "Pensamentos · Foco · Leitura · Domínio próprio", "Transformai-vos pela renovação do vosso entendimento.", "Romanos 12:2"),
        ("Espírito", "rubi", "Onde Deus fala com você. Exercita-se em piedade.", "Oração · Palavra · Obediência · Caráter", "Exercita-te a ti mesmo em piedade.", "1 Timóteo 4:7"),
    ],
    "virtudes_titulo": "As quatro virtudes desta travessia",
    "virtudes": [
        ("Temperança", "Dizer não a você mesma quando precisa.", "Provérbios 25:28"),
        ("Fé", "Confiar no que Deus disse antes de ver.", "Hebreus 11:1"),
        ("Fidelidade", "Fazer no escuro o que prometeu na luz.", "Lucas 16:10"),
        ("Coragem", "Fazer com medo.", "Josué 1:9"),
    ],
    "fruto": "O fruto do Espírito é: amor, gozo, paz, longanimidade, benignidade, bondade, fé, mansidão, temperança.",
    "fruto_ref": "Gálatas 5:22-23",
}

PROPOSITO_LIMITES = {
    "titulo": "Propósito e limites",
    "prop_intro": "Propósito dá direção. Sem ele, meta vira lista solta. E propósito não precisa ser extraordinário: cuidar bem da casa, ser uma filha melhor, ajudar uma amiga, criar os filhos na fé. Você tem várias versões, mulher, filha, esposa, mãe, amiga, e Deus tem um propósito pra cada uma. Escreva o rascunho hoje. No dia 40 você volta aqui e vê o que clareou.",
    "prop_versiculo": "Muitos propósitos há no coração do homem, porém o conselho do Senhor permanecerá.",
    "prop_ref": "Provérbios 19:21",
    "prop_perguntas": [
        "O que queima no meu coração e não sai da cabeça?",
    ],
    "prop_papeis": ["Como mulher", "Como filha", "Como esposa (ou um dia)", "Como mãe (ou um dia)"],
    "prop_frase": "Meu propósito em uma frase (rascunho, pode mudar até o dia 40):",
    "prop_papeis_titulo": "Meu propósito em cada papel, hoje",
    "lim_intro": "Mulher sem limite claro aceita qualquer coisa e depois se pergunta como chegou ali. Decida com a cabeça fria o que segura você quando o coração esquenta.",
    "lim_versiculo": "Sobre tudo o que se deve guardar, guarda o teu coração, porque dele procedem as saídas da vida.",
    "lim_ref": "Provérbios 4:23",
    "lim_areas": ["Relacionamento amoroso", "Amizades", "Família"],
    "lim_cols": ["Eu aceito", "Eu não aceito"],
}

REGRAS_SONHOS = {
    "titulo": "Regras e quadro dos sonhos",
    "regras_intro": "Inegociáveis por 40 dias. Marque as que valem e escreva as suas.",
    "regras": [
        "2 litros de água por dia.",
        "Celular fora do quarto.",
        "Primeira hora do dia sem tela.",
        "Palavra e oração no mesmo horário.",
        "Corpo em movimento 4 vezes por semana.",
        "Uma fruta antes de qualquer doce.",
        "Nenhuma palavra sobre quem não está presente.",
        "Contar até dez antes de responder o que irrita.",
    ],
    "sonhos_intro": "Metas que cabem em 40 dias e dá pra medir. \"Treinar 3 vezes por semana\", \"guardar 300 reais\", \"fazer as pazes com minha irmã\".",
    "sonhos_versiculo": "Escreve a visão e torna bem legível sobre tábuas.",
    "sonhos_ref": "Habacuque 2:2",
    "areas": [("Corpo", "salvia"), ("Mente", "dourado"), ("Espírito", "rubi"), ("Relacionamentos e casa", "ameixa")],
}

CARTA_FUTURO = {
    "titulo": "Carta pra mim, no dia 40",
    "intro": "Escreva pra mulher que vai abrir esta página daqui a 40 dias. Como você está hoje, o que dói, o que espera, quem quer que ela tenha se tornado. Dobre o canto. Só abra no dia 40.",
    "cabecalho": "Para: eu, no dia 40",
    "rodape": "Dobre este canto. Abrir só no dia 40.",
}

RETRATO = {
    "titulo_1": "Retrato do dia 1",
    "titulo_40": "Retrato do dia 40",
    "intro_1": "Uma foto honesta de onde você está hoje. Sem enfeitar. No dia 40 você volta aqui e compara.",
    "intro_40": "Volte ao retrato do dia 1 e preencha lado a lado. Não é sobre nota alta. É sobre ver onde Deus trabalhou.",
    "areas": ["Água e comida", "Sono", "Treino", "Foco e leitura", "Domínio próprio", "Oração", "Palavra", "Relacionamentos", "Casa e dinheiro", "Propósito claro"],
    "palavras_1": "Como eu me sinto hoje, em três palavras:",
    "incomodo_1": "O que mais me incomoda hoje:",
    "mudou_40": "O que mais mudou em mim:",
    "deus_40": "O que Deus fez que eu nem pedi:",
}

MAPA = {
    "titulo": "A travessia",
    "intro": "Quatro provas de 10 dias. Cada uma tem um lugar, uma virtude e uma mulher que já passou por ali. Marque ao terminar.",
}

TRACKER_HABITOS = ["Água", "Movimento", "Comida", "Sono", "Leitura", "Palavra", "Oração", "Sem tela 1ª h", "Domínio próprio", "Autocuidado"]

REVISAO = {
    "titulo": "Revisão da prova",
    "perguntas": [
        ("O que melhorou nestes 10 dias?", 3),
        ("Qual foi a maior dificuldade e o que ela me mostrou?", 3),
        ("Onde a virtude apareceu? Onde faltou?", 3),
        ("Uma conversa com Deus sobre esses dias:", 5),
    ],
    "notas": ["Corpo", "Mente", "Espírito", "Virtude"],
}

FECHAMENTO = {
    "titulo": "E agora?",
    "versiculo": "Aquele que em vós começou a boa obra a aperfeiçoará até ao dia de Jesus Cristo.",
    "ref": "Filipenses 1:6",
    "paragrafos": [
        "Quarenta dias. Você atravessou. Talvez não com todas as caixinhas marcadas, talvez com mais dias pulados do que gostaria. Não importa. Você abriu este caderno quarenta vezes. Isso é fidelidade, e fidelidade sustenta todas as outras virtudes.",
        "Olhe o retrato do dia 1 e o do dia 40 lado a lado. Não só os números. Veja como você responde, como dorme, como fala com Deus e com as pessoas. Isso é o que Ele fez, com a sua mão na dele.",
        "O que virou hábito fica. O que ainda não virou entra na próxima travessia. Porque sim, existe uma próxima. A mulher virtuosa não é a que chegou. É a que não para.",
    ],
    "proximos": ["As três coisas que viraram hábito:", "A virtude que preciso treinar de novo:", "O que clareou sobre o meu propósito, como mulher, filha, esposa, mãe:", "Quem vou chamar pra fazer comigo:"],
    "comunidade": "Você não foi feita pra caminhar sozinha. Conte o que mudou. Convide uma amiga. Virtude se espalha por contágio.",
}

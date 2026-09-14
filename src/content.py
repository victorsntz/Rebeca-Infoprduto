# -*- coding: utf-8 -*-
"""
Conteúdo do caderno "De Tola a Virtuosa: 100 dias".
Tudo que é texto vive aqui. O build.py só monta as páginas.
"""

TITULO = "De Tola a Virtuosa"
SUBTITULO = "100 dias pra virar a mulher que Deus já disse que você é"
TAGLINE = "Um caderno prático de corpo, mente e espírito"

VERSICULO_CAPA = {
    "texto": "Mulher virtuosa, quem a achará? O seu valor muito excede o de rubis.",
    "ref": "Provérbios 31:10",
}

# ---------------------------------------------------------------------------
# Fases
# ---------------------------------------------------------------------------
FASES = [
    {
        "num": 1,
        "nome": "Fundamento",
        "dias": "Dias 1 a 30",
        "inicio": 1,
        "fim": 30,
        "cor": "salvia",
        "versiculo": "Cavou, abriu bem fundo e pôs os alicerces sobre a rocha.",
        "ref": "Lucas 6:48",
        "resumo": "Aqui a gente não constrói nada bonito ainda. A gente cava. Água, sono, comida de verdade, corpo em movimento, Palavra e oração todo dia. Casa e dinheiro começam a ser olhados de frente. E você começa a responder a pergunta mais difícil: quem eu sou?",
        "foco": [
            "Instalar os hábitos base: 2 litros de água, 7 horas de sono, uma fruta por dia, corpo em movimento.",
            "Criar o horário fixo com Deus. Curto e todo dia vale mais que longo e de vez em quando.",
            "Organizar o que está bagunçado: um cômodo, os gastos, as pendências.",
            "Preencher o quadro dos sonhos, a carta pro futuro e o retrato do dia 1 antes do dia 1.",
        ],
    },
    {
        "num": 2,
        "nome": "Construção",
        "dias": "Dias 31 a 60",
        "inicio": 31,
        "fim": 60,
        "cor": "dourado",
        "versiculo": "Assim edificamos o muro, e todo o muro se fechou até a metade da sua altura; porque o coração do povo se inclinava a trabalhar.",
        "ref": "Neemias 4:6",
        "resumo": "O alicerce está pronto. Agora sobe parede. O treino fica mais pesado, as conversas que você evitava acontecem, e os relacionamentos entram no jogo. Neemias levantou um muro inteiro em 52 dias com gente rindo dele. Você tem 30.",
        "foco": [
            "Subir de nível no corpo: mais carga, mais tempo ou mais dias de treino.",
            "Enfrentar o que dá medo: a conversa difícil, o pedido de ajuda, o projeto parado.",
            "Trabalhar paciência e mansidão onde mais dói: família, namoro, casamento, amizades.",
            "Servir de propósito. Uma comida especial, uma visita, uma ajuda prática.",
        ],
    },
    {
        "num": 3,
        "nome": "Consolidação",
        "dias": "Dias 61 a 90",
        "inicio": 61,
        "fim": 90,
        "cor": "rubi",
        "versiculo": "Arraigados e sobreedificados nele, e confirmados na fé, assim como fostes ensinados, nela abundando em ação de graças.",
        "ref": "Colossenses 2:7",
        "resumo": "Aqui separa quem fez uma dieta de quem mudou de vida. O segredo desta fase é chato de propósito: repetir. Repetir até o hábito não precisar mais de você lembrando. Fidelidade no pequeno, humildade pra ouvir, alegria que não depende do dia.",
        "foco": [
            "Repetir a rotina completa mesmo sem vontade. Vontade é hóspede, hábito é morador.",
            "Fechar as promessas em aberto, com pessoas e com você mesma.",
            "Pedir feedback honesto e não se defender.",
            "Proteger a paz: menos notícia, menos comparação, mais silêncio com Deus.",
        ],
    },
    {
        "num": 4,
        "nome": "Fechamento",
        "dias": "Dias 91 a 100",
        "inicio": 91,
        "fim": 100,
        "cor": "ameixa",
        "versiculo": "Até aqui nos ajudou o Senhor.",
        "ref": "1 Samuel 7:12",
        "resumo": "Dez dias pra olhar pra trás com honestidade. Comparar o dia 1 com o dia 100. Marcar o que virou hábito de verdade, o que ficou pelo caminho, o que Deus fez que você nem pediu. E abrir a carta.",
        "foco": [
            "Reler o retrato do dia 1 e fazer o retrato do dia 100.",
            "Revisar cada meta do quadro dos sonhos, sem se punir pelas que não vieram.",
            "Contar pra alguém o que mudou. Testemunho firma o que aconteceu.",
            "Decidir os próximos 100 dias antes de terminar estes.",
        ],
    },
]

# ---------------------------------------------------------------------------
# Blocos de 10 dias
# ---------------------------------------------------------------------------
BLOCOS = [
    {
        "num": 1, "inicio": 1, "fim": 10, "fase": 1,
        "virtude": "Temperança",
        "sub": "Domínio próprio",
        "definicao": "Temperança é comer o que basta, falar o que basta e parar quando precisa. Não é ser morna. É ter as rédeas na mão. A mulher sem domínio próprio é como cidade sem muro: qualquer coisa entra.",
        "versiculo": "Como cidade derribada, sem muro, assim é o homem que não pode conter o seu espírito.",
        "ref": "Provérbios 25:28",
        "tola": "espera ter vontade pra começar.",
        "virtuosa": "começa e a vontade vem depois, ou não vem, e ela faz mesmo assim.",
        "metas": {
            "corpo": "2 litros de água por dia e uma fruta antes de qualquer doce.",
            "mente": "Celular fora do quarto. Primeira hora do dia sem tela.",
            "espirito": "10 minutos de Palavra e oração no mesmo horário, todos os dias.",
        },
    },
    {
        "num": 2, "inicio": 11, "fim": 20, "fase": 1,
        "virtude": "Fé",
        "sub": "Identidade e confiança",
        "definicao": "Fé é confiar no que Deus disse antes de ver acontecer. E o que Ele disse sobre você é bem claro: filha, escolhida, menina dos olhos dele. Quem acredita nisso age diferente sem precisar se forçar.",
        "versiculo": "Ora, a fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem.",
        "ref": "Hebreus 11:1",
        "tola": "se define pelo que sente hoje de manhã.",
        "virtuosa": "se define pelo que Deus falou, e o que ela sente vai atrás.",
        "metas": {
            "corpo": "Manter o bloco 1 e adicionar 20 minutos de caminhada, 3 vezes na semana.",
            "mente": "Colar versículos de identidade no espelho e ler em voz alta ao acordar.",
            "espirito": "Orar em voz alta pelo menos uma vez por dia. Memorizar 2 versículos.",
        },
    },
    {
        "num": 3, "inicio": 21, "fim": 30, "fase": 1,
        "virtude": "Prudência",
        "sub": "Sabedoria prática",
        "definicao": "Prudência é pensar antes. É contar o custo antes de construir, olhar a conta antes de comprar, planejar a semana antes que ela te atropele. A mulher sábia edifica a casa. A tola derruba com as próprias mãos, e geralmente nem percebe.",
        "versiculo": "Toda mulher sábia edifica a sua casa; mas a tola derruba-a com as suas próprias mãos.",
        "ref": "Provérbios 14:1",
        "tola": "não sabe pra onde o dinheiro foi nem onde o tempo passou.",
        "virtuosa": "anota, planeja e decide antes que a vida decida por ela.",
        "metas": {
            "corpo": "Planejar as refeições da semana. Cozinhar pelo menos 4 dias.",
            "mente": "Anotar todos os gastos por 10 dias. Organizar um cômodo por completo.",
            "espirito": "Ler Provérbios com caneta na mão, marcando o que fala de casa, boca e dinheiro.",
        },
    },
    {
        "num": 4, "inicio": 31, "fim": 40, "fase": 2,
        "virtude": "Fortaleza",
        "sub": "Coragem",
        "definicao": "Coragem não é ausência de medo. É fazer com medo. Fortaleza é continuar quando dói, quando cansa, quando ninguém está olhando. Ester entrou na sala do rei tremendo. Entrou mesmo assim.",
        "versiculo": "Não to mandei eu? Esforça-te, e tem bom ânimo; não temas, nem te espantes; porque o Senhor teu Deus é contigo, por onde quer que andares.",
        "ref": "Josué 1:9",
        "tola": "evita a conversa, o treino e a decisão porque dói.",
        "virtuosa": "sente a mesma dor e vai mesmo assim.",
        "metas": {
            "corpo": "Aumentar o treino: mais peso, mais tempo ou mais um dia na semana.",
            "mente": "Ter a conversa que está sendo evitada. Terminar um projeto parado.",
            "espirito": "Escrever cada medo e o que a Bíblia responde a ele.",
        },
    },
    {
        "num": 5, "inicio": 41, "fim": 50, "fase": 2,
        "virtude": "Paciência",
        "sub": "Mansidão",
        "definicao": "Paciência é esperar sem azedar. Mansidão é força sob controle, não fraqueza. A mulher mansa não é a que não tem opinião. É a que tem e sabe a hora e o tom de dizer. Governar o próprio espírito vale mais que conquistar uma cidade.",
        "versiculo": "Melhor é o longânimo do que o valente, e o que governa o seu espírito do que o que toma uma cidade.",
        "ref": "Provérbios 16:32",
        "tola": "responde na hora, no tom que veio, e depois pede desculpa.",
        "virtuosa": "respira, conta até dez e responde do jeito que edifica.",
        "metas": {
            "corpo": "Uma refeição por dia sem celular na mesa, com alguém.",
            "mente": "Contar até dez antes de responder qualquer coisa que irritar.",
            "espirito": "Orar pela pessoa que mais testa sua paciência, todos os dias do bloco.",
        },
    },
    {
        "num": 6, "inicio": 51, "fim": 60, "fase": 2,
        "virtude": "Bondade",
        "sub": "Benignidade e misericórdia",
        "definicao": "Bondade é fazer o bem sem plateia. Benignidade é gentileza que age, não só que sente. Misericórdia é perdoar como você foi perdoada. A mulher de Provérbios 31 abre a mão ao pobre e estende os braços ao necessitado. Ela serve. Sem postar.",
        "versiculo": "Antes sede uns para com os outros benignos, misericordiosos, perdoando-vos uns aos outros, como também Deus vos perdoou em Cristo.",
        "ref": "Efésios 4:32",
        "tola": "ajuda quando é vista e cobra depois.",
        "virtuosa": "ajuda em segredo e esquece que ajudou.",
        "metas": {
            "corpo": "Cozinhar algo especial pra alguém. Um bolo, um almoço, um pão.",
            "mente": "Elogiar três pessoas por dia, na frente de outras.",
            "espirito": "Um ato de bondade anônimo por dia. Ninguém pode saber.",
        },
    },
    {
        "num": 7, "inicio": 61, "fim": 70, "fase": 3,
        "virtude": "Fidelidade",
        "sub": "Constância",
        "definicao": "Fidelidade é fazer no escuro o que você prometeu na luz. É repetir o hábito no dia 65 com a mesma seriedade do dia 5. Quem é fiel no pouco recebe o muito. Não existe atalho aqui, e é exatamente por isso que pouca gente chega.",
        "versiculo": "Quem é fiel no pouco, também é fiel no muito; quem é injusto no pouco, também é injusto no muito.",
        "ref": "Lucas 16:10",
        "tola": "promete grande e entrega quando lembra.",
        "virtuosa": "promete pequeno e entrega sempre.",
        "metas": {
            "corpo": "Repetir o mesmo treino de 30 dias atrás e anotar a diferença.",
            "mente": "Cumprir a rotina completa todos os 10 dias, com ou sem vontade.",
            "espirito": "Ler a Bíblia no mesmo horário todos os dias. Sem exceção.",
        },
    },
    {
        "num": 8, "inicio": 71, "fim": 80, "fase": 3,
        "virtude": "Humildade",
        "sub": "Se ver do tamanho certo",
        "definicao": "Humildade não é se achar pequena. É se ver do tamanho certo: uma filha amada que ainda tem muito a aprender. A mulher humilde pede feedback e não se defende. Aprende com quem é mais novo. Serve quem não merece. Maria disse: eis aqui a serva do Senhor.",
        "versiculo": "Nada façais por contenda ou por vanglória, mas por humildade; cada um considere os outros superiores a si mesmo.",
        "ref": "Filipenses 2:3",
        "tola": "precisa ter razão e ser vista.",
        "virtuosa": "prefere estar certa diante de Deus e não faz questão de plateia.",
        "metas": {
            "corpo": "Fazer a tarefa mais chata da casa cantando um louvor.",
            "mente": "Perguntar a três pessoas onde você precisa melhorar. Só ouvir e anotar.",
            "espirito": "Orar de joelhos pelo menos uma vez por dia.",
        },
    },
    {
        "num": 9, "inicio": 81, "fim": 90, "fase": 3,
        "virtude": "Alegria e Paz",
        "sub": "Coração firme",
        "definicao": "Alegria é força que não depende de como foi o dia. Paz é mente firme em Deus no meio do barulho. As duas são fruto, não esforço. Mas fruto precisa de solo, e o solo você prepara: menos notícia, menos comparação, mais silêncio, mais louvor.",
        "versiculo": "Tu conservarás em paz aquele cuja mente está firme em ti; porque ele confia em ti.",
        "ref": "Isaías 26:3",
        "tola": "deixa o feed decidir o humor do dia.",
        "virtuosa": "decide o humor antes de abrir qualquer tela: com louvor e com a Palavra.",
        "metas": {
            "corpo": "Dormir uma hora mais cedo. Caminhar ao ar livre 3 vezes.",
            "mente": "Zero notícia e zero comparação por 10 dias. Um hobby de volta.",
            "espirito": "15 minutos de silêncio por dia. Sem música, sem tela. Só Deus.",
        },
    },
    {
        "num": 10, "inicio": 91, "fim": 100, "fase": 4,
        "virtude": "Amor e Esperança",
        "sub": "O que fica",
        "definicao": "Fé, esperança e amor. Os três ficam, mas o maior é o amor. Nestes dez dias você vai olhar pra trás e ver que tudo que mudou em você foi por amor: a Deus, às pessoas, à mulher que Ele te chamou pra ser. E vai olhar pra frente com esperança. Os próximos 100 dias já estão na mesa.",
        "versiculo": "Agora, pois, permanecem a fé, a esperança e o amor, estes três; mas o maior destes é o amor.",
        "ref": "1 Coríntios 13:13",
        "tola": "termina e esquece.",
        "virtuosa": "termina, agradece, anota o que aprendeu e recomeça mais forte.",
        "metas": {
            "corpo": "Fazer o retrato do dia 100 e comparar com o dia 1.",
            "mente": "Revisar cada meta do quadro dos sonhos. Marcar as cumpridas.",
            "espirito": "Escrever uma carta de gratidão a Deus pelos 100 dias. Abrir a carta do dia 1.",
        },
    },
]

# ---------------------------------------------------------------------------
# Desafios diários (100)
# ---------------------------------------------------------------------------
DESAFIOS = [
    # Bloco 1: Temperança
    "Encha uma garrafa de 1 litro de manhã e termine antes do almoço. Encha de novo.",
    "Deixe o celular fora do quarto esta noite. Compre um despertador de verdade se precisar.",
    "Escreva na geladeira as três coisas que você vai parar de comer nesses 100 dias.",
    "Caminhe 20 minutos hoje. Sem fone. Só você e o que passa na sua cabeça.",
    "Coma uma fruta antes de qualquer doce hoje. Se ainda quiser o doce depois, pode.",
    "Escolha um horário fixo pra dormir e cumpra hoje. Deitar de verdade, não deitar com o celular.",
    "Diga não a uma coisa hoje. Pequena. Só pra lembrar que você consegue.",
    "Prepare a sua própria comida em pelo menos duas refeições hoje.",
    "Passe o dia inteiro sem reclamar em voz alta. Se escapar, recomece a contagem.",
    "Faça o treino que você vem adiando. Dez minutos já contam.",
    # Bloco 2: Fé
    "Escreva três versículos sobre quem você é e cole no espelho do banheiro.",
    "Ore em voz alta hoje, mesmo que só por dois minutos. Ouvir a própria voz falando com Deus muda alguma coisa.",
    "Entregue a Deus uma preocupação específica, por escrito, e não a pegue de volta hoje.",
    "Conte pra alguém uma coisa que Deus fez na sua vida.",
    "Leia o capítulo de hoje duas vezes: uma pra entender, outra pra ouvir.",
    "Jejue de redes sociais por 24 horas. Use o tempo que sobrar na Palavra.",
    "Agradeça a Deus por uma coisa que você ainda está esperando.",
    "Peça perdão a Deus por algo que você vem escondendo. Depois deixe lá.",
    "Faça uma lista de dez orações que Deus já respondeu na sua vida.",
    "Memorize um versículo hoje. Repita até conseguir dizer sem olhar.",
    # Bloco 3: Prudência
    "Anote tudo o que gastou hoje. Cada centavo. Só olhar, sem julgar.",
    "Arrume um cômodo por completo. Um só. Tire o que você não usa.",
    "Planeje as refeições dos próximos três dias e faça a lista de compras.",
    "Liste tudo o que está pendente na sua vida e resolva uma coisa hoje.",
    "Passe uma hora sem celular fazendo algo com as mãos: cozinhar, organizar, costurar, plantar.",
    "Descubra quanto você gasta por mês com delivery e lanche fora. Escreva o número.",
    "Defina um valor pra guardar até o dia 100, mesmo que pequeno. Separe a primeira parte hoje.",
    "Acorde 30 minutos mais cedo e use esse tempo com Deus antes de qualquer tela.",
    "Faça uma pergunta a uma mulher mais velha que você admira. Anote a resposta.",
    "Revise o quadro dos sonhos. O que já mexeu? O que precisa ajustar?",
    # Bloco 4: Fortaleza
    "Aumente o treino hoje: mais peso, mais tempo ou mais repetições. Você já não é a do dia 1.",
    "Tenha a conversa que você vem evitando. Com mansidão e firmeza.",
    "Faça algo sozinha que você normalmente só faria acompanhada.",
    "Levante na primeira vez que o despertador tocar. Sem soneca.",
    "Escreva um medo que te trava e o que a Bíblia diz sobre ele.",
    "Termine o banho com 30 segundos de água fria. Corpo e mente aprendem que desconforto não mata.",
    "Peça ajuda a alguém em algo que você tem vergonha de não saber.",
    "Termine hoje uma coisa que você começou e largou pela metade.",
    "Diga a uma pessoa, em amor, uma verdade que ela precisa ouvir.",
    "Faça 30 minutos de exercício sem parar. Caminhada rápida vale.",
    # Bloco 5: Paciência
    "Antes de responder qualquer coisa que te irritar hoje, conte até dez e respire.",
    "Escute alguém por dez minutos sem interromper e sem dar conselho.",
    "Mande uma mensagem carinhosa pra alguém da família que você tem tratado com pressa.",
    "Perdoe uma pessoa por escrito. Não precisa enviar. Precisa soltar.",
    "Passe o dia sem sarcasmo e sem ironia. Perceba quantas vezes deu vontade.",
    "Faça uma refeição sem celular na mesa, com alguém. Só conversa.",
    "Dê uma resposta branda numa situação que pedia uma dura. Provérbios 15:1 na prática.",
    "Espere na fila, no trânsito ou na demora de alguém sem reclamar. Ore pela pessoa.",
    "Peça desculpas por algo que você fez. Sem o 'mas'.",
    "Ligue pra sua mãe, sua avó ou alguém que te criou. Só pra ouvir.",
    # Bloco 6: Bondade
    "Faça uma comida especial pra alguém, sem motivo. Pode ser um bolo.",
    "Sirva em casa sem ser pedida: lave, arrume, cuide de algo que não é 'sua responsabilidade'.",
    "Abençoe uma amiga com algo prático: uma visita, uma ajuda, um presente pequeno.",
    "Elogie três pessoas hoje, na frente de outras.",
    "Dê algo que você gosta pra alguém que precisa mais.",
    "Visite ou ligue pra alguém que está sozinho ou doente.",
    "Faça um ato de bondade anônimo. Ninguém pode saber. Nem depois.",
    "Ore por cinco pessoas pelo nome, incluindo alguém que te feriu.",
    "Ofereça ajuda a uma mulher que está começando algo que você já passou.",
    "Escreva um bilhete de gratidão à mão e entregue pessoalmente.",
    # Bloco 7: Fidelidade
    "Repita hoje o hábito mais difícil dos últimos 60 dias. Sem negociar.",
    "Cumpra o que você prometeu a alguém e ainda não fez.",
    "Faça a rotina completa hoje, mesmo sem vontade. Vontade é hóspede, hábito é morador.",
    "Volte a uma meta do quadro dos sonhos que você deixou pra trás.",
    "Passe o dia sem falar de ninguém que não esteja presente.",
    "Seja pontual em tudo hoje. Chegar na hora é fidelidade com o tempo dos outros.",
    "Faça o mesmo treino de 30 dias atrás e compare. Anote a diferença.",
    "Leia a Bíblia no mesmo horário dos últimos dias, mesmo que seja só um capítulo.",
    "Guarde um segredo que você estava com vontade de contar.",
    "Reveja suas regras inegociáveis. Qual você mais quebrou? Recomece por ela hoje.",
    # Bloco 8: Humildade
    "Pergunte a três pessoas próximas: 'em que eu preciso melhorar?'. Só ouça e anote.",
    "Deixe alguém ter a última palavra numa discussão que você ganharia.",
    "Sirva alguém que você acha que não merece.",
    "Admita um erro em voz alta hoje, sem se justificar.",
    "Aprenda alguma coisa com alguém mais novo que você.",
    "Faça a tarefa mais chata da casa cantando um louvor.",
    "Passe o dia sem falar de si mesma, a menos que perguntem.",
    "Agradeça a alguém por uma crítica que você recebeu.",
    "Ore de joelhos hoje. A postura do corpo ensina o coração.",
    "Escreva dez coisas boas que você tem e não conquistou. Só recebeu.",
    # Bloco 9: Alegria e Paz
    "Comece o dia com um louvor tocando, antes de qualquer notícia ou rede social.",
    "Faça algo que te dá alegria de verdade e que você deixou de lado. Só por fazer.",
    "Ande 20 minutos ao ar livre e agradeça por tudo o que enxergar.",
    "Escreva o que rouba sua paz e entregue item por item em oração.",
    "Passe o dia sem checar notícias. Veja se o mundo acaba.",
    "Ria alto com alguém hoje. Ligue pra aquela amiga engraçada.",
    "Durma uma hora mais cedo hoje. Só isso. É o desafio inteiro.",
    "Escreva uma carta de gratidão a Deus pelos últimos 87 dias.",
    "Faça 15 minutos de silêncio. Sem música, sem tela, sem falar. Só Deus e você.",
    "Celebre os 90 dias. Um jantar, uma foto, um passeio. Marque a data.",
    # Bloco 10: Amor e Esperança
    "Releia o retrato do dia 1. Escreva o que você sente ao ler.",
    "Diga 'eu te amo' pra três pessoas hoje, olhando nos olhos.",
    "Faça algo por alguém que nunca vai poder retribuir.",
    "Escreva o que você espera de Deus para os próximos 100 dias.",
    "Revise cada meta do quadro dos sonhos. Marque as cumpridas. Anote o que aprendeu com as que não vieram.",
    "Conte pra uma amiga o que mudou em você. Convide ela pra jornada.",
    "Perdoe a si mesma pelos dias em que falhou. Deus já perdoou.",
    "Escreva o que virou hábito de verdade. Esses ficam com você.",
    "Faça o retrato do dia 100. Compare com o dia 1 com honestidade.",
    "Abra a carta que você escreveu antes do dia 1. Leia em voz alta. Agradeça.",
]

# ---------------------------------------------------------------------------
# Plano de leitura (100)
# ---------------------------------------------------------------------------
LEITURAS = [
    # Bloco 1
    "Provérbios 31", "Mateus 7:24-29", "Romanos 12", "1 Coríntios 9:24-27", "1 Timóteo 4",
    "1 Coríntios 6:12-20", "Provérbios 25", "Salmo 1", "Gálatas 5:16-26", "2 Pedro 1:1-11",
    # Bloco 2
    "Salmo 139", "Efésios 1", "Efésios 2", "1 Pedro 2:1-12", "Hebreus 11",
    "Zacarias 2", "João 1", "Romanos 8", "Salmo 103", "2 Coríntios 5",
    # Bloco 3
    "Provérbios 14", "Provérbios 24", "Provérbios 6:1-11", "Lucas 14:25-35", "Provérbios 21",
    "Provérbios 22", "Mateus 6:19-34", "Salmo 90", "Provérbios 3", "Tiago 1",
    # Bloco 4
    "Josué 1", "Ester 4", "Ester 5", "Isaías 41", "Salmo 27",
    "2 Timóteo 1", "Neemias 2", "Neemias 4", "Neemias 6", "Efésios 6:10-20",
    # Bloco 5
    "Provérbios 15", "Tiago 3", "Provérbios 16", "Mateus 18:21-35", "Efésios 4",
    "Colossenses 3", "Provérbios 19", "Romanos 5:1-11", "1 Samuel 25", "Rute 1",
    # Bloco 6
    "Rute 2", "Rute 3", "Rute 4", "Lucas 10:25-42", "Atos 9:36-43",
    "Mateus 25:31-46", "Atos 16:11-15", "Miquéias 6", "Lucas 6:27-49", "1 João 3",
    # Bloco 7
    "Lucas 16:1-13", "Salmo 15", "Mateus 25:14-30", "Gálatas 6", "Salmo 101",
    "Provérbios 20", "Hebreus 12", "Josué 24", "Provérbios 11", "Daniel 1",
    # Bloco 8
    "Filipenses 2", "Lucas 1:26-56", "1 Samuel 1", "1 Samuel 2:1-11", "Mateus 11:25-30",
    "Lucas 14:1-14", "1 Pedro 5", "Provérbios 18", "Salmo 51", "Salmo 131 e Isaías 66:1-2",
    # Bloco 9
    "Salmo 100", "Filipenses 4", "Salmo 23", "Isaías 26:1-13", "Neemias 8",
    "Salmo 126", "Salmo 4 e Salmo 127", "Salmo 136", "Salmo 46", "João 14",
    # Bloco 10
    "1 Coríntios 13", "João 13:1-17", "1 João 4", "Jeremias 29:1-14", "Filipenses 3",
    "João 15", "Lamentações 3:19-33", "Isaías 43:1-21", "Filipenses 1", "Apocalipse 21:1-7",
]

assert len(DESAFIOS) == 100, len(DESAFIOS)
assert len(LEITURAS) == 100, len(LEITURAS)

# ---------------------------------------------------------------------------
# Páginas de abertura
# ---------------------------------------------------------------------------
CARTA_BOAS_VINDAS = {
    "titulo": "Antes de começar",
    "paragrafos": [
        "Menina chora. Mulher entende o que precisa fazer e quer melhorar. Se você está com este caderno na mão, já escolheu o segundo caminho. Bem-vinda.",
        "Este não é um livro pra ler. É um caderno pra usar. Todo dia, por 100 dias, você vai marcar, escrever, riscar, errar e continuar. Ele vai ficar amassado, com marca de café e letra feia. Ótimo. Caderno limpo é caderno que ninguém usou.",
        "A ideia é simples: a Bíblia diz que somos espírito, alma e corpo, e que tudo isso anda junto. Dormir mal vira irritação. Irritação vira palavra dura. Palavra dura vira distância de quem você ama e de Deus. Por isso aqui você vai cuidar dos três ao mesmo tempo: beber água e orar, treinar e perdoar, organizar a casa e renovar a mente. Nada está separado. O Evangelho se vive na pia da cozinha, no trânsito, no treino e no quarto com a porta fechada.",
        "Você vai passar por dez virtudes, uma a cada dez dias. Vai ter um desafio prático todo dia, uma leitura curta e um checklist de cinco minutos pra fechar a noite. E vai escrever, sempre, qual foi a sua maior dificuldade. Essa resposta é o seu mapa. Ela mostra exatamente onde Deus está trabalhando em você.",
        "Uma coisa precisa ficar clara: 'tola' aqui não é xingamento. É diagnóstico. A tola de Provérbios não é burra. É distraída de si mesma, do que fala, do que come, de quem deixa entrar. A virtuosa é a que acordou pra isso. Todas nós começamos tolas em alguma área. A diferença é quem decide sair.",
        "Não existe 100 dias perfeitos. Existe 100 dias vividos. Se perder um dia, marque o X, não se condene e volte no dia seguinte. Deus não está contando suas falhas. Está esperando você na próxima página.",
    ],
    "assinatura": "Vamos. Do dia 1 ao dia 100.",
}

COMO_USAR = {
    "titulo": "Como usar este caderno",
    "intro": "As regras do jogo. Poucas e claras.",
    "regras": [
        ("Imprima e encaderne.", "Fichário, espiral ou grampo. Deixe na mesa de cabeceira, não numa gaveta."),
        ("Preencha as páginas iniciais antes do dia 1.", "Identidade, propósito, limites, regras, quadro dos sonhos, carta pro futuro e retrato do dia 1. Reserve uma tarde."),
        ("Leia a abertura do bloco antes dos 10 dias.", "Ela diz qual virtude você vai treinar e quais metas cumprir. Escreva a sua meta pessoal ali."),
        ("Uma página por dia.", "De manhã: leia o desafio e a leitura. À noite: marque o checklist e escreva. Cinco minutos bastam."),
        ("Escreva a maior dificuldade. Sempre.", "É a pergunta mais importante do caderno. Não pule."),
        ("A cada 10 dias, faça a revisão do bloco.", "Quinze minutos. Compare, ajuste, agradeça."),
        ("Perdeu um dia? Marque o X e siga.", "Não compense, não desista, não recomece do zero. Vire a página."),
        ("No dia 100, abra a carta.", "E depois decida os próximos 100 dias."),
    ],
    "legenda_titulo": "O que tem na página de cada dia",
    "legenda": [
        ("Leitura de hoje", "Um trecho curto da Bíblia, ligado à virtude do bloco. Leia com caneta na mão."),
        ("Desafio do dia", "Uma ação concreta. Não é sugestão, é tarefa."),
        ("Checklist corpo, mente e espírito", "Nove caixinhas. Marque à noite, com honestidade."),
        ("Virtude em ação", "Onde a virtude do bloco apareceu no seu dia. Ou onde faltou."),
        ("Gratidão", "Três coisas. Específicas. 'Pela vida' não vale."),
        ("Maior dificuldade", "O mapa. Escreva o que foi mais difícil hoje e por quê."),
        ("Amanhã eu vou", "Uma coisa só. A que mais importa."),
    ],
}

TOLA_VIRTUOSA = {
    "titulo": "Tola ou virtuosa?",
    "versiculo": "Toda mulher sábia edifica a sua casa; mas a tola derruba-a com as suas próprias mãos.",
    "ref": "Provérbios 14:1",
    "intro": "Provérbios coloca duas mulheres lado a lado o livro inteiro. Uma edifica. A outra derruba. E o detalhe que assusta: as duas têm as mesmas mãos. A diferença não é talento, beleza nem sorte. É o que cada uma faz todo dia, no ordinário, quando ninguém está olhando.",
    "contrastes": [
        ("espera ter vontade.", "cria rotina."),
        ("se compara.", "se examina."),
        ("derruba a casa com a boca.", "edifica a casa com as mãos."),
        ("quer tudo em uma semana.", "planta e espera."),
        ("reage.", "responde."),
        ("corre atrás de ser vista.", "é achada."),
        ("cuida da aparência e esquece o coração.", "cuida dos dois, na ordem certa."),
        ("culpa.", "assume."),
        ("separa fé de vida.", "vive o Evangelho na pia da cozinha."),
        ("chora e para.", "chora e continua."),
    ],
    "fechamento": "Você vai se reconhecer nas duas colunas. Todas nós. A pergunta destes 100 dias é: em qual coluna você quer terminar?",
}

IDENTIDADE = {
    "titulo": "Quem Deus diz que você é",
    "intro": "Tudo neste caderno nasce daqui. Virtude, feminilidade, disciplina, relacionamentos: tudo brota de identidade. Quem sabe quem é age diferente sem precisar se forçar. E quem não sabe passa a vida tentando ser o que a última comparação mandou.",
    "versiculos": [
        ("Menina dos olhos dele", "Aquele que tocar em vós toca na menina do seu olho.", "Zacarias 2:8"),
        ("Feita de modo assombroso", "Eu te louvarei, porque de um modo assombroso e tão maravilhoso fui feito.", "Salmo 139:14"),
        ("Obra dele, com propósito", "Somos feitura sua, criados em Cristo Jesus para as boas obras, as quais Deus preparou para que andássemos nelas.", "Efésios 2:10"),
        ("Escolhida", "Vós sois a geração eleita, o sacerdócio real, a nação santa, o povo adquirido.", "1 Pedro 2:9"),
        ("Filha", "A todos quantos o receberam, deu-lhes o poder de serem feitos filhos de Deus.", "João 1:12"),
        ("Nova criatura", "Se alguém está em Cristo, nova criatura é; as coisas velhas já passaram; eis que tudo se fez novo.", "2 Coríntios 5:17"),
    ],
    "pergunta1": "Quem eu sou hoje, sem filtro (o que eu penso de mim quando ninguém está olhando):",
    "pergunta2": "Quem Deus diz que eu sou (escreva com as suas palavras, como se fosse uma resposta ao que você escreveu acima):",
}

CORPO_ALMA_ESPIRITO = {
    "titulo": "Corpo, alma e espírito",
    "versiculo": "E o mesmo Deus de paz vos santifique em tudo; e todo o vosso espírito, e alma, e corpo, sejam plenamente conservados irrepreensíveis para a vinda de nosso Senhor Jesus Cristo.",
    "ref": "1 Tessalonicenses 5:23",
    "intro": "A gente vive separando. Fé é domingo, corpo é academia, cabeça é terapia. A Bíblia não separa. Ela diz que Deus santifica os três, juntos, e que o que você faz com um mexe nos outros dois.",
    "pilares": [
        {
            "nome": "Corpo",
            "cor": "salvia",
            "frase": "Templo do Espírito Santo. Você cuida dele porque não é seu.",
            "itens": ["Água", "Sono", "Comida de verdade", "Movimento", "Disciplina física"],
            "versiculo": "Ou não sabeis que o vosso corpo é o templo do Espírito Santo? Glorificai, pois, a Deus no vosso corpo.",
            "ref": "1 Coríntios 6:19-20",
        },
        {
            "nome": "Alma",
            "cor": "dourado",
            "frase": "Mente, vontade e emoções. Renova-se pensando diferente.",
            "itens": ["Pensamentos", "Autoconhecimento", "Leitura", "Foco", "Domínio próprio"],
            "versiculo": "Transformai-vos pela renovação do vosso entendimento, para que experimenteis qual seja a boa, agradável e perfeita vontade de Deus.",
            "ref": "Romanos 12:2",
        },
        {
            "nome": "Espírito",
            "cor": "rubi",
            "frase": "Onde Deus fala com você. Exercita-se em piedade.",
            "itens": ["Oração", "Palavra", "Comunhão", "Obediência", "Caráter"],
            "versiculo": "Exercita-te a ti mesmo em piedade. Porque o exercício corporal para pouco aproveita, mas a piedade para tudo é proveitosa.",
            "ref": "1 Timóteo 4:7-8",
        },
    ],
    "fechamento": "Um exemplo simples: você dorme mal. Acorda irritada. Responde mal o marido, a mãe, a colega. Se sente culpada. Não ora, porque está com vergonha. Come besteira pra compensar. Dorme mal de novo. Viu? Um só hábito derruba os três. E um só hábito, feito com fidelidade, levanta os três. É por isso que o checklist de cada dia tem corpo, mente e espírito juntos.",
    "disciplina": "Antes subjugo o meu corpo, e o reduzo à servidão, para que, pregando aos outros, eu mesmo não venha de alguma maneira a ficar reprovado.",
    "disciplina_ref": "1 Coríntios 9:27",
}

VIRTUDES = {
    "titulo": "As virtudes",
    "intro": "Virtude é hábito bom que virou caráter. Não é sentimento, é prática. Aqui estão as que você vai treinar nestes 100 dias. Dez delas ganham um bloco inteiro. As outras aparecem nos desafios de cada dia.",
    "lista": [
        ("Domínio próprio", "Dizer não a você mesma quando precisa.", "Provérbios 25:28"),
        ("Temperança", "O que basta. Na comida, na fala, no gasto.", "Provérbios 25:16"),
        ("Fé", "Confiar no que Deus disse antes de ver.", "Hebreus 11:1"),
        ("Esperança", "Esperar com os pés no chão e os olhos em Deus.", "Romanos 5:5"),
        ("Amor a Deus", "O primeiro mandamento. A raiz de todos os outros.", "Mateus 22:37"),
        ("Amor ao próximo", "Querer o bem do outro e fazer algo a respeito.", "1 Coríntios 13:4-7"),
        ("Prudência", "Pensar antes. Contar o custo antes de construir.", "Lucas 14:28"),
        ("Justiça", "Dar a cada um o que é devido, começando pela verdade.", "Miquéias 6:8"),
        ("Fortaleza", "Continuar quando dói.", "Josué 1:9"),
        ("Coragem", "Fazer com medo.", "Ester 4:14"),
        ("Alegria", "Força que não depende do dia.", "Neemias 8:10"),
        ("Paz", "Mente firme em Deus no meio do barulho.", "Isaías 26:3"),
        ("Paciência", "Esperar sem azedar.", "Provérbios 16:32"),
        ("Benignidade", "Gentileza que age.", "Efésios 4:32"),
        ("Bondade", "Fazer o bem sem plateia.", "Gálatas 6:9-10"),
        ("Fidelidade", "Fazer no escuro o que prometeu na luz.", "Lucas 16:10"),
        ("Mansidão", "Força sob controle.", "Mateus 11:29"),
        ("Misericórdia", "Perdoar como foi perdoada.", "Colossenses 3:12-13"),
        ("Humildade", "Se ver do tamanho certo.", "Filipenses 2:3"),
    ],
    "fruto": "Mas o fruto do Espírito é: amor, gozo, paz, longanimidade, benignidade, bondade, fé, mansidão, temperança.",
    "fruto_ref": "Gálatas 5:22-23",
    "pergunta": "Das virtudes acima, marque as três que você mais precisa hoje. Escreva por quê:",
}

FEMINILIDADE = {
    "titulo": "Feminilidade",
    "intro": "Feminilidade não é cor de rosa, voz fina nem fraqueza. Provérbios 31 descreve uma mulher que compra campo, negocia, trabalha de madrugada, fortalece os braços e ri do dia de amanhã. E o texto resume tudo em uma frase: força e dignidade são as suas vestes. Ser feminina é ser forte do jeito que Deus desenhou. Sem virar homem pra ser respeitada e sem virar boneca pra ser amada.",
    "versiculos": [
        ("A força e a dignidade são os seus vestidos, e ri-se do dia futuro. Abre a sua boca com sabedoria, e a lei da beneficência está na sua língua.", "Provérbios 31:25-26"),
        ("O incorruptível traje de um espírito manso e quieto, que é precioso diante de Deus.", "1 Pedro 3:4"),
        ("Enganosa é a graça e vã a formosura, mas a mulher que teme ao Senhor, essa será louvada.", "Provérbios 31:30"),
    ],
    "mulheres_titulo": "Mulheres que não foram tolas",
    "mulheres": [
        ("Rute", "Fidelidade que muda uma linhagem inteira.", "Rute 1 a 4"),
        ("Ester", "Coragem pra um tempo como este.", "Ester 4"),
        ("Maria", "Obediência sem entender tudo.", "Lucas 1"),
        ("Ana", "Oração que insiste até Deus responder.", "1 Samuel 1"),
        ("Débora", "Sabedoria que lidera sem perder a mansidão.", "Juízes 4"),
        ("Abigail", "Prudência que evita uma tragédia.", "1 Samuel 25"),
        ("Lídia", "Trabalho e hospitalidade que abrem uma igreja.", "Atos 16"),
        ("Maria de Betânia", "Prioridade: escolheu a boa parte.", "Lucas 10"),
    ],
    "pergunta": "O que é ser feminina, pra você, hoje? E o que você acha que Deus quer mudar nessa resposta?",
}

AUTOCONHECIMENTO = {
    "titulo": "Autoconhecimento",
    "versiculo": "Sonda-me, ó Deus, e conhece o meu coração; prova-me, e conhece os meus pensamentos.",
    "ref": "Salmo 139:23",
    "intro": "Responda com honestidade. Ninguém vai ler além de você e de Deus, e Ele já sabe. Quanto mais verdade aqui, mais os 100 dias funcionam.",
    "perguntas": [
        "O que mais me incomoda em mim hoje?",
        "Em que área eu tenho sido tola (o que eu sei que devia fazer e não faço)?",
        "Por que eu quero me tornar uma mulher virtuosa? Qual é o motivo de verdade?",
        "Por que isso importa diante de Deus?",
        "Como essa mudança afeta meus relacionamentos, minha vida financeira e meus sonhos?",
        "O que eu sinto que Deus vem falando comigo e eu tenho adiado?",
    ],
}

PROPOSITO = {
    "titulo": "Propósito",
    "versiculo": "Muitos propósitos há no coração do homem, porém o conselho do Senhor permanecerá.",
    "ref": "Provérbios 19:21",
    "intro": "Propósito dá direção. Sem ele, meta vira lista solta e todo dia parece igual. E aqui vai o alívio: propósito não precisa ser extraordinário. Pode ser cuidar bem da sua casa, ser uma filha melhor, ajudar uma amiga, pregar pros seus filhos, pra sua sala de aula, pra sua faculdade. Deus prepara boas obras específicas pra cada uma. O ordinário feito com fidelidade é o extraordinário de Deus.",
    "perguntas": [
        "O que queima no meu coração e não sai da minha cabeça?",
        "Quem são as pessoas que Deus já colocou perto de mim (família, amigas, trabalho, igreja)? O que elas precisam?",
        "O que eu faço bem e que abençoa outras pessoas, mesmo que pareça pequeno?",
        "Se eu vivesse os próximos 100 dias com fidelidade total, o que mudaria pra quem está ao meu redor?",
    ],
    "frase": "Meu propósito, em uma frase (rascunho, pode mudar até o dia 100):",
    "versiculo2": "Porque somos feitura sua, criados em Cristo Jesus para as boas obras, as quais Deus preparou para que andássemos nelas.",
    "ref2": "Efésios 2:10",
}

LIMITES = {
    "titulo": "Limites e princípios",
    "intro": "Mulher sem limite claro aceita qualquer coisa e depois se pergunta como chegou ali. Escreva aqui, antes que a situação apareça, o que você aceita, o que não aceita e o que oferece. Princípio decidido com a cabeça fria segura você quando o coração esquenta.",
    "versiculos": [
        ("Andarão dois juntos, se não estiverem de acordo?", "Amós 3:3"),
        ("Não vos prendais a um jugo desigual com os infiéis.", "2 Coríntios 6:14"),
        ("Não acordeis nem desperteis o amor, até que ele o queira.", "Cânticos 8:4"),
        ("O que anda com os sábios ficará sábio, mas o companheiro dos tolos sofrerá severamente.", "Provérbios 13:20"),
    ],
    "areas": [
        ("Relacionamento amoroso", "Solteira, namorando, noiva ou casada: o que você espera, o que não negocia, o que você entrega."),
        ("Amizades", "Quem te aproxima de Deus e quem te afasta. O que você aceita e o que não aceita mais."),
        ("Família", "Como você quer tratar e ser tratada. Onde precisa de mais paciência e onde precisa de mais firmeza."),
    ],
    "colunas": ["Eu aceito", "Eu não aceito", "Eu ofereço"],
}

REGRAS = {
    "titulo": "As regras da virtuosa",
    "intro": "Regras práticas, inegociáveis, pra 100 dias. Aqui vão dez sugestões. Risque as que não fazem sentido pra você e escreva as suas. O que importa é que sejam claras e que você cumpra.",
    "lista": [
        "2 litros de água por dia. Garrafa na mesa, sempre.",
        "Celular fora do quarto. Despertador de verdade.",
        "Primeira hora do dia sem tela. Deus fala antes do mundo.",
        "Palavra e oração no mesmo horário, todo dia. Dez minutos já valem.",
        "Corpo em movimento pelo menos 4 vezes por semana.",
        "Uma fruta por dia antes de qualquer doce.",
        "Dormir no horário combinado. Deitar de verdade.",
        "Nenhuma palavra sobre quem não está presente.",
        "Contar até dez antes de responder o que irrita.",
        "Anotar cada gasto. Sem exceção.",
    ],
    "minhas": "Minhas regras (as que eu não vou negociar por 100 dias):",
    "versiculo": "Portanto, quer comais quer bebais, ou façais outra qualquer coisa, fazei tudo para glória de Deus.",
    "ref": "1 Coríntios 10:31",
}

QUADRO_SONHOS = {
    "titulo": "Quadro dos sonhos de 100 dias",
    "versiculo": "Escreve a visão e torna bem legível sobre tábuas, para que a possa ler o que correndo passa.",
    "ref": "Habacuque 2:2",
    "intro": "A regra é uma só: tem que caber em 100 dias. Nada de 'ser uma mulher melhor'. Escreva coisas que dá pra medir: 'ler a Bíblia 90 dias de 100', 'treinar 3 vezes por semana', 'guardar 500 reais', 'terminar o curso', 'fazer as pazes com minha irmã'. Meta que não se mede não se cumpre.",
    "areas": [
        ("Corpo", "salvia"),
        ("Mente", "dourado"),
        ("Espírito", "rubi"),
        ("Relacionamentos", "ameixa"),
        ("Casa e finanças", "salvia"),
        ("Propósito e chamado", "dourado"),
    ],
    "campos": ["Minha meta (mensurável)", "Como vou saber que cheguei"],
}

CARTA_FUTURO = {
    "titulo": "Carta pra mim, no dia 100",
    "intro": "Escreva pra mulher que vai abrir esta página daqui a 100 dias. Conte como você está hoje, o que dói, o que você espera, o que quer que ela tenha se tornado. Feche a página, dobre o canto e só abra no dia 100.",
    "cabecalho": "Para: eu, no dia 100",
    "rodape": "Dobre este canto. Abrir só no dia 100.",
}

RETRATO = {
    "titulo_dia1": "Retrato do dia 1",
    "titulo_dia100": "Retrato do dia 100",
    "intro_dia1": "Uma foto honesta de onde você está hoje. Sem enfeitar. No dia 100 você volta aqui e compara.",
    "intro_dia100": "Volte ao retrato do dia 1 e preencha este lado a lado. Não é sobre nota alta. É sobre ver onde Deus trabalhou.",
    "areas": [
        "Água e alimentação", "Sono", "Treino e movimento", "Leitura e foco",
        "Domínio próprio", "Vida de oração", "Leitura da Palavra", "Relacionamentos",
        "Casa e finanças", "Propósito claro",
    ],
    "medidas": [
        "Copos de água por dia", "Horas de sono por noite", "Dias de treino por semana",
        "Minutos com Deus por dia", "Livros lidos nos últimos 3 meses", "Peso (opcional)",
    ],
    "palavras": "Como eu me sinto hoje, em três palavras:",
    "incomodo": "O que mais me incomoda hoje:",
    "dia100_mudou": "O que mais mudou em mim:",
    "dia100_deus": "O que Deus fez que eu nem pedi:",
}

MAPA = {
    "titulo": "O mapa dos 100 dias",
    "intro": "Quatro fases, dez blocos, cem dias. Cada bloco treina uma virtude. Cada fase tem um objetivo. Marque cada bloco ao terminar.",
}

TRACKER_HABITOS = [
    "Água (2L)", "Movimento", "Comida de verdade", "Sono (7h+)", "Leitura",
    "Palavra", "Oração", "Sem tela na 1ª hora", "Desafio do dia", "Meu hábito: ______",
]

CHECKLIST = {
    "corpo": ["Bebi 2 litros de água", "Movi o corpo", "Comi de verdade e uma fruta", "Dormi 7 horas ou mais"],
    "mente": ["Li pelo menos 10 minutos", "Sem tela na primeira hora", "Controlei um pensamento ruim"],
    "espirito": ["Orei", "Li a Palavra", "Obedeci em uma coisa que Deus pediu"],
}

REVISAO = {
    "titulo": "Revisão do bloco",
    "perguntas": [
        ("O que melhorou nestes 10 dias?", 3),
        ("Qual foi a maior dificuldade e o que ela me mostrou?", 3),
        ("Onde a virtude deste bloco apareceu? E onde faltou?", 3),
        ("O que eu levo pro próximo bloco?", 2),
        ("Uma conversa com Deus sobre esses dias:", 4),
    ],
    "notas": ["Corpo", "Mente", "Espírito", "Virtude do bloco"],
}

FECHAMENTO = {
    "titulo": "E agora?",
    "versiculo": "Tendo por certo isto mesmo, que aquele que em vós começou a boa obra a aperfeiçoará até ao dia de Jesus Cristo.",
    "ref": "Filipenses 1:6",
    "paragrafos": [
        "Cem dias. Você chegou. Talvez não com o checklist perfeito, talvez com mais X do que gostaria. Não importa. Você abriu este caderno cem vezes. Isso é fidelidade, e fidelidade é a virtude que sustenta todas as outras.",
        "Agora olhe o retrato do dia 1 e o do dia 100 lado a lado. Veja o que mudou. Não só os números. Veja como você responde, como você dorme, como você fala com Deus e com as pessoas. Isso é o que Ele fez, com a sua mão na dele.",
        "O que virou hábito fica. O que ainda não virou entra nos próximos 100 dias. Porque sim, existe um próximo. Escolha novas metas, novas regras, novos versículos. Imprima de novo. Comece de novo. A mulher virtuosa não é a que chegou. É a que não para.",
    ],
    "proximos_titulo": "Meus próximos 100 dias começam em:",
    "proximos": [
        "As três metas que ficam:",
        "As três metas novas:",
        "A virtude que mais preciso treinar de novo:",
        "Uma mulher que eu vou convidar pra fazer a jornada comigo:",
    ],
    "comunidade": "Você não foi feita pra caminhar sozinha. Compartilhe o que mudou, o que foi difícil, o que Deus fez. Convide uma amiga. Virtude se espalha por contágio.",
}

CONTRACAPA = {
    "versiculo": "Dai-lhe do fruto das suas mãos, e louvem-na nas portas as suas obras.",
    "ref": "Provérbios 31:31",
}

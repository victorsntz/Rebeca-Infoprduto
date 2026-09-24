// Configuração da área de membros.
// Deixe SUPABASE_URL vazio pra rodar em modo demonstração (tudo salvo só neste navegador).
// Com URL e chave preenchidas, o app usa login de verdade e salva o progresso na nuvem.
window.DTV_CONFIG = {
  SUPABASE_URL: "https://stcskyelzuynfnmdrnth.supabase.co",
  SUPABASE_ANON_KEY: "sb_publishable_qRZtPer3nwwQqo3J-T2qPQ_yLJpGDQv",

  // Vídeos (YouTube ou Vimeo). Pode colar o link normal do vídeo, o app converte pro player.
  VIDEOS: {
    aula_inaugural: "https://youtu.be/kUP5Hm-PTVw",
    conhecendo_caderno: "",
    como_imprimir: "",
    como_usar_site: "",
  },

  // Link do PDF pra download dentro da área de membros.
  PDF_URL: "../dist/de-tola-a-virtuosa.pdf",   // no site publicado os PDFs ficam em detolaavirtuosa/dist/

  // Link do checkout, usado quando a assinatura está inativa.
  CHECKOUT_URL: "https://pay.kiwify.com.br/6IGmfcv",

  // Link do checkout do produto "Presentear uma amiga" (R$ 27), pra comprar depois e quantas vezes quiser.
  // Vazio esconde o botão de comprar dentro do app.
  GIFT_CHECKOUT_URL: "https://pay.kiwify.com.br/l2of2hZ",
  GIFT_PRICE: "R$ 27",

  // Suporte
  SUPORTE_EMAIL: "contato@detolaavirtuosa.com",
};

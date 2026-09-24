// Configuração da área de membros.
// Deixe SUPABASE_URL vazio pra rodar em modo demonstração (tudo salvo só neste navegador).
// Com URL e chave preenchidas, o app usa login de verdade e salva o progresso na nuvem.
window.DTV_CONFIG = {
  SUPABASE_URL: "https://stcskyelzuynfnmdrnth.supabase.co",
  SUPABASE_ANON_KEY: "sb_publishable_qRZtPer3nwwQqo3J-T2qPQ_yLJpGDQv",

  // Vídeos (YouTube ou Vimeo). Cole só o ID ou a URL de embed.
  VIDEOS: {
    aula_inaugural: "",   // ex.: "https://www.youtube.com/embed/XXXXXXXX"
    como_imprimir: "",
    como_usar_site: "",
  },

  // Link do PDF pra download dentro da área de membros.
  PDF_URL: "../dist/de-tola-a-virtuosa.pdf",   // no site publicado os PDFs ficam em detolaavirtuosa/dist/

  // Link do checkout, usado quando a assinatura está inativa.
  CHECKOUT_URL: "https://pay.kiwify.com.br/6IGmfcv",

  // Suporte
  SUPORTE_EMAIL: "contato@detolaavirtuosa.com",
};

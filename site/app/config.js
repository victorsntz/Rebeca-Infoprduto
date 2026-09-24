// Configuração da área de membros.
// Deixe SUPABASE_URL vazio pra rodar em modo demonstração (tudo salvo só neste navegador).
// Com URL e chave preenchidas, o app usa login de verdade e salva o progresso na nuvem.
window.DTV_CONFIG = {
  SUPABASE_URL: "",
  SUPABASE_ANON_KEY: "",

  // Vídeos (YouTube ou Vimeo). Cole só o ID ou a URL de embed.
  VIDEOS: {
    aula_inaugural: "",   // ex.: "https://www.youtube.com/embed/XXXXXXXX"
    como_imprimir: "",
    como_usar_site: "",
  },

  // Link do PDF pra download dentro da área de membros.
  PDF_URL: "../../dist/de-tola-a-virtuosa.pdf",

  // Link do checkout, usado quando a assinatura está inativa.
  CHECKOUT_URL: "",

  // Turma ao vivo (extra): link do grupo no WhatsApp e dos encontros. Só aparece pra quem comprou a turma.
  COMUNIDADE_URL: "",       // ex.: "https://chat.whatsapp.com/XXXXXXXX"
  ENCONTROS_URL: "",        // ex.: link fixo do Meet/Zoom, ou uma página com a agenda
  ENCONTROS_INFO: "Toda quarta, 20h, ao vivo. O link fica aqui e no grupo.",

  // Suporte
  SUPORTE_EMAIL: "contato@rebecafortunato.com",
};

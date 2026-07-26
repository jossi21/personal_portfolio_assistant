export type Language =
  | "English"
  | "አማርኛ"
  | "tትግርኛi"
  | "Afaan Oromoo"
  | "Soomaali";

export const languages = [
  {
    code: "English",
    name: "English",
  },
  {
    code: "አማርኛ",
    name: "አማርኛ",
  },
  {
    code: "ትግርኛ",
    name: "ትግርኛ",
  },
  {
    code: "Afaan Oromoo",
    name: "Afaan Oromo",
  },
  {
    code: "Soomaali",
    name: "Somali",
  },
] as const;

export type ActionType = "link" | "button" | "language" | "redirect";

export interface Action {
  label: string;
  type: ActionType;
  value: string;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  actions?: Action[];
}

export interface ChatRequest {
  session_id?: string;
  message: string;
}

export interface ChatResponse {
  session_id: string;
  answer: string;
  actions?: Action[];
  language?: Language;
}

export interface LanguageResponse {
  session_id: string;
  language: Language;
}

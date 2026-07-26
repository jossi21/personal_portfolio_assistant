"use client";

import { Language } from "@/types/chat";

interface Props {
  currentLanguage: Language;

  onChange: (language: Language) => void;
}

export default function LanguageSelector({ currentLanguage, onChange }: Props) {
  const languages = [
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
      name: "Afaan Oromoo",
    },
    {
      code: "Soomaali",
      name: "Soomaali",
    },
  ];

  return (
    <select
      value={currentLanguage}
      onChange={(e) => onChange(e.target.value as Language)}
      className="
border
rounded-lg
p-2
"
    >
      {languages.map((lang) => (
        <option key={lang.code} value={lang.code}>
          {lang.name}
        </option>
      ))}
    </select>
  );
}

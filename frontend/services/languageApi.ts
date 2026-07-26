import { Language, ChatResponse } from "@/types/chat";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function changeLanguage(
  session_id: string,
  language: Language,
): Promise<ChatResponse> {
  const response = await fetch(`${API_URL}/language`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      session_id,
      language,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to change language");
  }

  return response.json();
}

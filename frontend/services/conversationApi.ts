import { ChatMessage } from "@/types/chat";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getConversation(sessionId: string) {
  const response = await fetch(`${API_URL}/conversation/${sessionId}`);

  if (!response.ok) {
    throw new Error("Failed to load conversation");
  }

  return response.json();
}

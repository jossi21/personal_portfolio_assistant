import { ChatRequest, ChatResponse } from "@/types/chat";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function sendMessage(data: ChatRequest): Promise<ChatResponse> {
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  return response.json();
}

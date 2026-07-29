# from fastapi import APIRouter, Depends, Query
# from fastapi.responses import PlainTextResponse

# from app.services.channel_gateway import ChannelGateway
# from app.core.dependencies import get_channel_gateway
# from app.services.whatsapp_service import WhatsAppService
# from app.core.config import settings


# router = APIRouter(
#     prefix="/whatsapp",
#     tags=["WhatsApp"]
# )


# whatsapp_service = WhatsAppService()


# # Meta webhook verification
# @router.get("/webhook")
# def verify_whatsapp_webhook(
#     mode: str = Query(alias="hub.mode"),
#     token: str = Query(alias="hub.verify_token"),
#     challenge: str = Query(alias="hub.challenge"),
# ):

#     print("MODE:", mode)
#     print("TOKEN:", token)
#     print("CHALLENGE:", challenge)

#     if mode == "subscribe" and token == settings.verify_token:
#         print("✅ WHATSAPP VERIFIED")
#         return PlainTextResponse(
#             content=challenge,
#             status_code=200
#         )

#     print("❌ WHATSAPP FAILED")

#     return PlainTextResponse(
#         "Verification failed",
#         status_code=403
#     )


# # Receive WhatsApp messages
# @router.post("/webhook")
# def whatsapp_webhook(
#     data: dict,
# ):

#     print("============================")
#     print("INCOMING WHATSAPP MESSAGE")
#     print(data)
#     print("============================")

#     return {
#         "status": "received"
#     }
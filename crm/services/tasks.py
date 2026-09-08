from celery import shared_task

@shared_task
def processar_mensagem_assincrona(mensagem):
    print(f"Mensagem processada: {mensagem}")

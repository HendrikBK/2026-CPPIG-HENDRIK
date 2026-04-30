from datetime import timedelta

from apscheduler.schedulers.background import BackgroundScheduler

from django.utils import timezone

from reservas.models import Reserva


def job():
    reservas = Reserva.objects.filter(ativo=True)
    for reserva in reservas:
        if timezone.now() - reserva.inicio > timedelta(minutes=15):
            reserva.ativo = False
            reserva.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'cron', minute='*/15')
    scheduler.start()
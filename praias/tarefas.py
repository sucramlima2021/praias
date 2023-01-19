from django_cron import CronJobBase, Schedule
from praias.atualizacao import *

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'praia.tarefas.my_cron_job'    # a unique code

    def do(self):
        if atualiza():
            pass
        else: print('falha na atualização') 
        if atualiza2():
            pass
        else: print('falha na atualização 2')
        if atualiza3():
            pass
        else: print('falha na atualização 3')
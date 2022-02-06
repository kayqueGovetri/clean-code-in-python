# Para tirar proveito do seu editor de código é interessante criar nomes que seja facilmente pesquisado.
# O tamanho de um nome deve ser proporcional a seu escopo, se ela pode ser vista ou usada em varios lugares
# é imperativo atribui-la um nome fácil.

# Compare

s = 0
t = [i for i in range(0, 100)]
for j in range(0, 100):
    s += (t[j]*4)/5


real_days_per_ideal_day = 4
WORK_DAYS_PER_WEEK = 5
task_estimate = [i for i in range(0, WORK_DAYS_PER_WEEK)]
total = 0
for j in range(0, WORK_DAYS_PER_WEEK):
    real_task_day = task_estimate[j] * real_days_per_ideal_day
    real_task_weeks = (real_task_day / WORK_DAYS_PER_WEEK)
    total += real_task_weeks



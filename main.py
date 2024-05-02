from crewai import Crew, Process
from tasks import GameTasks
from agents import GameAgents

agents = GameAgents()
tasks = GameTasks()

# Criar Agents
pesquisador = agents.pesquisador_agent()
esbocador = agents.esbocador_agent()
copywriter = agents.copywriter_agent()
revisor = agents.revisor_agent()

# Criar Tasks
pesquisar = tasks.pesquisar_task(pesquisador)
esbocar = tasks.esbocar_task(esbocador, [pesquisar])
redigir = tasks.redigir_task(copywriter, [esbocar])
revisar = tasks.revisar_task(revisor, [redigir])

# Configurar crew
crew = Crew(
    agents=[pesquisador, esbocador, copywriter, revisor],
    tasks=[pesquisar, esbocar, redigir, revisar],
    process=Process.sequential,
    verbose=2
)

# Iniciar e printar relatório
result = crew.kickoff()
print('Relatório:')
print(result)

from crewai import Task


class GameTasks():
    def pesquisar_task(self, agent):
        return Task(
            description="Coletar informações sobre temas atuais e populares no mercado de jogos. Participar e documentar reuniões de brainstorming para gerar ideias inovadoras para histórias e personagens",
            agent=agent,
            async_execution=True,
            expected_output="Relatório contendo tendências de mercado, insights do consumidor e uma lista preliminar de temas e arquétipos de personagens para desenvolvimento futuro"
        )

    def esbocar_task(self, agent, context):
        return Task(
            description="Desenvolver um esboço detalhado da narrativa principal e das subtramas. Criar descrições detalhadas dos personagens principais e secundários, incluindo suas motivações e arcos de desenvolvimento",
            agent=agent,
            context=context,
            async_execution=True,
            expected_output="Documento com a estrutura completa da história e perfis detalhados dos personagens, pronto para revisão"
        )

    def redigir_task(self, agent, context):
        return Task(
            description="Escrever diálogos detalhados e descrições de cenas que complementam a narrativa principal. Colaborar com artistas para garantir que a visualização dos personagens esteja em harmonia com o roteiro",
            agent=agent,
            context=context,
            async_execution=True,
            expected_output="""
            Documento de roteiros detalhados que inclui:
            1) Diálogos: Textos completos e detalhados para cada cena, refletindo a voz e a evolução dos personagens ao longo do jogo.
            2) Descrições de Cenas: Descrições vívidas e envolventes de cada cena, incluindo ambientes, ações e interações chave entre personagens.
            3) Coordenação Visual: Propostas de design visual dos personagens e cenas, alinhadas com os diálogos e ações descritas, preparadas em colaboração com a equipe de artistas.
            4) Revisões Preliminares: Inclusão de feedbacks iniciais sobre os diálogos e designs para ajustes necessários antes da revisão final.
            Este documento deve fornecer uma base sólida para a avaliação e feedback final, garantindo que todos os aspectos da narrativa e visualização estejam em perfeita sincronia.
            """
        )

    def revisar_task(self, agent, context):
        return Task(
            description="Analisar feedback interno e externo sobre o roteiro e designs dos personagens. Implementar ajustes necessários para melhorar a coesão e impacto da história e visual dos personagens. Garantir que todos os elementos estão alinhados com a visão criativa do jogo.",
            agent=agent,
            context=context,
            expected_output="""
            Documento final revisado que inclui:
            1) Narrativa Completa: Detalhamento da trama principal, subtramas, e a história escrita por completo, incluindo diálogos e descrições detalhadas das cenas.
            2) Personagens: Descrições completas e detalhadas de todos os personagens principais e secundários, incluindo suas motivações, histórias de fundo e evolução ao longo do jogo.
            3) Diálogos e Cenas: Diálogos finais e descrições detalhadas das cenas que complementam a narrativa.
            4) Designs de Personagens: Designs finais de personagens, incluindo visualizações e especificações artísticas.
            5) Integração com Jogabilidade: Resumo de como a história e os elementos de design se integram com a mecânica e jogabilidade do jogo.
            Este documento deve estar formatado para facilitar a implementação pelos desenvolvedores, com clareza na especificação de elementos interativos e interfaces necessárias para a programação.
            """
        )

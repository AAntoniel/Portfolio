import streamlit as st

lang = st.sidebar.radio("Language / Idioma", ["EN-US", "PT-BR"])

if lang == "EN-US":
    st.title("About me")

    # -- About me section --
    st.write(
        """
        My name is Antoniel Kleber Stefaniak. I was born in 2001 and have been passionate about technology for as long as I can remember. This lifelong interest has shaped me 
        into a dedicated, data-driven professional who values precision and continuous growth.
        
        #### 🎸Beyond the code
        
        When I’m not at my desk working with data or developing software, I find balance through creative and technical hobbies that keep my mind active. I am a passionate 
        music enthusiast and a collector of CDs and LPs. Beyond listening, I dedicate time to studying music theory and practicing the electric guitar.
        
        I am also currently learning how to draw. This helps me develop a sharper eye for detail and provides a creative outlet that contrasts with my technical work.
        
        As someone who values a focused and calm environment, I spend much of my free time immersed in books. Whether it's fiction or technical literature, reading 
        is my favorite way to explore new perspectives.
        
        In the next sections, you can find more information about me, my academic background, work experiences and technical skills. 
        """
    )

    # -- Graduation section --
    st.write("#### 🎓Academic Background")
    col1, col2 = st.columns(2)

    with st.container(border=True):
        st.markdown("##### **Master with specialization in Applied AI** | UFSC (2025)")
        st.write("**Research focus on Applied Artificial Intelligence.**")
        st.write("Focused on advanced predictive modeling and time series analysis.")

    with st.container(border=True):
        st.markdown("##### **Bachelor in Software Engineering** | Ugv (2022)")
        st.write("Core training in software architecture and system development.")


    # -- Professional experience section --
    st.write("#### 💼Professional Experience")

    col_a, col_b = st.columns(2)

    with col_a:
        with st.container(border=True, height=250):  # Fixed height keeps boxes aligned
            st.markdown("##### **Data Analysis and Data Scientist**")
            st.write("**Whirlpool | 2025 - Current**")
            st.write(
                """
            - Maintained and enhanced company cost reduction systems.
            - Implemented analytical and AI solutions, optimizing processes and increasing operational efficiency.
            - Generated strategic insights through data analysis, supporting executive decision-making.
            - Introduced automation tools for critical tasks, significantly optimizing execution time. 
            """
            )

    with col_b:
        with st.container(border=True, height=250):
            st.markdown("##### **Teaching Assistantship**")
            st.write("**UFSC | 2024**")
            st.write(
                """
            - Developed and delivered lectures on statistical methods.
            - Taught an introduction to time series analysis: characteristics, components and fundamental concepts.
            - Covered forecasting models, including ARIMA and its extensions.
            - Led a case study focusing on stock market applications.
            """
            )

    col_a, col_b = st.columns(2)

    with col_a:
        with st.container(border=True, height=250):  # Fixed height keeps boxes aligned
            st.markdown("##### **IT Intern and Support Specialist**")
            st.write("**Intellectual Distribution Center (CDI)| 2021 - 2022**")
            st.write(
                """
            - Assisted with computer hardware configuration and general IT department routines.
            - Supported operating system and network configuration.
            - Managed software installation, monitoring and regular data backups.
            - Provided technical support in the computer lab.
            """
            )


    # -- Key project section --
    st.write(
        """   
        #### 📜**Research & Publications**
        
        A key project of my career was my Master’s research, where I developed a comparative research using Classical Statistical models, Machine Learning, 
        and Large Language Models (LLMs) to forecast water demand in a coastal tourist city in Brazil. I am proud to share that a portion of this research was 
        accepted and published by Springer Nature for the BRACIS 2024 conference.
        
        *Link*: Stefaniak, A.K., et al. (2025). "A Case Study on Water Demand Forecasting in a Coastal Tourist City." Intelligent Systems. BRACIS 2024. Springer, Cham. https://doi.org/10.1007/978-3-031-79035-5_1
        """
    )

    st.write("#### 🛠️Technical Skills")

    cols = st.columns(4)

    with cols[0]:
        # Python
        with st.container(border=True):
            st.image(
                "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
            )
            st.write("Python")

    with cols[1]:
        # Sheets
        with st.container(border=True):
            st.image("https://www.svgrepo.com/show/223056/sheets-sheet.svg")
            st.write("Excel/GoogleSheets")


    with cols[2]:
        # lookerstudio
        with st.container(border=True):
            st.image("https://www.svgrepo.com/show/354012/looker-icon.svg")
            st.write("LookerStudio")


    with cols[3]:
        # Git
        with st.container(border=True):
            st.image(
                "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg"
            )
            st.write("Git/GitHub")

    st.write("#### 📚Currently studying")

    cols = st.columns(4)

    with cols[0]:
        # SQL
        with st.container(border=True):
            st.image(
                "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg"
            )
            st.write("SQL")

    with cols[1]:
        # Stats.
        with st.container(border=True):
            st.image("https://www.svgrepo.com/show/292706/statistics-graph.svg")
            st.write("Statistics")

    st.write(
        """
        #### **🚀Explore My Portfolio**
        
        Beyond my academic research, I enjoy applying data science to diverse real-world challenges. This portfolio features projects that span the entire data lifecycle, from 
        in-depth statistical analysis to building and deploying functional applications for real-world usage. I invite you to explore my work through the menu on the side.
    """
    )

    st.markdown("---")
    st.write("### 📫 Contact & Socials")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        # LinkedIn
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://www.linkedin.com/in/antoniel-k-stefaniak/" target="_blank">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="50">
                </a>
                <p style="margin-bottom: 0px; margin-top: 10px;">Linkedin</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        # GitHub
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://github.com/AAntoniel" target="_blank">
                    <img src="https://www.svgrepo.com/show/439171/github.svg" width="50" style="filter: invert(100%) if_dark_mode;">
                </a>
                <p style="margin-bottom: 0px; margin-top: 10px;">GitHub</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        # Email
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="50">
                <p style="margin-bottom: 0px; margin-top: 10px;">E-mail</p>
                <p style="font-size: 16px;">antonielstefaniak@gmail.com</p>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.title("Sobre mim")

    # -- About me section --
    st.write(
        """
        Meu nome é Antoniel Kleber Stefaniak. Nasci em 2001 e sou apaixonado por tecnologia desde que me conheço por gente. Esse interesse de longa data me moldou como um 
        profissional dedicado e orientado a dados, que valoriza a precisão e o crescimento contínuo.

        #### 🎸Além do código

        Quando não estou na minha mesa trabalhando com dados ou desenvolvendo alguma coisa, gosto de passar meu tempo com hobbies criativos e técnicos que mantêm minha mente ativa. 
        Sou apaixonado por música, e, por isso, coleciono CDs e LPs. Além de ouvir, estudo teoria musical e pratico guitarra.

        Também estou aprendendo a desenhar, pois isso ajuda a desenvolver um olhar mais atento aos detalhes, algo fundamental na área de dados, além de oferecer
        uma válvula de escape criativa. 
        
        Outro hobby que aprecio muito é a leitura. Seja através da ficção ou da literatura técnica, ler é a minha maneira preferida de descobrir novos pontos de vista e expandir 
        horizontes.

        Nas próximas seções, você pode encontrar mais informações sobre mim, minha formação acadêmica, experiências profissionais e habilidades técnicas.
        """
    )

    # -- Graduation section --
    st.write("#### 🎓Formação Acadêmica")
    col1, col2 = st.columns(2)

    with st.container(border=True):
        st.markdown("##### **Mestrado em Engenharia de Sistemas Eletrônicos** | UFSC (2025)")
        st.write("**Linha de pesquisa em Inteligência Artificial Aplicada.**")
        st.write("Especializado em modelagem preditiva e análise de séries temporais.")

    with st.container(border=True):
        st.markdown("##### **Bacharelado em Engenharia de Software** | Ugv (2022)")
        st.write("Base técnica centrada em arquitetura de software e desenvolvimento de sistemas.")

    # -- Professional experience section --
    st.write("#### 💼Experiência Profissional")

    col_a, col_b = st.columns(2)

    with col_a:
        with st.container(border=True, height=250):  # Fixed height keeps boxes aligned
            st.markdown("##### **Analista e Cientista de Dados**")
            st.write("**Whirlpool | 2025 - Current**")
            st.write(
                """
            - Manutenção e aprimoramento nos sistemas de redução de custo da companhia.
            - Implementação de soluções analíticas e de IA, otimizando processos e aumentando a eficiência operacional.
            - Geração de insights estratégicos a partir da análise de dados, auxiliando a tomada de decisão.
            - Introdução de ferramentas de automação para tarefas críticas, otimizando o tempo de execução.
            """
            )

    with col_b:
        with st.container(border=True, height=250):
            st.markdown("##### **Estágio de Docência**")
            st.write("**UFSC | 2024**")
            st.write(
                """
            - Elaboração e aplicação de aulas sobre modelos estatísticos.
            - Introdução à análise de séries temporais: características, componentes e conceitos fundamentais.
            - Modelos de previsão: ARIMA e suas extensões.
            - Estudo de caso aplicado a bolsa de valores.
            """
            )

    col_a, col_b = st.columns(2)

    with col_a:
        with st.container(border=True, height=250):  # Fixed height keeps boxes aligned
            st.markdown("##### **Estagiário e suporte de TI**")
            st.write("**Centro de Distribuição Intelectual (CDI) | 2021 - 2022**")
            st.write(
                """
            - Auxiliar na configuração de hardware de computadores e nas rotinas gerais da área de TI.
            - Auxiliar na configuração do sistema operacional e rede.
            - Instalação/Acompanhamento de softwares e backups.
            - Auxiliar no laboratório de informática.
            """
            )

    # -- Key project section --
    st.write(
        """   
        #### 📜**Pesquisas & Publicações**

        Um projeto fundamental na minha carreira foi minha pesquisa de mestrado, onde desenvolvi um estudo comparativo utilizando modelos estatísticos clássicos, machine learning 
        e modelos pré-treinados de larga escala (LLMs) para prever a demanda de água em uma cidade turística litorânea no Brasil. Tenho orgulho em compartilhar que parte desta pesquisa 
        foi aceita e publicada pela Springer Nature para a conferência BRACIS 2024.

        *Link*: Stefaniak, A.K., et al. (2025). "A Case Study on Water Demand Forecasting in a Coastal Tourist City." Intelligent Systems. BRACIS 2024. Springer, Cham. https://doi.org/10.1007/978-3-031-79035-5_1
        """
    )

    st.write("#### 🛠️Competências Técnicas")

    cols = st.columns(4)

    with cols[0]:
        # Python
        with st.container(border=True):
            st.image(
                "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
            )
            st.write("Python")

    with cols[1]:
        # Sheets
        with st.container(border=True):
            st.image("https://www.svgrepo.com/show/223056/sheets-sheet.svg")
            st.write("Excel/GoogleSheets")

    with cols[2]:
        # lookerstudio
        with st.container(border=True):
            st.image("https://www.svgrepo.com/show/354012/looker-icon.svg")
            st.write("LookerStudio")

    with cols[3]:
        # Git
        with st.container(border=True):
            st.image(
                "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg"
            )
            st.write("Git/GitHub")

    st.write("#### 📚Estudando no momento")

    cols = st.columns(4)

    with cols[0]:
        # SQL
        with st.container(border=True):
            st.image(
                "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg"
            )
            st.write("SQL")

    with cols[1]:
        # Stats.
        with st.container(border=True):
            st.image("https://www.svgrepo.com/show/292706/statistics-graph.svg")
            st.write("Estatística")

    st.write(
        """
        #### **🚀Conheça meu Portfólio**

        Para além do meu background acadêmico e profissional, gosto de aplicar ciência de dados em diversos desafios do mundo real. Este portfólio apresenta projetos que abrangem
        todo o ciclo de vida dos dados: desde análises estatísticas aprofundadas até o desenvolvimento e deploy de aplicações funcionais. Convido você 
        a explorar meu trabalho através do menu lateral.
    """
    )

    st.markdown("---")
    st.write("### 📫 Contato e Redes Sociais")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        # LinkedIn
        st.markdown("""
                <div style="text-align: center;">
                    <a href="https://www.linkedin.com/in/antoniel-k-stefaniak/" target="_blank">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="50">
                    </a>
                    <p style="margin-bottom: 0px; margin-top: 10px;">Linkedin</p>
                </div>
                """,
                    unsafe_allow_html=True
                    )

    with col2:
        # GitHub
        st.markdown("""
                <div style="text-align: center;">
                    <a href="https://github.com/AAntoniel" target="_blank">
                        <img src="https://www.svgrepo.com/show/439171/github.svg" width="50" style="filter: invert(100%) if_dark_mode;">
                    </a>
                    <p style="margin-bottom: 0px; margin-top: 10px;">GitHub</p>
                </div>
                """,
                    unsafe_allow_html=True
                    )

    with col3:
        # Email
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="50">
                <p style="margin-bottom: 0px; margin-top: 10px;">E-mail</p>
                <p style="font-size: 16px;">antonielstefaniak@gmail.com</p>
            </div>
            """,
            unsafe_allow_html=True
        )
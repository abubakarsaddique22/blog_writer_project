# from agno.agent import Agent 
# from agno.models.ollama import Ollama
# from agno.team import Team
# from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.tools.hackernews import HackerNewsTools
# from agno.tools.arxiv import ArxivTools
# from agno.tools.wikipedia import WikipediaTools
# from agno.tools.youtube import YouTubeTools
# from agno.tools.newspaper4k import Newspaper4kTools
# from agno.tools.local_file_system import LocalFileSystemTools
# from pathlib import Path
# from agno.db.in_memory import InMemoryDb
# from agno.os import AgentOS

# # define the dir to save the research paper 

# dir_path = Path('./research_paper/')
# dir_path.mkdir(exist_ok=True)

# # define the dir to save the artical final output 

# target_dir_path = Path('./medium_articals/')
# target_dir_path.mkdir(exist_ok=True)

# # define db 

# db = InMemoryDb()


# # # define orchestrator and agent model

# orchestrator_model = Ollama(
#     id='deepseek-v3.1:671b-cloud',
#     host='http://localhost:11434' 
# )

# agents_model = Ollama(
#     id = 'gpt-oss:120b-cloud',
#     host='http://localhost:11434' 
# )

# # ============================================ agents ====================================================
# # define the arxive research agent 

# arxiv_research_agent = Agent(
#     id='arxiv_research_agent',
#     name = 'Arxiv_Research_Agent',
#     model=agents_model,
#     role = 'Arxiv Research Assistant',
#     instructions=[
#         "You are a research assistant that gathers research papers from Arxiv",
#         "Use the available tools to search for research papers, authors and topics as per user's request",
#         "Summarize your findings clearly and concisely"
#     ],
#     tools=[ArxivTools(download_dir=dir_path)],
#     add_datetime_to_context=True

# )


# # define the hackernews research agent

# hackernews_agent = Agent(
#     id='hackerenews_research_agent',
#     name='Hackernews_Research_Agent',
#     model = agents_model,
#     role = "Hackernews Research Assistant",
#     instructions=[
#         "You are an expert research assistant that can access HackerNews",
#         "Get relevant information for the recent topics, and get information about the articles for the topic user requested for",
#         "Summarize your findings in proper format"
#     ],
#     tools=[HackerNewsTools()],
#     add_datetime_to_context=True

# )


# # define wikipedia  research agent 


# wikipedia_agent = Agent(
#     id='wikipedia_research_agent',
#     name = "Wikipedia_Research_Agent",
#     model = agents_model,
#     role = 'Wikipedia Research Assistant',
#     instructions=[
#         "You are a research assistant that gathers information from Wikipedia based on the input topic",
#         "You have the capability to search for articles and gather its content",
#         "Summarize the findings and mention the appropriate resources and references in your output"
#     ],
#     tools=[WikipediaTools()],
#     add_datetime_to_context=True
# ) 


# # define YouTubeTools agent 
# YouTube_agent = Agent(
#     id='YouTube_research_agent',
#     name = "YouTube_Research_Agent",
#     model = agents_model,
#     role = 'Youtube Research Assistant',
#     instructions=[
#         "You are a research assistant that gathers information from Youtube",
#         "You have the capability to read youtube video transcripts and summarize them",
#         "You can also read metadata related to youtube videos",
#         "you can also fetch timestamps of a particular video",
#         "summarize the transcripts in clear and concised manner"
#     ],
#     tools=[YouTubeTools()],
#     add_datetime_to_context=True
# )


# # define research agent using newspaper4k
# new_paper_agent = Agent(
#     id='newspaper_research_agent',
#     name = "newspaper_Research_Agent",
#     model = agents_model,
#     role = 'newpaper Research Assistant',
#     instructions=[
#         "You are a research assistant that can read the contents of articles",
#         "Whenever an url is provided you can read the content of the article and can also get its data",
#         "Using the available tools search for articles and summarize them and gather relevant information"
#     ],
#     tools=[Newspaper4kTools()],
#     add_datetime_to_context=True
# )


# # define the web search agent 
# web_search_agent = Agent(
#     id="web-search-agent",
#     name="Web Search Agent",
#     role="Web Research Assistant",
#     model=agents_model,
#     instructions=["You are a research assistant that gathers information from the web",
#                 "Use the available tools to search for articles, summaries and other important material based on the topic the user requested about",
#                 "Summarize your findings along with the resource links"],
#     add_datetime_to_context=True,
#     tools=[DuckDuckGoTools()]
# )



# # ===================================== Team =======================================================
# medium_article_team = Team(
#     id="medium-article-creation-team",
#     name="Medium Article Creation Team",
#     role="Team Leader which manages research and content creation",
#     db=db,
#     members=[
#         arxiv_research_agent,
#         hackernews_agent,
#         wikipedia_agent,
#         YouTube_agent,
#         new_paper_agent,
#         web_search_agent
#         ],
#     model=orchestrator_model,
#     instructions=["You are a team leader managing multiple sub agents in your team",
#                 "You have access to agents which can do research based on the topic on various sources such as arxiv, X(formerly twitter), youtube, reddit, wikipedia, hackernews, newspaper articles, web search using google search and duckduckgo search",
#                 "you also have the capability to read and write emails",
#                 "your task is to understand the topic given by the user and fetch relevant research information using your team members",
#                 "once you have enough research material, your primary task is to create medium(platform) styled articles",
#                 "for checking how articles are written on medium you can use the article research agent",
#                 "once you have created the medium article, show the user the final draft",
#                 "only when the user confirms the draft, save it to the filesystem in a markdown format as a .md file using the filename suggested by user",
#                 "if the user does not give a filename, then use a self created name based on the topic on which the article was created"],
#     add_datetime_to_context=True,
#     add_history_to_context=True,
#     num_history_runs=10,
#     tools=[LocalFileSystemTools(target_directory=target_dir_path,
#                                 default_extension="md")],
#     stream=True,
#     markdown=True
# )




# # # ======================== AgentOS ============================

# # agent_os = AgentOS(
# #     id="medium-article-os",
# #     name="Medium Article Generator OS",
# #     description="An Agent that conducts research of latest tech topics across multiple platforms and generates medium articles based on its findings",
# #     teams=[medium_article_team]
# # )


# # # create a fastapi app
# # app = agent_os.get_app()

# # if __name__ == "__main__":
# #     agent_os.serve(
# #         app="app:app",
# #     )


# if __name__ == "__main__":
#     print("🧠 Medium Article Generator (CMD Mode)")
#     print("Type 'exit' to quit\n")

#     while True:
#         user_prompt = input(">>> ")

#         if user_prompt.lower() in ["exit", "quit"]:
#             print("👋 Exiting...")
#             break

#         print("\n⏳ Processing... Please wait...\n")

#         response = medium_article_team.run(user_prompt)

#         print("\n========== FINAL ARTICLE ==========\n")
#         print(response)
#         print("\n✅ Article process completed & saved (if confirmed)\n")



from agno.agent import Agent 
from agno.models.ollama import Ollama
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.arxiv import ArxivTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.youtube import YouTubeTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.local_file_system import LocalFileSystemTools
from pathlib import Path
from agno.db.in_memory import InMemoryDb

# ======================= Directories =========================
research_dir = Path("./research_paper/")
research_dir.mkdir(exist_ok=True)

medium_dir = Path("./medium_articals/")
medium_dir.mkdir(exist_ok=True)

# ======================== DB ================================
db = InMemoryDb()

# ======================== Models ============================
orchestrator_model = Ollama(
    id='deepseek-v3.1:671b-cloud',
    host='http://localhost:11434' 
)

agents_model = Ollama(
    id='gpt-oss:120b-cloud',
    host='http://localhost:11434' 
)

# ======================= Agents =============================
arxiv_research_agent = Agent(
    id='arxiv_research_agent',
    name='Arxiv_Research_Agent',
    model=agents_model,
    role='Arxiv Research Assistant',
    instructions=[
        "You are a research assistant that gathers research papers from Arxiv",
        "Use the available tools to search for research papers, authors and topics as per user's request",
        "Summarize your findings clearly and concisely"
    ],
    tools=[ArxivTools(download_dir=research_dir)],
    add_datetime_to_context=True
)

hackernews_agent = Agent(
    id='hackerenews_research_agent',
    name='Hackernews_Research_Agent',
    model=agents_model,
    role='Hackernews Research Assistant',
    instructions=[
        "You are an expert research assistant that can access HackerNews",
        "Get relevant information for the recent topics, and get information about the articles for the topic user requested",
        "Summarize your findings in proper format"
    ],
    tools=[HackerNewsTools()],
    add_datetime_to_context=True
)

wikipedia_agent = Agent(
    id='wikipedia_research_agent',
    name='Wikipedia_Research_Agent',
    model=agents_model,
    role='Wikipedia Research Assistant',
    instructions=[
        "You are a research assistant that gathers information from Wikipedia based on the input topic",
        "You have the capability to search for articles and gather its content",
        "Summarize the findings and mention the appropriate resources and references in your output"
    ],
    tools=[WikipediaTools()],
    add_datetime_to_context=True
) 

youtube_agent = Agent(
    id='YouTube_research_agent',
    name='YouTube_Research_Agent',
    model=agents_model,
    role='Youtube Research Assistant',
    instructions=[
        "You are a research assistant that gathers information from Youtube",
        "You have the capability to read youtube video transcripts and summarize them",
        "You can also read metadata related to youtube videos",
        "You can also fetch timestamps of a particular video",
        "Summarize the transcripts in clear and concise manner"
    ],
    tools=[YouTubeTools()],
    add_datetime_to_context=True
)

newspaper_agent = Agent(
    id='newspaper_research_agent',
    name='Newspaper_Research_Agent',
    model=agents_model,
    role='Newspaper Research Assistant',
    instructions=[
        "You are a research assistant that can read the contents of articles",
        "Whenever a URL is provided you can read the content of the article and can also get its data",
        "Using the available tools search for articles and summarize them and gather relevant information"
    ],
    tools=[Newspaper4kTools()],
    add_datetime_to_context=True
)

web_search_agent = Agent(
    id='web_search_agent',
    name='Web_Search_Agent',
    model=agents_model,
    role='Web Research Assistant',
    instructions=[
        "You are a research assistant that gathers information from the web",
        "Use the available tools to search for articles, summaries, and other important material based on the topic the user requested",
        "Summarize your findings along with the resource links"
    ],
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True
)

# ======================= Team ==============================
medium_article_team = Team(
    id='medium-article-creation-team',
    name='Medium Article Creation Team',
    role='Team Leader which manages research and content creation',
    db=db,
    members=[
        # arxiv_research_agent,
        # hackernews_agent,
        # wikipedia_agent,
        # youtube_agent,
        newspaper_agent,
        # web_search_agent
    ],
    model=orchestrator_model,
    instructions=[
        "You are a team leader managing multiple sub agents in your team",
        "You have access to agents which can do research based on the topic on various sources such as arxiv, X(formerly twitter), youtube, reddit, wikipedia, hackernews, newspaper articles, web search using google search and duckduckgo search",
        "You also have the capability to read and write emails",
        "Your task is to understand the topic given by the user and fetch relevant research information using your team members",
        "Once you have enough research material, your primary task is to create medium(platform) styled articles",
        "Once you have created the medium article, show the user the final draft",
        "Only when the user confirms the draft, save it to the filesystem in a markdown format as a .md file using the filename suggested by user",
        "If the user does not give a filename, then use a self-created name based on the topic on which the article was created"
    ],
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=10,
    tools=[LocalFileSystemTools(target_directory=medium_dir, default_extension='md')],
    stream=True,
    markdown=True
)


# ======================= CMD Interface =====================
if __name__ == "__main__":
    print("🧠 Medium Article Generator (CMD Mode)")
    print("Type 'exit' to quit\n")

    while True:
        user_prompt = input(">>> ")

        if user_prompt.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        print("\n⏳ Running research agents... Please wait...\n")

        # Run research agents and save raw content
        for agent in [
            newspaper_agent,
            # web_search_agent
        ]:
            try:
                run_output = agent.run(user_prompt)
                research_text = run_output.content or ""
            except Exception as e:
                print(f"⚠️ {agent.name} failed: {e}")
                research_text = ""

            # Save raw research content
            agent_filename = f"{agent.id}_{user_prompt.replace(' ', '_')[:50]}.txt"
            filepath = research_dir / agent_filename
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(research_text)

            print(f"💾 Research saved: {filepath.name}")

        print("\n⏳ Research complete. Generating final Medium-style article...\n")

        # ======================== Medium Article ========================
        response_text = ""
        try:
            for event in medium_article_team.run(user_prompt):
                if hasattr(event, "content") and event.content:
                    print(event.content, end="", flush=True)
                    response_text += event.content
        except Exception as e:
            print(f"⚠️ Medium article generation failed: {e}")
            continue

        print("\n\n✅ Article generation completed.")

        save_confirm = input("\nDo you want to save this article? (y/n): ").strip().lower()
        if save_confirm == "y":
            filename = input("Enter filename (without extension) or leave blank for auto-generated: ").strip()
            if filename == "":
                filename = user_prompt.replace(" ", "_")[:50]

            # Save final article ONLY in medium_articals
            filepath = medium_dir / f"{filename}.md"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(response_text)

            print(f"💾 Article saved to {filepath.resolve()}")

        print("\n---------------------------------\n")

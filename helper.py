from agno.agent import Agent 
from agno.models.ollama import Ollama
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import ArxivTools
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

# ======================= Agents ==============================
arxiv_research_agent = Agent(
    id='arxiv_research_agent',
    name='Arxiv_Research_Agent',
    model=agents_model,
    role='Arxiv Research Assistant',
    instructions=[
        "Gather research papers from Arxiv based on user topic.",
        "Summarize findings concisely in plain text."
    ],
    tools=[ArxivTools(download_dir=research_dir)],
    add_datetime_to_context=True
)

newspaper_agent = Agent(
    id='newspaper_research_agent',
    name='Newspaper_Research_Agent',
    model=agents_model,
    role='Newspaper Research Assistant',
    instructions=[
        "Gather information from newspaper articles using URLs or topics.",
        "Summarize content clearly and concisely without unnecessary metadata."
    ],
    tools=[Newspaper4kTools()],
    add_datetime_to_context=True
)

# ======================= Team ================================
medium_article_team = Team(
    id='medium-article-creation-team',
    name='Medium Article Creation Team',
    role='Team Leader managing research and content creation',
    db=db,
    members=[arxiv_research_agent, newspaper_agent],
    model=orchestrator_model,
    instructions=[
        "Use the research collected by team members to create a clean, well-structured, long-form article suitable for Medium or similar blogs.",
        "Do not include local paths, file names, or PC-specific info.",
        "Focus on narrative content with proper headings, flow, and readability.",
        "Once the article is finalized, show it to the user and save only if confirmed."
    ],
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=10,
    tools=[LocalFileSystemTools(target_directory=medium_dir, default_extension='md')],
    stream=True,
    markdown=True
)

# ======================= CMD Interface =======================
if __name__ == "__main__":
    print("🧠 Medium Article Generator (CMD Mode)")
    print("Type 'exit' to quit\n")

    while True:
        user_prompt = input(">>> ")

        if user_prompt.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        print("\n⏳ Running research agents...\n")

        # Run research agents and save raw content
        for agent in [arxiv_research_agent, newspaper_agent]:
            try:
                run_output = agent.run(user_prompt)
                research_text = run_output.content or ""
            except Exception as e:
                print(f"⚠️ {agent.name} failed: {e}")
                research_text = ""

            # Save raw research content in research_paper folder
            safe_filename = f"{agent.id}_{user_prompt.replace(' ', '_')[:50]}.txt"
            filepath = research_dir / safe_filename
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(research_text)

            print(f"💾 Research saved: {filepath.name}")

        print("\n⏳ Research complete. Generating final Medium-style article...\n")

        # Prepare prompt for Medium article generation
        article_prompt = f"""
Using the research collected in a structured manner, 
write a detailed, long-form, well-structured blog article suitable for Medium about: {user_prompt}.
Do NOT include local paths, file addresses, or PC-specific info.
Focus on readability, flow, headings, and engaging narrative style.
"""

        blog_text = ""
        try:
            for event in medium_article_team.run(article_prompt):
                if hasattr(event, "content") and event.content:
                    print(event.content, end="", flush=True)
                    blog_text += event.content
        except Exception as e:
            print(f"⚠️ Medium article generation failed: {e}")
            continue

        print("\n\n✅ Article generation completed.")

        save_confirm = input("\nDo you want to save this article? (y/n): ").strip().lower()
        if save_confirm == "y":
            filename = input("Enter filename (without extension) or leave blank for auto-generated: ").strip()
            if not filename:
                filename = user_prompt.replace(" ", "_")[:50]

            filepath = medium_dir / f"{filename}.md"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(blog_text)

            print(f"💾 Article saved to {filepath.resolve()}")

        print("\n---------------------------------\n")

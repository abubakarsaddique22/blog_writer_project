

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

# ======================= Agents ==============================
arxiv_agent = Agent(
    id='arxiv_research_agent',
    name='Arxiv_Research_Agent',
    model=agents_model,
    role='Arxiv Research Assistant',
    instructions=[
        "You are an expert research assistant specialized in scientific and technical papers on Arxiv.",
        "When given a topic, search for the most relevant and recent papers.",
        "Extract the main findings, methodologies, conclusions, and key insights.",
        "Summarize each paper in a clear, concise manner in plain text.",
        "Do NOT include raw PDFs, tables, or personal file paths.",
        "Organize the summary with headings for clarity if multiple papers are included.",
        "Output should be well-structured research notes suitable for content generation."
    ],
    tools=[ArxivTools(download_dir=research_dir)],
    add_datetime_to_context=True
)

hackernews_agent = Agent(
    id='hackernews_research_agent',
    name='HackerNews_Research_Agent',
    model=agents_model,
    role='HackerNews Research Assistant',
    instructions=[
        "You are an expert in extracting trending tech, AI, and startup discussions from HackerNews.",
        "Find recent posts, comments, or discussions related to the given topic.",
        "Summarize the context, main points, and valuable insights in clear, concise notes.",
        "Highlight opinions, debates, and emerging trends that can enrich the final article.",
        "Do NOT include usernames, links, or any irrelevant data."
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
        "You are an expert in summarizing Wikipedia articles.",
        "Search for relevant articles for the user-provided topic.",
        "Extract main sections, subheadings, key facts, definitions, and historical context.",
        "Summarize the information in your own words in a clear, coherent narrative.",
        "Include citations in plain text format if possible, without URLs or metadata.",
        "Avoid copying raw Wikipedia content; rewrite for readability."
    ],
    tools=[WikipediaTools()],
    add_datetime_to_context=True
)

youtube_agent = Agent(
    id='youtube_research_agent',
    name='YouTube_Research_Agent',
    model=agents_model,
    role='YouTube Research Assistant',
    instructions=[
        "You are an expert in summarizing YouTube video content.",
        "Search for videos relevant to the topic and analyze transcripts, titles, descriptions, and metadata.",
        "Summarize the main points, examples, explanations, and insights from the video.",
        "Include any useful timestamps for reference.",
        "Output should be in concise notes suitable for article generation.",
        "Do NOT include raw transcripts, links, or channel info."
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
        "You are an expert in gathering information from news articles.",
        "Search for news articles relevant to the given topic.",
        "Summarize the key information, quotes, trends, statistics, and context in plain text.",
        "Do NOT include raw HTML, URLs, or unrelated metadata.",
        "Organize findings clearly for easy integration into blog articles."
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
        "You are an expert web researcher using DuckDuckGo.",
        "Search for relevant blogs, articles, forums, or posts for the topic.",
        "Summarize insights, examples, and important points in your own words.",
        "Avoid including personal URLs, local paths, or raw tables.",
        "Output should be structured and ready for article writing."
    ],
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True
)

# ======================= Team ================================
medium_article_team = Team(
    id='medium-article-creation-team',
    name='Medium Article Creation Team',
    role='Team Leader managing research and content creation',
    db=db,
    members=[
        arxiv_agent,
        hackernews_agent,
        wikipedia_agent,
        youtube_agent,
        newspaper_agent,
        web_search_agent
    ],
    model=orchestrator_model,
    instructions=[
        "You are a team leader coordinating multiple research agents.",
        "Collect all research data from your agents, then synthesize it into a clean, long-form Medium-style article.",
        "Ensure the article is professional, in-depth, and engaging, suitable for top Medium blogs.",
        "Use headings, subheadings, and sections to organize the content clearly.",
        "Focus on readability, narrative flow, and clarity for the target audience.",
        "Do NOT include file paths, raw research files, or PC-specific information in the article.",
        "Aim for a word count between 1500–2500 words for comprehensive coverage.",
        "After generating the draft, present it to the user for confirmation before saving.",
        "Only save final Markdown (.md) article in the 'medium_articals' folder."
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

        # Run all research agents and save raw content
        for agent in medium_article_team.members:
            try:
                run_output = agent.run(user_prompt)
                research_text = run_output.content or ""
            except Exception as e:
                print(f"⚠️ {agent.name} failed: {e}")
                research_text = ""

            # Save raw research content
            safe_filename = f"{agent.id}_{user_prompt.replace(' ', '_')[:50]}.txt"
            filepath = research_dir / safe_filename
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(research_text)

            print(f"💾 Research saved: {filepath.name}")

        print("\n⏳ Research complete. Generating final Medium-style article...\n")

        # Prompt for Medium article
        article_prompt = f"""
Using all research collected by the team, write a detailed, long-form, well-structured blog article suitable for Medium about: {user_prompt}.
- Include headings, subheadings, and logical sections.
- Make it professional, engaging, and easy to read.
- Do NOT include file paths, local PC info, or raw tables.
- Aim for a comprehensive 1500–2500 words narrative.
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

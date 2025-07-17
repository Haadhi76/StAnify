# StAnify

A multi-agent visual storytelling system for teaching children generalized concepts.

## 📦 Dependencies

- crewai
- streamlit
- openai
- diffusers (Stable Diffusion)
- transformers
- accelerate
- pillow
- python-dotenv

## 🛠️ Setup

1. **Clone & enter the project**

   ```bash
   git clone <https://github.com/yourusername/StAnify.git>
   cd stanify_project
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   .\\venv\\Scripts\\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your API/model paths.

5. **Test minimal demo**

   ```bash
   python main.py
   ```

## 📁 Folder Structure

```
agents/      # Agent definitions
tools/       # Utility scripts/tools
pipeline/    # Dataflow and orchestration
ui/          # Streamlit or other frontend
outputs/     # Generated images/stories
docs/        # Documentation, guides
logs/        # Logs and traces
main.py      # Entrypoint
.env
.env.example
.gitignore
README.md
```

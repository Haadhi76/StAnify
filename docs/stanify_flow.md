# StAnify Pipeline Flow

## Input
- Concept: e.g., "What is an if-statement?"

## Pipeline:
1. **ConceptToNarrativeAgent** → story beats + characters
2. **SceneGeneratorAgent** → scene prompts
3. **PromptRefinerAgent** → refine image prompts
4. **ImageGeneratorAgent (Stable Diffusion)** → visuals
5. **DialogueAgent** → character speech bubbles, narration
6. **TTS (optional)**
7. **SlideCompiler** → Streamlit or slide output

## Output
- Interactive, visual story explaining the concept for children

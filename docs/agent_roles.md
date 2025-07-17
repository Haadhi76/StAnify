## ConceptToNarrativeAgent
- **Goal**: Convert a learning concept into a narrative outline
- **Input**: Concept string
- **Output**:
  ```json
  {
    "title": "Max Learns Multiplication",
    "characters": ["Max", "Miss Dot"],
    "beats": ["Max wants to buy toys", "Miss Dot teaches grouping", "They solve it with multiplication"],
    "setting": "toy store"
  }
  ```
- **Tools**: OpenAI prompt
- **Behavior**: task-driven

---

## SceneGeneratorAgent
- **Goal**: Transform story outline into visual scene prompts
- **Input**: Story outline JSON
- **Output**:
  ```json
  [
    "Max looks at toys, puzzled by the price tags",
    "Miss Dot draws groups of toys on a chalkboard",
    "Max groups toys into sets and multiplies"
  ]
  ```
- **Tools**: OpenAI prompt
- **Behavior**: task-driven

---

## PromptRefinerAgent
- **Goal**: Enhance and clarify scene prompts for image generation
- **Input**: Scene prompt strings
- **Output**:
  ```json
  [
    "A child in a toy store, looking at many toys with price tags, colorful, cartoon style",
    "A friendly teacher drawing groups of teddy bears on a chalkboard, classroom, cartoon style",
    "A child happily grouping toys into sets of five, bright store, cartoon style"
  ]
  ```
- **Tools**: OpenAI, prompt engineering
- **Behavior**: task-driven

---

## ImageGeneratorAgent
- **Goal**: Generate images from refined prompts using Stable Diffusion
- **Input**: Refined prompt strings
- **Output**: image files/paths (PNG/JPG)
- **Tools**: Stable Diffusion (diffusers)
- **Behavior**: task-driven

---

## DialogueAgent
- **Goal**: Write speech bubbles and narration for each scene
- **Input**: Story beats, scene images, characters
- **Output**:
  ```json
  [
    {"scene": 1, "dialogue": ["Max: How do I buy so many toys?", "Miss Dot: Let me show you a trick!"]},
    {"scene": 2, "dialogue": ["Miss Dot: See how we can group them?", "Max: Wow!"]},
    {"scene": 3, "dialogue": ["Max: Multiplying is easy!", "Miss Dot: Great job, Max!"]}
  ]
  ```
- **Tools**: OpenAI prompt
- **Behavior**: task-driven

---

## TTSAgent (optional)
- **Goal**: Convert narration/dialogue to audio
- **Input**: Narration/dialogue text
- **Output**: Audio file paths
- **Tools**: ElevenLabs TTS
- **Behavior**: task-driven

---

## SlideCompiler
- **Goal**: Assemble images, dialogue, and narration into slides
- **Input**: Images, dialogue, optional audio
- **Output**: Streamlit UI or exportable slides
- **Tools**: Streamlit, Python
- **Behavior**: task-driven

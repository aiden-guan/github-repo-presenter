# Project Archetypes & Classification Guide

A repository presentation must reflect what the software actually is. Forcing a developer tool into a consumer SaaS template, or an AI research pipeline into a generic web app layout, damages credibility immediately.

When auditing or presenting a repository, first classify the project into one or more of the archetypes below. Tailor the information hierarchy, visual presentation, and technical focus accordingly.

---

## 1. Product / SaaS

Web applications, dashboards, platforms, and hosted software (e.g., Supabase, Formbricks, Plane, Midday).

### Identification Signals
- Manifests: Next.js, Remix, Vite, SvelteKit, Nuxt, Rails, Django, Laravel.
- Directories: `app/`, `pages/`, `components/`, `routes/`, `server/`, `prisma/`, `drizzle/`.
- Infrastructure: Docker compose, database migrations, authentication providers, Stripe/payment configs.

### Presentation Priorities
1. **Hero Viewport**: Value proposition, immediate visual proof (high-resolution product screenshot or short loop GIF), and live links (`Live Demo`, `Docs`, `Deploy`).
2. **Feature Grid**: 2x2 or 2x1 visual grid highlighting primary workflows with concrete outcomes—not generic marketing buzzwords.
3. **User Flow / Walkthrough**: Clear step-by-step narrative showing how a user accomplishes their primary goal.
4. **Architecture & Data Flow**: Diagram showing Client → API/BFF → Services → Database / Third-party APIs (Stripe, Auth, LLM).
5. **Self-Hosting / Deployment**: Separate Quick Start (local development) from Production Deployment (Docker, Vercel, Supabase).

### Ideal Section Order
1. Hero (Identity + One-sentence promise + Badges/Links + Hero Visual)
2. What it does (Core value & target audience)
3. Key Features (Structured 2-column visual grid with screenshots/diagrams)
4. Interactive Walkthrough / Demo path
5. System Architecture (Mermaid diagram + numbered data flow)
6. Engineering Highlights (Problem, Approach, Why, Tradeoff)
7. Tech Stack (Client, Server, Database, Infrastructure)
8. Getting Started (Prerequisites, env setup, run)
9. Production / Deployment (Docker, Docker Compose, Cloud)
10. Roadmap & Status (Honest maturity declaration)
11. Contributing & License

---

## 2. AI / Agent Project

Autonomous agents, LLM orchestration, evaluation pipelines, multimodal assistants, and RAG systems (e.g., Browser Use, Langfuse, AutoGen).

### Identification Signals
- Manifests / Dependencies: `openai`, `anthropic`, `langchain`, `langgraph`, `llamaindex`, `instructor`, `guidance`, `crewai`, `transformers`, `torch`.
- Directories: `prompts/`, `agents/`, `tools/`, `evals/`, `chains/`, `embeddings/`.
- Configuration: Model provider keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`), vector databases (Pinecone, Qdrant, Chroma, pgvector).

### Presentation Priorities
1. **Immediate Demonstration**: Visual proof of the agent or model *actually performing a task* (terminal recording, web interaction recording, input-to-output transformation).
2. **System Flow & Orchestration**: Mermaid diagram showing:
   `User Input → Context / Vector Retrieval → Agent Core / Planner → Tool Execution Loop → Response / Artifact Generation`.
3. **Model & Tool Responsibilities**: Clear breakdown of which models/prompts handle which sub-tasks (e.g., cheap model for triage, frontier model for code synthesis).
4. **Evaluation & Guardrails**: How output is validated, cost/latency controls, context window management, and fallback behaviors.
5. **Known Limitations**: Explicit discussion of edge cases, token limits, failure modes, and security constraints (prompt injection, tool permissions).

### Ideal Section Order
1. Hero (Identity + Value proposition + Terminal/Browser Demo)
2. Capability Demonstration (Concrete Input → Agent Reasoning → Tool Action → Output)
3. Architecture & Orchestration Flow (Mermaid state diagram / sequence)
4. Tooling & Integrations (APIs, sandbox environments, browser drivers)
5. Engineering Highlights (Context management, error recovery, token optimization)
6. Evaluation & Benchmarks (Only verified eval results; omit if unmeasured)
7. Quick Start (API keys required, local run command)
8. Known Limitations & Failure Modes (Honest boundaries)
9. Tech Stack & Model Requirements
10. License & Safety Notice

---

## 3. Developer Tool / Library / CLI

SDKs, CLI utilities, npm/PyPI packages, UI component kits, and middleware (e.g., shadcn/ui, Trigger.dev, Infisical CLI).

### Identification Signals
- Manifests: Package publishing configuration (`exports`, `types`, `publishConfig`, `setup.py`, `Cargo.toml [package]`, `main.go`).
- Directories: `lib/`, `src/`, `cmd/`, `packages/`, `crates/`, `examples/`.
- Tests: Heavy test suites (`tests/`, `__tests__/`, `spec/`), GitHub Actions for multiple OS/runtimes.

### Presentation Priorities
1. **Immediate Code Example**: A working, copy-pasteable 5-line code snippet or terminal CLI snippet in the first viewport.
2. **Installation**: One-line package manager install command (`npm install`, `pip install`, `cargo add`, `brew install`).
3. **API Ergonomics & Key Exports**: Short, readable code snippets covering the top 3-4 use cases.
4. **Configuration / Type Reference**: Concise explanation of core options.
5. **Benchmarks**: Only include if rigorous, automated, reproducible, and verifiable in `benchmarks/` or CI.
6. **Architecture**: Only if the tool has a non-trivial runtime engine or plugin model.

### Ideal Section Order
1. Hero (Identity + One-sentence description + Install badge/npm version + Short code block)
2. Why [Tool Name]? (The specific developer friction it eliminates)
3. 60-Second Quick Start (Install → Import → Minimal working execution)
4. Common Recipes / Use Cases (Tabbed or sequential code blocks with explanations)
5. Architecture & How it Works (If plugin-based, compiled, or multi-process)
6. Configuration & Options (Typed reference table)
7. Development & Running Tests
8. Contributing & License

---

## 4. Game / Interactive Graphics

Web games, 2D/3D engines, canvas simulations, Godot/Unity exports, Three.js/WebGL applications.

### Identification Signals
- Manifests: `three`, `pixi.js`, `phaser`, `kaboom`, `godot`, `unity`, `raylib`, `pygame`, `wgpu`.
- Directories: `assets/sprites/`, `assets/audio/`, `scenes/`, `shaders/`, `engine/`, `entities/`.
- Code: Game loop (`tick`, `update`, `render`), collision detection, state machines.

### Presentation Priorities
1. **Gameplay Demonstration**: High-framerate GIF, webm, or screenshot sequence showing the core gameplay loop.
2. **Core Loop Explanation**: `Player Input → Physics / Collision → Game State Update → Render Pipeline`.
3. **Controls & Mechanics**: Clear keyboard/mouse/gamepad mapping table.
4. **Technical Systems**: Asset pipeline, shader architecture, state management, procedural generation, or physics engine.
5. **Play Online Link**: Direct link to itch.io, GitHub Pages, or Vercel live instance.

### Ideal Section Order
1. Hero (Identity + Game hook + Play Online Button + Gameplay GIF)
2. Core Gameplay Loop & Mechanics
3. Controls (Clean visual table)
4. Technical Architecture (Game loop, physics, state synchronizer)
5. Asset & Pipeline Architecture (Spritesheets, procedural algorithms, audio)
6. Engineering Highlights (Frame pacing, memory optimization, collision spatial hash)
7. Local Development & Build
8. Credits (Art, music, third-party libraries) & License

---

## 5. Data / Machine Learning / Research

ETL pipelines, data visualization platforms, training/inference code, dataset analysis, research papers.

### Identification Signals
- Manifests: `pandas`, `numpy`, `scipy`, `polars`, `dbt`, `airflow`, `mlflow`, `scikit-learn`, `jax`, `torch`.
- Files/Directories: `notebooks/`, `data/`, `pipelines/`, `models/`, `experiments/`, `train.py`.
- Documentation: References to papers, datasets (Kaggle, HuggingFace), methodology.

### Presentation Priorities
1. **Problem Definition & Hypothesis**: What data problem or research question is being solved?
2. **Pipeline Architecture**: Visual Mermaid diagram of the end-to-end DAG:
   `Data Ingestion → Preprocessing / Cleaning → Feature Engineering → Model / Transformation → Evaluation / Dashboard`.
3. **Dataset & Provenance**: Source, size, licensing, and schema of data.
4. **Reproducible Methodology**: Exact scripts and seed configs to reproduce results.
5. **Evaluation & Artifacts**: Visual charts, loss curves, confusion matrices, or data outputs.

### Ideal Section Order
1. Hero (Identity + Research/Problem thesis + Output visualization)
2. Methodology & Problem Statement
3. Pipeline Architecture (Mermaid flowchart)
4. Dataset & Preprocessing Details
5. Model / Algorithm Design & Decisions
6. Results, Metrics, and Evaluation (Honest comparisons)
7. Reproducibility Guide (Data download, env setup, train/eval commands)
8. Hardware Requirements & Cost/Runtime Estimates
9. References & License

---

## 6. Mobile Application

iOS, Android, React Native, Expo, Flutter, or Swift/Kotlin apps.

### Identification Signals
- Manifests: `react-native`, `expo`, `flutter`, `pubspec.yaml`, `Podfile`, `build.gradle.kts`, `Package.swift`.
- Directories: `ios/`, `android/`, `app/`, `screens/`, `navigation/`.
- Assets: App icons, splash screens, mobile screenshots.

### Presentation Priorities
1. **Device Mockups**: Framed iPhone/Android device screenshots showing the app's top 2-3 screens side by side.
2. **User Journey**: Screen-by-screen progression of the core flow.
3. **Platform Support & Architecture**: Native modules, navigation hierarchy, offline storage (SQLite, WatermelonDB, MMKV), background sync.
4. **Running Locally**: Expo Go QR code, simulator commands (`npm run ios`, `npm run android`).

### Ideal Section Order
1. Hero (Identity + App Store / TestFlight badge or demo video + Framed phone mockup)
2. User Experience & Key Flows (Side-by-side screenshots with descriptions)
3. Architecture (Client state, local cache, offline-first sync, push notifications)
4. Engineering Highlights (Gesture physics, 60fps animations, background tasks)
5. Prerequisites & Local Setup (Node, Xcode, Android Studio, Expo CLI)
6. Environment Configuration
7. Testing & Build Instructions
8. License

---

## 7. Infrastructure / Backend System

Distributed systems, message queues, databases, API gateways, proxy services, daemon processes, Kubernetes controllers.

### Identification Signals
- Languages: Go, Rust, C++, Java, Erlang, Elixir, Python (FastAPI/Tornado).
- Files: `docker-compose.yml`, `Dockerfile`, `k8s/`, `proto/`, `terraform/`, `Makefile`.
- Patterns: Concurrency primitives, network protocols (gRPC, WebSocket, TCP, Raft, Paxos).

### Presentation Priorities
1. **System Topology**: Clean architecture diagram of nodes, workers, brokers, and storage tiers.
2. **Performance & Protocol Characteristics**: Latency SLA, concurrency model, serialization protocol (Protobuf, FlatBuffers), consistency model.
3. **API / Wire Protocol**: Minimal request/response or message spec.
4. **Failure Modes & Resilience**: Network partitions, retry policy, backpressure, leader election.
5. **Deployment & Observability**: Metrics (Prometheus), logging, tracing (OpenTelemetry), health probes.

### Ideal Section Order
1. Hero (Identity + System purpose + Architecture overview diagram)
2. System Architecture & Component Topology
3. Core Protocol / API Specification (Curl / gRPC snippet)
4. Resilience & Concurrency Model (Worker pools, queues, transactions)
5. Engineering Highlights (Memory pooling, zero-copy, lock-free queues, backpressure)
6. Verified Performance Profile (Only if benchmark code is in the repository)
7. Quick Start with Docker / Local cluster
8. Configuration Reference (Flags, environment variables)
9. Observability & Monitoring
10. License

---

## 8. Personal Experimental / Showcase Project

Hackathon entries, creative experiments, novel algorithms, proof-of-concept prototypes.

### Identification Signals
- Single maintainer, recent creation date, high density of novel experimentation, minimal enterprise boilerplate.
- Often explores a single provocative idea or technology pairing.

### Presentation Priorities
1. **The Core Question / Hook**: "Can X be done in the browser using Y?" or "What happens when you combine A with B?"
2. **Interactive Proof / Visual Demo**: Immediately show that the experiment actually works.
3. **What Was Built vs What Was Borrowed**: Explicit attribution of author-written code vs third-party libraries.
4. **Engineering Hurdles & Insights**: What failed first? What non-obvious solution worked? What trade-offs were made?
5. **Honest Scope**: Clear declaration that this is a prototype, noting what would be needed for production.

### Ideal Section Order
1. Hero (Identity + The Experiment Hook + Demo GIF/Video + Try it live link)
2. The Hypothesis & What it Proves
3. How it Works Under the Hood (Step-by-step breakdown with code pointers)
4. Engineering Challenges & What I Learned (Problem-Approach-Why-Tradeoff)
5. Technology Stack & Attribution
6. How to Run it Locally
7. Known Limitations & What's Next
8. License

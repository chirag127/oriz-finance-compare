<div align="center">


  __ _ _ __  _ __   __ _  ___| |__   ___  _ __ ___   ___  _ __ 
 / _` | '_ \| '_ \ / _` |/ __| '_ \ / _ \| '_ ` _ \ / _ \| '__|
| (_| | | | | | | | (_| | (__| | | | (_) | | | | | | (_) | |   
 \__,_|_| |_|_| |_|\__,_|\___|_| |_|\___/|_| |_| |_|\___/|_|   
                                                              


**A modern, responsive web application for comparing financial products, offering users a clear and concise overview of various banking and investment options.**

---


![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/FinCompare-Financial-Product-Comparison-Web-App/ci.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white)


![Codecov](https://img.shields.io/codecov/c/github/chirag127/FinCompare-Financial-Product-Comparison-Web-App?style=flat-square&logo=codecov&logoColor=white)


![Tech Stack](https://img.shields.io/badge/Stack-TypeScript%20%7C%20Vite%20%7C%20React-blue?style=flat-square&logo=typescript&logoColor=white)


![Formatter](https://img.shields.io/badge/Formatted%20with-Biome-blueviolet?style=flat-square&logo=biome&logoColor=white)


![License](https://img.shields.io/github/license/chirag127/FinCompare-Financial-Product-Comparison-Web-App?style=flat-square)


![GitHub Stars](https://img.shields.io/github/stars/chirag127/FinCompare-Financial-Product-Comparison-Web-App?style=flat-square&logo=github)


**[Star ⭐ this Repo](https://github.com/chirag127/FinCompare-Financial-Product-Comparison-Web-App/stargazers) to support the project!**

</div>

## Overview

FinCompare is a modern, responsive web application designed to simplify the complex world of financial products. It provides users with a clean, intuitive interface to compare banking, investment, and insurance options side-by-side, empowering informed financial decisions through data-driven insights.

## Table of Contents

- [Architecture](#architecture)
- [AI Agent Directives](#-ai-agent-directives)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Available Scripts](#available-scripts)
- [Core Principles](#core-principles)
- [Contributing](#contributing)
- [License](#license)

## Architecture

This project adheres to **Feature-Sliced Design (FSD)**, a scalable and maintainable architectural methodology for frontend applications. This structure promotes a clear separation of concerns and minimizes coupling between different parts of the application.

plaintext
src/
├── app/         # App-wide logic, providers, and styles
├── pages/       # Complete pages (e.g., HomePage, ComparisonPage)
├── widgets/     # Composite UI components (e.g., Header, ProductTable)
├── features/    # Business-logic features (e.g., FilterProducts, AddToCompare)
├── entities/    # Business entities and their UI (e.g., ProductCard, BankLogo)
└── shared/      # Reusable utilities, UI kit, APIs, and configuration


## 🤖 AI Agent Directives

<details>
<summary><strong>Click to Expand: System Instructions for AI Code Generation</strong></summary>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat this `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type and apply the corresponding **Apex Toolchain**. This repository, `FinCompare-Financial-Product-Comparison-Web-App`, is a modern frontend web application.

*   **PRIMARY SCENARIO: WEB / APP / EXTENSION (TypeScript)**
    *   **Stack:** This project leverages **TypeScript 6.x (Strict Mode)**. Key tools include **Vite 7** (with the Rolldown Rust-based bundler for extreme speed), **React 20** (or a signal-based framework like SolidJS 2.0), and **TailwindCSS v4** (JIT Engine) for styling.
    *   **Architecture:** Adheres to **Feature-Sliced Design (FSD)**, ensuring a strict, scalable, and maintainable project structure. Code must be organized into `app`, `pages`, `widgets`, `features`, `entities`, and `shared` layers.
    *   **Linting & Formatting:** **Biome** is the single, unified toolchain for all linting, formatting, and import sorting. All code MUST pass Biome checks before merging.
    *   **Testing:** **Vitest** for unit and integration tests, colocated with source code. **Playwright** for end-to-end (E2E) testing to ensure robust user journeys.
    *   **Desktop Strategy:** The architecture is designed to be compatible with **Tauri v2**, allowing for a seamless transition to a native desktop application with minimal refactoring.

*   **SECONDARY SCENARIO B: SYSTEMS / PERFORMANCE (Rust/Go) - *Not applicable for this project's primary function. Reference only for potential high-performance backend services.***
    *   **Stack:** Rust (Cargo), Go (Modules).

*   **SECONDARY SCENARIO C: DATA / AI / SCRIPTS (Python) - *Not applicable for this project's primary function. Reference only for potential data ingestion or analysis scripts.***
    *   **Stack:** uv, Ruff, Pytest.

</details>

## Getting Started

Follow these instructions to get a local copy up and running for development and testing purposes.

### Prerequisites

- Node.js (v20.x or later)
- pnpm (recommended package manager)

### Installation

1.  **Clone the repository:**
    sh
    git clone https://github.com/chirag127/FinCompare-Financial-Product-Comparison-Web-App.git
    

2.  **Navigate to the project directory:**
    sh
    cd FinCompare-Financial-Product-Comparison-Web-App
    

3.  **Install dependencies:**
    sh
    pnpm install
    

4.  **Start the development server:**
    sh
    pnpm dev
    
    The application will be available at `http://localhost:5173`.

## Available Scripts

This project uses `pnpm` as its primary package manager. Here are the most common scripts:

| Script       | Description                                                 |
| :----------- | :---------------------------------------------------------- |
| `pnpm dev`     | Starts the development server with Hot Module Replacement.  |
| `pnpm build`   | Compiles and bundles the application for production.        |
| `pnpm preview` | Serves the production build locally for verification.       |
| `pnpm test`    | Runs unit and integration tests using Vitest.               |
| `pnpm lint`    | Lints the codebase using Biome.                             |
| `pnpm format`  | Formats the codebase using Biome.                           |

## Core Principles

- **SOLID:** Ensures code is understandable, flexible, and maintainable.
- **DRY (Don't Repeat Yourself):** Avoids redundancy to improve clarity and reduce bugs.
- **YAGNI (You Ain't Gonna Need It):** Prevents over-engineering by implementing only what is necessary.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see the [**CONTRIBUTING.md**](https://github.com/chirag127/FinCompare-Financial-Product-Comparison-Web-App/blob/main/.github/CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**.

See the [**LICENSE**](https://github.com/chirag127/FinCompare-Financial-Product-Comparison-Web-App/blob/main/LICENSE) file for more details.

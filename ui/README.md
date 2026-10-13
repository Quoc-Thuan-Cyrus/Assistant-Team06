# docs/

Project brief, blueprint, ADRs, reports and the team logbook go here.

## Overview
This directory serves as the central hub for the foundational planning, strategic architecture, and ongoing records of our upcoming interactive platform. While the core objective revolves around user engagement, media delivery, and immersive experiences, the specific content verticals and final implementation details remain intentionally undefined at this stage of development. 

## Directory Structure
*   **`/briefs`**: High-level outlines of engagement goals, target audience demographics, and overarching experience pillars.
*   **`/blueprints`**: Conceptual designs, wireframes, and architectural plans for the platform's interactive features and media handling.
*   **`/adrs`**: Architecture Decision Records detailing the technical choices made to support dynamic content delivery and user interaction mechanics.
*   **`/reports`**: Feasibility studies, market research on audience retention, and milestone progress tracking.
*   **`/logbook`**: The team's ongoing brainstorms, daily development notes, and meeting minutes, incl.

## Contributor Guidelines
Until Phase 2 is officially greenlit, all documentation should remain generalized. Focus on the underlying mechanics of user engagement, system scalability, and interaction models rather than specific genres or concrete entertainment themes.
# UI

This folder is reserved for the user interface of the Smart Virtual Assistant.

The interface will be built later using Streamlit or Gradio in the practical session.

## Current status

This folder is intentionally left empty for Lab 1 and serves as a placeholder for the future UI implementation.

## Planned functionality

- display a chat interface for the assistant
- allow users to enter questions in the browser
- connect the UI to the backend logic in `src/assistant`

## Example setup for later

### Streamlit
```bash
pip install streamlit
streamlit run app.py
```

### Gradio
```bash
pip install gradio
python app.py
```

## Notes

For the current lab, the main logic is implemented in the Python backend and can be run with:
```bash
python -m assistant "where is the training office?"
```

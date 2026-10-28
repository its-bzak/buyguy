# CLAUDE.md

## Project Overview

This project is a full-stack shopping application built for the 2026 PayPal AI Hackathon.

The application integrates with the Channel3 API, OpenAI API, and PayPal API to provide a seamless shopping experience where users can:

- Describe their shopping needs using natural language.
- Receive relevant product recommendations.
- Discover products from multiple vendors.
- Complete purchases through a streamlined, unified checkout experience.

Prioritize a functional end-to-end user experience, reliability, security, and maintainable code.

## Tech Stack

### Languages
- TypeScript
- Python

### Frontend
- React
- Next.js
- Tailwind CSS

### Backend
- FastAPI

### External Services
- Channel3 API: Product discovery and recommendations.
- OpenAI API: Natural language understanding and shopping assistance.
- PayPal API: Checkout and payment processing.

Use the existing project structure and dependencies. Do not introduce new frameworks or dependencies unless necessary.

## Development Guidelines

### General
- Inspect the existing codebase before making changes.
- Follow established project patterns and architecture.
- Prefer simple, focused changes over unnecessary refactoring.
- Reuse existing components, utilities, and abstractions where appropriate.
- Avoid duplicating logic.
- Do not introduce placeholder implementations or mock data into production flows unless explicitly requested.
- Do not overwrite unrelated user changes.
- Explain significant architectural decisions and trade-offs.

### Code Style
- Use camelCase for variables and functions.
- Use PascalCase for React components, classes, and types where appropriate.
- Use kebab-case for filenames unless the framework or existing conventions require otherwise.
- Use 2 spaces for indentation in TypeScript and frontend code.
- Follow PEP 8 conventions in Python.
- Follow the formatting and linting rules defined by the existing project configuration.
- Prefer descriptive names and small, focused functions.
- Add comments for non-obvious logic, not self-explanatory code.
- Use TypeScript types effectively; avoid `any` unless there is a clear justification.
- Handle errors explicitly and provide useful error messages.

### Architecture
- Keep frontend presentation separate from backend business logic.
- Use Next.js for the frontend and FastAPI for backend services, following the existing division of responsibilities.
- Keep external API integrations behind reusable service or client modules.
- Validate inputs at application boundaries.
- Use environment variables for configuration and secrets.
- Avoid duplicating business logic across the frontend and backend.
- Follow existing API response formats and error-handling conventions.

### API Integrations and Security
- Never hardcode API keys, access tokens, client secrets, or other credentials.
- Never expose private API credentials in client-side code.
- Use environment variables and the existing configuration system for secrets.
- Validate and sanitize external API responses before relying on them.
- Handle API failures, timeouts, rate limits, and unexpected response formats.
- Follow the official API documentation and existing integration patterns.
- Never assume an external API succeeded without checking its response.

### Payments and Checkout
- Treat payment processing and order creation as security-sensitive operations.
- Perform payment verification on the server.
- Never trust client-submitted prices, totals, payment statuses, or vendor identifiers without server-side validation.
- Prevent duplicate order creation and payment processing where applicable.
- Verify payment completion using the appropriate PayPal server-side mechanisms.
- Keep order state consistent when payments fail, are canceled, or remain pending.
- Do not claim that a payment succeeded until its status has been verified.

### Testing and Verification
- Inspect available scripts and project configuration before running commands.
- Run relevant tests, linting, and type checks after making changes when available.
- Add or update tests for important business logic and bug fixes.
- Test error cases as well as successful flows.
- Do not claim that tests pass unless they were actually run and passed.
- If a check cannot be run, explain why.

### Working Process
1. Understand the relevant code and existing implementation before editing.
2. Identify the smallest reasonable change that solves the problem.
3. Implement the change while following project conventions.
4. Run relevant checks and review the resulting diff.
5. Summarize what changed, what was tested, and any remaining issues.

## Project-Specific Priorities

- Prioritize the core shopping flow: natural-language input → product discovery → recommendations → checkout.
- Keep product information and vendor details consistent throughout the shopping flow.
- Make the user experience clear when products are unavailable, API requests fail, or checkout cannot be completed.
- Prefer reliable, demonstrable end-to-end functionality over unnecessary complexity.
- Do not invent API capabilities, request fields, or response formats; consult the official documentation or existing implementation.
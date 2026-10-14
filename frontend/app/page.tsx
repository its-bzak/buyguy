"use client";

import { useState, type FormEvent } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [hasSubmitted, setHasSubmitted] = useState(false);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (query.trim()) {
      setHasSubmitted(true);
    }
  }

  return (
    <main className="grid min-h-screen grid-cols-1 items-center justify-items-center bg-[radial-gradient(ellipse_at_top,_#172554_0%,_#09090b_55%)] px-6 font-sans text-white md:grid-cols-[1fr_minmax(0,8fr)_1fr]">
      <div className="flex w-full flex-col items-center gap-10 text-center md:col-start-2">
        <h1 className="text-3xl sm:text-4xl">
          What are we looking for today?
        </h1>
        <form
          className="flex w-full items-center gap-3 rounded-full border border-blue-200/10 bg-zinc-900/80 p-2 shadow-2xl shadow-blue-950/30 backdrop-blur-sm md:max-w-2xl"
          onSubmit={handleSubmit}
        >
          <input
            aria-label="Search"
            className="min-w-0 flex-1 bg-transparent px-4 py-3 text-left text-lg text-white outline-none placeholder:text-zinc-400"
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Pair of shoes for dad, a shirt for mom..."
            type="text"
            value={query}
          />
          <button
            aria-label="Send"
            className="flex size-11 shrink-0 items-center justify-center rounded-full bg-blue-600 text-white transition-colors hover:bg-blue-500 disabled:cursor-not-allowed disabled:bg-zinc-700 disabled:text-zinc-400"
            disabled={!query.trim()}
            type="submit"
          >
            <svg
              aria-hidden="true"
              className="size-5"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                d="M5 12h14m-6-6 6 6-6 6"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="1.8"
              />
            </svg>
          </button>
        </form>
        <section
          aria-label="Search results"
          className={`w-full overflow-hidden transition-[height] duration-700 ease-in-out motion-reduce:transition-none md:max-w-2xl ${
            hasSubmitted ? "h-[40vh]" : "h-0"
          }`}
        />
      </div>
    </main>
  );
}

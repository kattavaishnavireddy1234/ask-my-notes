<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AskMyNotes</title>

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      line-height: 1.5;
      background-color: #f4f7fb;
      color: #1e293b;
    }

    header {
      background: linear-gradient(135deg, #0b1f5e, #08143c);
      color: white;
      padding: 3rem 1.5rem;
      text-align: center;
    }

    header h1 {
      margin: 0;
      font-size: 2.5rem;
    }

    header p {
      margin-top: 0.75rem;
      font-size: 1.1rem;
    }

    main,
    footer {
      width: 100%;
      max-width: 850px;
      margin: 0 auto;
      padding: 2rem 1.5rem;
    }

    main {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    section {
      background-color: white;
      padding: 1.5rem;
      border-radius: 12px;
      border: 1px solid #dbe4f0;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
    }

    label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
      color: #0b1f5e;
    }

    input,
    textarea,
    button {
      width: 100%;
      padding: 0.85rem;
      font-size: 1rem;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      margin-bottom: 1rem;
    }

    textarea {
      resize: vertical;
    }

    button {
      background-color: #0b1f5e;
      color: white;
      border: none;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.2s ease;
    }

    button:hover {
      background-color: #08143c;
    }

    #answer {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    #qtype-pill,
    #tool-pill {
      display: inline-block;
      width: fit-content;
      padding: 0.3rem 0.9rem;
      border-radius: 999px;
      background-color: #dbeafe;
      color: #0b1f5e;
      font-size: 0.9rem;
      font-weight: bold;
    }

    details {
      margin-top: 1rem;
    }

    summary {
      cursor: pointer;
      font-weight: bold;
      color: #0b1f5e;
    }

    footer {
      text-align: center;
      color: #64748b;
      font-size: 0.95rem;
      padding-bottom: 2rem;
    }
  </style>
</head>

<body>
  <header>
    <h1>AskMyNotes</h1>
    <p>Upload a PDF. Ask a question. Get a grounded answer.</p>
  </header>

  <main>
    <section>
      <label for="pdf-input">Upload your notes (PDF)</label>
      <input type="file" id="pdf-input" accept="application/pdf">
      <p id="upload-status"></p>
    </section>

    <section>
      <label for="question">Your question</label>
      <textarea id="question" rows="3" placeholder="Type your question here..."></textarea>
      <button id="ask-btn" type="button">Submit</button>
      <p id="status"></p>
    </section>

    <section>
      <div id="answer" hidden>
        <h2>Answer</h2>

        <p id="qtype-pill" hidden></p>
        <p id="tool-pill" hidden></p>

        <p id="answer-text"></p>

        <details id="sources" hidden>
          <summary>Sources</summary>
          <ul id="sources-list"></ul>
        </details>
      </div>
    </section>
  </main>

  <footer>
    <p>Built in the AI Engineering Bootcamp.</p>
  </footer>

  <script src="app.js" defer></script>
</body>
</html>
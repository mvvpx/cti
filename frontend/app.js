const form = document.getElementById("search-form");
const results = document.getElementById("results");

function renderResults(payload) {
  results.innerHTML = "";
  if (!payload.snippets.length) {
    results.innerHTML = "<p class=\"muted\">No results returned.</p>";
    return;
  }

  payload.snippets.forEach((snippet) => {
    const card = document.createElement("article");
    card.className = "result-card";
    card.innerHTML = `
      <h3>${snippet.source.toUpperCase()} · ${snippet.url}</h3>
      <p>${snippet.snippet}</p>
      <p class="muted">Extracted at ${snippet.extracted_at}</p>
    `;
    results.appendChild(card);
  });
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const keyword = document.getElementById("keyword").value.trim();
  const maxResults = Number(document.getElementById("max-results").value);
  const sources = Array.from(document.querySelectorAll("input[name='sources']:checked")).map(
    (input) => input.value
  );

  results.innerHTML = "<p class=\"muted\">Collecting intelligence...</p>";

  try {
    const response = await fetch("http://localhost:8000/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        keyword,
        sources,
        max_results: maxResults,
      }),
    });

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const payload = await response.json();
    renderResults(payload);
  } catch (error) {
    results.innerHTML = `
      <p class="muted">Unable to reach the API: ${error.message}</p>
    `;
  }
});

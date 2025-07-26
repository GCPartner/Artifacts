Working example of MCP Tool and before_tool_callback

<h2 id="prerequisites">Prerequisites<a class="headerlink" href="https://google.github.io/adk-docs/tools/mcp-tools/#prerequisites" title="Permanent link">¶</a></h2>
<p>Before you begin, ensure you have the following set up:</p>

<ul>
<li><strong>Set up ADK:</strong> Follow the standard ADK <a href="https://google.github.io/adk-docs/get-started/quickstart/#venv-install">setup instructions</a> in the quickstart.</li>
<li><strong>Install/update Python/Java:</strong> MCP requires Python version of 3.9 or higher for Python or Java 17+.</li>
<li><strong>Setup Node.js and npx:</strong> <strong>(Python only)</strong> Many community MCP servers are distributed as Node.js packages and run using <code>npx</code>. Install Node.js (which includes npx) if you haven't already. For details, see <a href="https://nodejs.org/en">https://nodejs.org/en</a>.</li>
<li><strong>Verify Installations:</strong> <strong>(Python only)</strong> Confirm <code>adk</code> and <code>npx</code> are in your PATH within the activated virtual environment:</li>
</ul>

<div class="language-shell highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 &gt; code"></button><code class="md-code__content"><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1" href="https://google.github.io/adk-docs/tools/mcp-tools/#__codelineno-0-1"></a><span class="c1"># Both commands should print the path to the executables.</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2" href="https://google.github.io/adk-docs/tools/mcp-tools/#__codelineno-0-2"></a>which<span class="w"> </span>adk
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3" href="https://google.github.io/adk-docs/tools/mcp-tools/#__codelineno-0-3"></a>which<span class="w"> </span>npx
</span></code></pre></div>

Create .env file with

```
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your project
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_MAPS_API_KEY=your API key
```

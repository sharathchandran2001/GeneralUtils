# GeneralUtils
General utils
"""

<style>
  .config-form {
    font-family: Arial, sans-serif;
    border: 1px solid #FFA500;
    padding: 16px;
    border-radius: 8px;
    max-width: 550px;
    background-color: #e6f0ff;
  }

  .form-group {
    margin-bottom: 14px;
  }

  .form-group label {
    font-weight: bold;
    display: block;
    margin-bottom: 4px;
    color: #333;
  }

  .form-description {
    font-size: 12px;
    color: #666;
    margin-bottom: 6px;
  }

  select, input[type="text"] {
    padding: 6px;
    border-radius: 4px;
    border: 1px solid #ccc;
    width: 100%;
  }

  #generateBtn {
    background-color: #FFA500;
    color: white;
    border: none;
    padding: 10px 18px;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
  }

  #generateBtn:hover {
    background-color: #e69500;
  }

  .config-note {
    font-size: 13px;
    font-style: italic;
    margin-top: 18px;
    color: #333;
  }

  #configOutput {
    margin-top: 8px;
    background: #f0f0f0;
    padding: 12px;
    border-radius: 6px;
    white-space: pre-wrap;
    font-family: monospace;
    border: 1px dashed #ccc;
  }
</style>

<div class="config-form">
  <div class="form-group">
    <label for="runRemote">Run Remote</label>
    <div class="form-description">
      If true, the task will be executed on a remote server. Use this for distributed environments.
    </div>
    <select id="runRemote">
      <option value="true">true</option>
      <option value="false">false</option>
    </select>
  </div>

  <div class="form-group">
    <label for="parallel">Parallel Execution</label>
    <div class="form-description">
      Enables parallel task execution. Improves speed but may consume more resources.
    </div>
    <select id="parallel">
      <option value="true">true</option>
      <option value="false">false</option>
    </select>
  </div>

  <div class="form-group">
    <label>Grid URL</label>
    <div class="form-description">
      This is the remote Selenium Grid endpoint where tests will be run.
    </div>
    <input type="text" id="gridURL" value="https://gridul.com" readonly>
  </div>

  <div class="form-group">
    <label for="jiraxrayP">Jira Xray Project Key</label>
    <div class="form-description">
      Select the Jira Xray project key associated with this test run.
    </div>
    <select id="jiraxrayP">
      <option value="abc">abc</option>
      <option value="def">def</option>
      <option value="xyz">xyz</option>
    </select>
  </div>

  <button id="generateBtn" onclick="generateConfig()">Generate Config</button>

  <div class="config-note">
    📋 You can copy and paste the output below directly into your <code>config.properties</code> file:
  </div>
  <pre id="configOutput"></pre>
</div>

<script>
  function generateConfig() {
    const runRemote = document.getElementById("runRemote").value;
    const parallel = document.getElementById("parallel").value;
    const gridURL = document.getElementById("gridURL").value;
    const jiraxrayP = document.getElementById("jiraxrayP").value;

    const output = 
`runRemote=${runRemote}
parallel=${parallel}
gridURL=${gridURL}
jiraxray.P=${jiraxrayP}`;

    document.getElementById("configOutput").innerText = output;
  }
</script>
"""

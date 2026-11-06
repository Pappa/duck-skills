## skillgrade error

```
ACP Agent error: toClient is not a function
```

## Cause

Skillgrade **0.5.0** wires the ACP SDK like this (from your installed `dist/agents/acp.js`):

```128:133:/home/pappa/.nvm/versions/node/v24.20.0/lib/node_modules/skillgrade/dist/agents/acp.js
        const stream = acp.ndJsonStream(stdoutWeb, stdinWeb);
        // Create client handler
        const clientHandler = this.createClientHandler();
        // Create client-side connection
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        this.connection = new acp.ClientSideConnection(clientHandler, stream);
```

But **`@agentclientprotocol/sdk` 0.19.x** defines `ClientSideConnection` like this:

```467:468:/home/pappa/.nvm/versions/node/v24.20.0/lib/node_modules/skillgrade/node_modules/@agentclientprotocol/sdk/dist/acp.js
    constructor(toClient, stream) {
        const client = toClient(this);
```

The first parameter must be a **function** `(agent) => Client`. Skillgrade passes the **handler object** from `createClientHandler()`, so `toClient` is an object. Invoking it throws **`toClient is not a function`**.

So this is a **Skillgrade ↔ ACP SDK API mismatch**, not something wrong with your Cursor CLI or `eval.yaml`.

There is likely a **second bug** in the same file: `ndJsonStream` is documented as `(output, input)` = **writable** (to the process) then **readable** (from the process). For a child process that should be **`stdin` then `stdout`**, but Skillgrade passes **`stdout`, `stdin`**. That may bite you after the constructor is fixed.

## What you can do

### 1. One-line patch (fastest)

Edit `dist/agents/acp.js` in your global Skillgrade install (same path as above) and change the connection line to wrap the handler in a function:

```javascript
this.connection = new acp.ClientSideConnection(() => clientHandler, stream);
```

Optionally fix the stream line to match the SDK’s `ndJsonStream(output, input)` semantics (writable → child stdin, readable ← child stdout):

```javascript
const stream = acp.ndJsonStream(stdinWeb, stdoutWeb);
```

(Patching `node_modules` is brittle; see below for something sturdier.)

### 2. **patch-package** / **pnpm patch** / fork

Keep the same two-line fix via a patch so reinstalls don’t drop it.

### 3. **Upstream**

Open an issue or PR on [mgechev/skillgrade](https://github.com/mgechev/skillgrade): `ClientSideConnection` now requires a **factory**; Skillgrade still passes a plain **client object**.

### 4. **Workaround without ACP**

Use **`agent: command`** and a small script that drives the Cursor **Python/TS SDK** (`Agent.prompt`), which avoids Skillgrade’s ACP adapter entirely until it’s fixed.

---

**Bottom line:** the JSON error is from Skillgrade calling **`ClientSideConnection`** with the wrong first-argument shape for **`@agentclientprotocol/sdk` 0.19**. Wrapping the handler as **`() => clientHandler`** (and fixing **`ndJsonStream`** argument order) aligns with the current SDK.
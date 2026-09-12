# Web frontend

The browser editor uses a PlayCanvas adapter so WebGL2/WebGPU capability can be selected by the runtime. The viewport is a preview integration point for the shared Chimera scene/interchange model.

## Development

```bash
npm install
npm run dev
```

## Production

```bash
npm run build
```

The web frontend is designed for later hosted collaboration and scene synchronization; authentication and server-side persistence must be added before exposing collaborative editing publicly.

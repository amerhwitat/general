import * as pc from 'playcanvas';

export function createViewport(canvas: HTMLCanvasElement): pc.Application {
  const app = new pc.Application(canvas, {
    graphicsDeviceOptions: { antialias: true, alpha: false },
  });
  app.setCanvasFillMode(pc.FILLMODE_FILL_WINDOW);
  app.setCanvasResolution(pc.RESOLUTION_AUTO);
  return app;
}

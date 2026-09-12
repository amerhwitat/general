import * as pc from 'playcanvas';
import { createViewport } from './viewport';

const canvas = document.querySelector<HTMLCanvasElement>('#viewport');
if (!canvas) throw new Error('Missing #viewport canvas');

const app = createViewport(canvas);
const camera = new pc.Entity('Camera');
camera.addComponent('camera', { clearColor: new pc.Color(0.04, 0.04, 0.05) });
camera.setPosition(0, 0, 4);
app.root.addChild(camera);

const light = new pc.Entity('Key');
light.addComponent('light', { type: 'directional', intensity: 2 });
light.setEulerAngles(35, 45, 0);
app.root.addChild(light);

const box = new pc.Entity('PreviewMesh');
box.addComponent('render', { type: 'box' });
app.root.addChild(box);

app.start();
window.addEventListener('resize', () => app.resizeCanvas());

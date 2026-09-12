import * as pc from 'playcanvas';
const canvas=document.querySelector<HTMLCanvasElement>('#viewport')!;
const app=new pc.Application(canvas,{graphicsDeviceOptions:{powerPreference:'high-performance'}});
app.setCanvasFillMode(pc.FILLMODE_FILL_WINDOW); app.setCanvasResolution(pc.RESOLUTION_AUTO);
const camera=new pc.Entity('Camera'); camera.addComponent('camera',{clearColor:new pc.Color(0.04,0.04,0.05)}); app.root.addChild(camera); camera.setPosition(0,0,4);
const light=new pc.Entity('Key'); light.addComponent('light',{type:'directional',intensity:2}); light.setEulerAngles(35,45,0); app.root.addChild(light);
const box=new pc.Entity('PreviewMesh'); box.addComponent('render',{type:'box'}); app.root.addChild(box); app.start();
window.addEventListener('resize',()=>app.resizeCanvas());

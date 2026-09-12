import { useEffect, useState } from 'react';
export type Project={id:string;name:string;methodology:string};
export function App(){const [projects,setProjects]=useState<Project[]>([]);useEffect(()=>{fetch('/api/projects').then(r=>r.json()).then(setProjects).catch(()=>{});},[]);return <main><h1>Chimera WorkFlow Studio</h1><p>Agile · DevOps · ITIL 4 · AI · Observability</p><ul>{projects.map(p=><li key={p.id}>{p.name} — {p.methodology}</li>)}</ul></main>}

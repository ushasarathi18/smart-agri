import React, { useEffect, useState } from 'react';
import api from '../services/api';
export default function Schemes() {
  const [s,setS]=useState([]); const [soils,setSoils]=useState([]); const [w,setW]=useState(null);
  useEffect(()=>{api.get('/info/schemes/').then(r=>setS(r.data));
                  api.get('/info/soils/').then(r=>setSoils(r.data));
                  api.get('/info/weather/').then(r=>setW(r.data));},[]);
  return (<div><h2>🏛️ Government Schemes</h2>
    <div className="grid">{s.map((x,i)=><div key={i} className="card"><h4>{x.name}</h4><p>{x.benefit}</p><a href={x.link} target="_blank" rel="noreferrer">Visit →</a></div>)}</div>
    <h2>🌱 Soil & Crop Suitability</h2>
    <div className="grid">{soils.map((x,i)=><div key={i} className="card"><h4>{x.type} Soil</h4><p>Best: {x.crops.join(', ')}</p></div>)}</div>
    {w && <><h2>☁️ Weather & Seasons</h2>
      <div className="grid">{w.seasons.map((x,i)=><div key={i} className="card"><h4>{x.season}</h4><p>Crops: {x.crops}</p><small>{x.tip}</small></div>)}</div></>}
  </div>);
}

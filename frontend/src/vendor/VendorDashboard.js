import React, { useEffect, useState } from 'react';
import api from '../services/api';
export default function VendorDashboard() {
  const [v,setV]=useState([]);
  useEffect(()=>{api.get('/vendors/').then(r=>setV(r.data));},[]);
  return (<div><h2>🤝 Vendor Network</h2>
    <div className="grid">{v.map(x=><div key={x.id} className="card">
      <h4>{x.business}</h4><p>{x.state} {x.verified&&<span className="tag">Verified</span>}</p>
      <p>⭐ {x.rating}</p></div>)}</div>
  </div>);
}

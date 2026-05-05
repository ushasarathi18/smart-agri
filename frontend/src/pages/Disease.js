import React, { useState } from 'react';
import api from '../services/api';
export default function Disease() {
  const [file,setFile]=useState(null); const [res,setRes]=useState(null); const [loading,setLoading]=useState(false);
  const submit=async()=>{
    if(!file) return;
    setLoading(true);
    const fd = new FormData(); fd.append('image',file);
    try { const r = await api.post('/disease/detect/',fd,{headers:{'Content-Type':'multipart/form-data'}});
          setRes(r.data); } finally { setLoading(false); }
  };
  return (<div>
    <h2>🔬 Disease & Defect Detection</h2>
    <div className="card">
      <p>Upload a leaf or crop image. AI returns disease, severity, pesticide & organic alternatives.</p>
      <input type="file" accept="image/*" onChange={e=>setFile(e.target.files[0])}/>
      <button className="btn" disabled={!file||loading} onClick={submit}>{loading?'Analyzing...':'Detect'}</button>
    </div>
    {res && <div className="card">
      <h3>{res.details.name} ({res.confidence}% confidence)</h3>
      <p><b>Severity:</b> {res.details.severity}</p>
      <p><b>Pesticide:</b> {res.details.pesticide} — {res.details.dosage}, every {res.details.interval}</p>
      <p><b>Organic alternative:</b> {res.details.organic}</p>
      <p><b>Precautions:</b> {res.details.precautions}</p>
      <p><b>Prevention:</b> {res.details.prevention}</p>
      <small>{res.note}</small>
    </div>}
  </div>);
}

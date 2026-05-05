import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../services/api';
export default function ProductDetail() {
  const { id } = useParams();
  const [p,setP]=useState(null); const [qty,setQty]=useState(1);
  useEffect(()=>{api.get(`/products/${id}/`).then(r=>setP(r.data));},[id]);
  if (!p) return <div className="card">Loading...</div>;
  return (<div>
    <div className="card" style={{display:'grid',gridTemplateColumns:'300px 1fr',gap:20}}>
      <img src={p.image_url} alt="" style={{width:'100%',borderRadius:8}}/>
      <div>
        <h2>{p.title}</h2>
        <div className="price">₹{p.selling_price}</div>
        <div className={p.stock<10?'stock-low':'stock-ok'}>{p.stock>0?`${p.stock} in stock`:'Out of stock'}</div>
        <p style={{margin:'10px 0'}}>{p.description}</p>
        <div><span className="tag">Soil: {p.soil_suitability||'All'}</span><span className="tag">State: {p.state||'India'}</span></div>
        <input type="number" min="1" max={p.stock} value={qty} onChange={e=>setQty(+e.target.value)} style={{width:100}}/>
        <Link to={`/checkout/${p.id}?q=${qty}`} className="btn">Buy Now</Link>
      </div>
    </div>
    <div className="card"><h3>Cultivation Guide</h3><p>{p.cultivation_guide||'Standard farming practices apply.'}</p></div>
    <div className="card"><h3>Storage</h3><p>{p.storage_info||'Cool, dry place.'}</p></div>
    <div className="card"><h3>Reviews ({p.reviews_count})</h3>
      {(p.reviews||[]).map((r,i)=><div key={i} style={{borderBottom:'1px solid var(--border)',padding:8}}>
        <b>{r.user}</b> {'⭐'.repeat(r.rating)} {r.verified&&<span className="tag">Verified</span>}
        <p>{r.comment}</p></div>)}
    </div>
  </div>);
}

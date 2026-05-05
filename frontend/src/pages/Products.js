import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
export default function Products() {
  const [items,setItems]=useState([]); const [q,setQ]=useState('');
  useEffect(()=>{api.get(`/products/?q=${q}`).then(r=>setItems(r.data));},[q]);
  return (<div>
    <h2>🛒 Agri Marketplace</h2>
    <input placeholder="Search seeds, fertilizers, machinery..." value={q} onChange={e=>setQ(e.target.value)} />
    {items.length===0 && <div className="card">No products yet. Admin can add via /admin/ panel or load fixtures.</div>}
    <div className="grid">
      {items.map(p=>(
        <Link key={p.id} to={`/products/${p.id}`} className="product-card" style={{textDecoration:'none',color:'inherit'}}>
          <img src={p.image_url} alt={p.title} />
          <div className="body">
            <h4>{p.title}</h4>
            <div className="price">₹{p.selling_price}</div>
            <div className={p.stock<10?'stock-low':'stock-ok'}>
              {p.stock>0?`In stock: ${p.stock}`:'Out of stock'}
            </div>
            <small>⭐ {p.avg_rating} ({p.reviews_count} reviews)</small>
          </div>
        </Link>
      ))}
    </div>
  </div>);
}

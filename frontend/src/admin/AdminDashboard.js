import React, { useEffect, useState } from 'react';
import api from '../services/api';
export default function AdminDashboard() {
  const [d,setD]=useState(null); const [w,setW]=useState([]);
  useEffect(()=>{api.get('/analytics/dashboard/').then(r=>setD(r.data));
                  api.get('/warehouse/').then(r=>setW(r.data));},[]);
  if(!d) return <div className="card">Loading...</div>;
  return (<div><h2>🛡️ Admin Dashboard</h2>
    <div className="grid">
      <div className="card"><h4>Users</h4><div className="price">{d.total_users}</div></div>
      <div className="card"><h4>Products</h4><div className="price">{d.total_products}</div></div>
      <div className="card"><h4>Orders</h4><div className="price">{d.total_orders}</div></div>
      <div className="card"><h4>Revenue</h4><div className="price">₹{d.revenue.toFixed(2)}</div></div>
    </div>
    <div className="card"><h3>⚠️ Low Stock</h3>
      {d.low_stock.length===0?<p>All good</p>:<ul>{d.low_stock.map(p=><li key={p.id}>{p.title} — {p.stock}</li>)}</ul>}
    </div>
    <div className="card"><h3>🏭 Warehouses</h3>
      <table><thead><tr><th>Name</th><th>State</th><th>Used / Capacity</th></tr></thead>
      <tbody>{w.map(x=><tr key={x.id}><td>{x.name}</td><td>{x.state}</td><td>{x.used}/{x.capacity}</td></tr>)}</tbody></table>
    </div>
    <p>Full management: <a href="http://127.0.0.1:8000/admin/" target="_blank" rel="noreferrer">/admin/</a></p>
  </div>);
}

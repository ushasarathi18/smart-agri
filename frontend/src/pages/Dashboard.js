import React, { useEffect, useState } from 'react';
import api from '../services/api';
export default function Dashboard() {
  const [orders,setOrders]=useState([]); const [profile,setProfile]=useState(null);
  useEffect(()=>{api.get('/transactions/my/').then(r=>setOrders(r.data));
                  api.get('/accounts/profile/').then(r=>setProfile(r.data)).catch(()=>{});},[]);
  return (<div><h2>👤 My Dashboard</h2>
    {profile && <div className="card">
      <h3>{profile.username} ({profile.role})</h3>
      <p>📧 {profile.email} · 📱 {profile.phone}</p>
      <p>📍 {profile.district}, {profile.state}</p>
    </div>}
    <h3>My Orders</h3>
    <table className="card"><thead><tr><th>#</th><th>Product</th><th>Qty</th><th>Total</th><th>Status</th><th>Invoice</th></tr></thead>
    <tbody>{orders.map(o=><tr key={o.id}>
      <td>{o.id}</td><td>{o.product}</td><td>{o.quantity}</td><td>₹{o.total}</td><td>{o.status}</td>
      <td><a href={`http://127.0.0.1:8000/api/transactions/invoice/${o.id}/`} target="_blank" rel="noreferrer">📄</a></td>
    </tr>)}</tbody></table>
  </div>);
}

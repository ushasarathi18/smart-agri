import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Link } from 'react-router-dom';
export default function Cart() {
  const [items,setItems]=useState([]);
  useEffect(()=>{api.get('/products/cart/').then(r=>setItems(r.data));},[]);
  const total = items.reduce((s,i)=>s+i.total,0);
  return (<div><h2>🛍️ Cart</h2>
    {items.length===0?<div className="card">Your cart is empty. <Link to="/products">Browse products</Link></div>:
    <>{items.map(i=><div key={i.id} className="card">
      <b>{i.product.title}</b> × {i.quantity} = ₹{i.total}
      <Link className="btn" style={{float:'right'}} to={`/checkout/${i.product.id}?q=${i.quantity}`}>Checkout</Link>
    </div>)}<div className="card"><h3>Total: ₹{total.toFixed(2)}</h3></div></>}
  </div>);
}

import React, { useState } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import api from '../services/api';
export default function Checkout() {
  const { id } = useParams();
  const [sp] = useSearchParams();
  const [method,setMethod]=useState('upi');
  const [addr,setAddr]=useState(''); const [state,setState]=useState('');
  const [res,setRes]=useState(null);
  const place=()=>api.post('/transactions/create/',{
    product_id:id, quantity:+(sp.get('q')||1), payment_method:method, address:addr, state
  }).then(r=>setRes(r.data)).catch(e=>alert(e.response?.data?.error||'Error'));
  return (<div><h2>💳 Checkout</h2>
    {!res?<div className="card">
      <textarea placeholder="Delivery address" value={addr} onChange={e=>setAddr(e.target.value)}/>
      <input placeholder="State" value={state} onChange={e=>setState(e.target.value)}/>
      <select value={method} onChange={e=>setMethod(e.target.value)}>
        <option value="cod">Cash on Delivery</option><option value="upi">UPI/GPay</option>
        <option value="qr">QR Code</option><option value="online">Online Card</option>
      </select>
      <button className="btn" onClick={place}>Place Order</button>
    </div>:<div className="card">
      <h3>✅ Order #{res.order_id} placed!</h3>
      <p>Base: ₹{res.base_price} + GST: ₹{res.gst} + Transport: ₹{res.transport}</p>
      <h2 className="price">Total: ₹{res.total}</h2>
      {res.qr_code && <img src={res.qr_code} alt="QR" style={{maxWidth:240}}/>}
      <p><a href={res.upi_link}>Open in UPI app</a></p>
      <a className="btn" href={`http://127.0.0.1:8000/api/transactions/invoice/${res.order_id}/`} target="_blank" rel="noreferrer">📄 Download Invoice PDF</a>
      <p>Stock left: {res.remaining_stock}</p>
    </div>}
  </div>);
}

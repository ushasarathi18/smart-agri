import React, { useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';
export default function Register() {
  const nav=useNavigate();
  const [f,setF]=useState({username:'',email:'',password:'',role:'user',phone:'',state:'',district:''});
  const ch=(k,v)=>setF({...f,[k]:v});
  const submit=()=>api.post('/accounts/register/',f).then(r=>{
    localStorage.setItem('token',r.data.access);
    localStorage.setItem('user',JSON.stringify(r.data.user));
    nav('/dashboard');
  }).catch(e=>alert(e.response?.data?.error||'Failed'));
  return (<div><h2>📝 Register</h2><div className="card">
    {['username','email','password','phone','state','district'].map(k=>
      <input key={k} placeholder={k} type={k==='password'?'password':'text'} value={f[k]} onChange={e=>ch(k,e.target.value)}/>)}
    <select value={f.role} onChange={e=>ch('role',e.target.value)}>
      <option value="user">Farmer/User</option><option value="seller">Seller</option><option value="vendor">Vendor</option>
    </select>
    <button className="btn" onClick={submit}>Register</button>
  </div></div>);
}

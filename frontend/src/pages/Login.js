import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import { AppContext } from '../context/AppContext';
export default function Login() {
  const { setUser } = useContext(AppContext);
  const nav = useNavigate();
  const [u,setU]=useState(''); const [p,setP]=useState(''); const [err,setErr]=useState('');
  const submit=async()=>{
    try { const r = await api.post('/accounts/login/',{username:u,password:p});
      localStorage.setItem('token',r.data.access);
      localStorage.setItem('user',JSON.stringify(r.data.user));
      setUser(r.data.user); nav('/dashboard');
    } catch (e) { setErr(e.response?.data?.error||'Login failed'); }
  };
  return (<div><h2>🔐 Login</h2><div className="card">
    <input placeholder="Username" value={u} onChange={e=>setU(e.target.value)}/>
    <input type="password" placeholder="Password" value={p} onChange={e=>setP(e.target.value)}/>
    <button className="btn" onClick={submit}>Login</button>
    {err && <div style={{color:'red'}}>{err}</div>}
    <small>Defaults: admin/admin123 · seller/seller123 · vendor/vendor123 · user/user123</small>
  </div></div>);
}

import React, { useState } from 'react';
import api from '../services/api';
export default function Chatbot() {
  const [m,setM]=useState([{from:'bot',text:'👋 Hi! Ask me about prices, diseases, schemes, soil, payments.'}]);
  const [t,setT]=useState('');
  const send=async()=>{
    if(!t.trim())return;
    const u=t; setT(''); setM(x=>[...x,{from:'me',text:u}]);
    const r = await api.post('/chatbot/chat/',{message:u});
    setM(x=>[...x,{from:'bot',text:r.data.reply}]);
  };
  return (<div><h2>🤖 AI Farmer Advisor</h2>
    <div className="card" style={{minHeight:300,maxHeight:400,overflowY:'auto'}}>
      {m.map((x,i)=><div key={i} style={{textAlign:x.from==='me'?'right':'left',margin:'8px 0'}}>
        <span style={{display:'inline-block',padding:'8px 12px',borderRadius:12,
                      background:x.from==='me'?'var(--primary)':'var(--border)',
                      color:x.from==='me'?'#fff':'inherit'}}>{x.text}</span>
      </div>)}
    </div>
    <div className="card" style={{display:'flex',gap:8}}>
      <input value={t} onChange={e=>setT(e.target.value)} onKeyDown={e=>e.key==='Enter'&&send()} placeholder="Ask anything..." />
      <button className="btn" onClick={send}>Send</button>
    </div>
  </div>);
}

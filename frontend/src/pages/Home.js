import React from 'react';
import { Link } from 'react-router-dom';
export default function Home() {
  return (
    <div>
      <div className="hero">
        <h1>🌾 Smart Agri Market & Disease Detection</h1>
        <p>India's complete AI-powered agriculture ecosystem — 25+ crops, all states, real-time pricing, disease detection, and marketplace.</p>
      </div>
      <div className="grid">
        {[
          {t:'📊 Live Market Prices',d:'Buying & selling prices for 25+ crops across 15+ states.',l:'/market'},
          {t:'🛒 Agri Marketplace',d:'Seeds, fertilizers, pesticides, machinery — real-time stock.',l:'/products'},
          {t:'🔬 Disease Detection',d:'AI-powered leaf & crop disease detection with treatment.',l:'/disease'},
          {t:'🏛️ Govt Schemes',d:'PM-KISAN, PMFBY, KCC and more.',l:'/schemes'},
          {t:'🤖 AI Farmer Chatbot',d:'24/7 AI advisor for prices, diseases, and farming tips.',l:'/chatbot'},
          {t:'📈 Price Forecasting',d:'Weekly, monthly & seasonal price predictions.',l:'/market'},
        ].map((c,i)=> <Link to={c.l} key={i} className="card" style={{textDecoration:'none',color:'inherit'}}>
          <h3>{c.t}</h3><p style={{marginTop:8}}>{c.d}</p>
        </Link>)}
      </div>
    </div>
  );
}

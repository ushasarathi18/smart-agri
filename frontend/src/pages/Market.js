import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';
import api from '../services/api';
export default function Market() {
  const [crops,setCrops]=useState([]); const [locs,setLocs]=useState([]);
  const [crop,setCrop]=useState('rice'); const [loc,setLoc]=useState('karnataka');
  const [data,setData]=useState(null); const [dyn,setDyn]=useState(null);
  useEffect(()=>{api.get('/market/crops/').then(r=>setCrops(r.data));
                  api.get('/market/locations/').then(r=>setLocs(r.data));},[]);
  const load=()=>{api.get(`/market/history/?crop=${crop}&location=${loc}`).then(r=>setData(r.data)).catch(()=>setData(null));
                  api.get(`/market/dynamic-price/?crop=${crop}&location=${loc}`).then(r=>setDyn(r.data));};
  useEffect(load,[crop,loc]);
  const chart = data && {
    labels:[...data.history.map(h=>h.date),...data.forecast.map(f=>f.date)],
    datasets:[
      {label:'Selling ₹',data:[...data.history.map(h=>h.selling_price),...Array(data.forecast.length).fill(null)],borderColor:'#2e7d32',tension:0.3},
      {label:'Buying ₹',data:[...data.history.map(h=>h.buying_price),...Array(data.forecast.length).fill(null)],borderColor:'#ff9800',tension:0.3},
      {label:'Forecast ₹',data:[...Array(data.history.length).fill(null),...data.forecast.map(f=>f.predicted_price)],borderColor:'#1976d2',borderDash:[6,4],tension:0.3},
    ]};
  return (<div>
    <h2>📊 Market Prices & Forecast</h2>
    <div className="card" style={{display:'flex',gap:12}}>
      <select value={crop} onChange={e=>setCrop(e.target.value)}>{crops.map(c=><option key={c}>{c}</option>)}</select>
      <select value={loc} onChange={e=>setLoc(e.target.value)}>{locs.map(l=><option key={l}>{l}</option>)}</select>
    </div>
    {data && <>
      <div className="grid" style={{gridTemplateColumns:'repeat(auto-fit,minmax(200px,1fr))'}}>
        <div className="card"><b>Current Selling</b><div className="price">₹{data.current.selling_price}</div></div>
        <div className="card"><b>Current Buying</b><div className="price">₹{data.current.buying_price}</div></div>
        <div className="card"><b>Best Sell Location</b><div>{data.best_sell_location.name}<br/>₹{data.best_sell_location.price}</div></div>
        <div className="card"><b>Best Buy Location</b><div>{data.best_buy_location.name}<br/>₹{data.best_buy_location.price}</div></div>
        <div className="card"><b>India Average</b><div className="price">₹{data.india_average}</div></div>
        {dyn && <div className="card"><b>🔥 Dynamic Price</b><div className="price">₹{dyn.dynamic_price}</div>
          <small>weather × season × demand × festival × govt</small></div>}
      </div>
      <div className="card"><Line data={chart} /></div>
    </>}
  </div>);
}

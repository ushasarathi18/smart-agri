import React, { useContext } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import { AppProvider, AppContext } from './context/AppContext';
import Home from './pages/Home';
import Market from './pages/Market';
import Products from './pages/Products';
import ProductDetail from './pages/ProductDetail';
import Disease from './pages/Disease';
import Cart from './pages/Cart';
import Checkout from './pages/Checkout';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import AdminDashboard from './admin/AdminDashboard';
import SellerDashboard from './seller/SellerDashboard';
import VendorDashboard from './vendor/VendorDashboard';
import Schemes from './pages/Schemes';
import Chatbot from './pages/Chatbot';
import About from './pages/About';

function Nav() {
  const { theme, setTheme, lang, setLang, user, setUser } = useContext(AppContext);
  return (
    <nav className="navbar">
      <div><Link to="/" className="brand">🌾 Smart Agri</Link></div>
      <div>
        <Link to="/market">Market</Link>
        <Link to="/products">Shop</Link>
        <Link to="/disease">Disease</Link>
        <Link to="/schemes">Schemes</Link>
        <Link to="/chatbot">AI Help</Link>
        <Link to="/cart">Cart</Link>
        <Link to="/dashboard">Dashboard</Link>
        {user?.role === 'admin' && <Link to="/admin">Admin</Link>}
        {user?.role === 'seller' && <Link to="/seller">Seller</Link>}
        {user?.role === 'vendor' && <Link to="/vendor">Vendor</Link>}
      </div>
      <div style={{display:'flex',alignItems:'center',gap:8}}>
        <select value={lang} onChange={e=>setLang(e.target.value)} style={{padding:4,color:'#000'}}>
          <option value="en">EN</option><option value="hi">हि</option><option value="kn">ಕ</option>
          <option value="ta">த</option><option value="te">తె</option>
        </select>
        <button className="btn" onClick={()=>setTheme(theme==='light'?'dark':'light')}>
          {theme==='light'?'🌙':'☀️'}
        </button>
        {user ? <button className="btn" onClick={()=>{localStorage.clear();setUser(null);}}>Logout ({user.username})</button>
              : <Link to="/login" style={{color:'#fff'}}>Login</Link>}
      </div>
    </nav>
  );
}

export default function App() {
  return (
    <AppProvider>
      <Nav />
      <main className="container">
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/market" element={<Market/>} />
          <Route path="/products" element={<Products/>} />
          <Route path="/products/:id" element={<ProductDetail/>} />
          <Route path="/disease" element={<Disease/>} />
          <Route path="/cart" element={<Cart/>} />
          <Route path="/checkout/:id" element={<Checkout/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/register" element={<Register/>} />
          <Route path="/dashboard" element={<Dashboard/>} />
          <Route path="/admin" element={<AdminDashboard/>} />
          <Route path="/seller" element={<SellerDashboard/>} />
          <Route path="/vendor" element={<VendorDashboard/>} />
          <Route path="/schemes" element={<Schemes/>} />
          <Route path="/chatbot" element={<Chatbot/>} />
          <Route path="/about" element={<About/>} />
        </Routes>
      </main>
      <a className="whatsapp-float" href="https://wa.me/919606610568" target="_blank" rel="noreferrer">💬 WhatsApp</a>
      <footer>© 2026 Smart Agri Market & Disease Detection System | All India Coverage 🇮🇳</footer>
    </AppProvider>
  );
}

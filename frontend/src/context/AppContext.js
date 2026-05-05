import React, { createContext, useState, useEffect } from 'react';
export const AppContext = createContext();
export function AppProvider({ children }) {
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light');
  const [lang, setLang] = useState(localStorage.getItem('lang') || 'en');
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user') || 'null'));
  useEffect(() => { document.body.dataset.theme = theme; localStorage.setItem('theme',theme); }, [theme]);
  useEffect(() => { localStorage.setItem('lang',lang); }, [lang]);
  return <AppContext.Provider value={{theme,setTheme,lang,setLang,user,setUser}}>{children}</AppContext.Provider>;
}

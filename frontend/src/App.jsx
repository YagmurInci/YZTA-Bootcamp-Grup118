import React from 'react';

export default function App() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#FAF9F6' }}>
      
      {/* Gezi Kartı */}
      <div style={{
        backgroundColor: '#FFFFFF',
        padding: '24px',
        borderRadius: '16px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.05)',
        maxWidth: '320px',
        border: '2px solid #FADADD', /* Pastel Pembe Çerçeve */
        fontFamily: 'sans-serif'
      }}>
        <h2 style={{ color: '#5C6B73', margin: '0 0 8px 0' }}>📍 Moda Sahili</h2>
        <p style={{ color: '#9DB4C0', fontSize: '15px', lineHeight: '1.5' }}>
          Güneş batarken yürüyüş yapmak için harika bir lokasyon. Sakin ve huzurlu.
        </p>
        
        {/* Etiketler */}
        <div style={{ marginTop: '16px', display: 'flex', gap: '8px' }}>
          <span style={{ backgroundColor: '#E6E6FA', padding: '6px 12px', borderRadius: '12px', fontSize: '12px', color: '#483D8B', fontWeight: 'bold' }}>
            #cozy
          </span>
          <span style={{ backgroundColor: '#FFDAB9', padding: '6px 12px', borderRadius: '12px', fontSize: '12px', color: '#D2691E', fontWeight: 'bold' }}>
            #yürüyüş
          </span>
        </div>
      </div>

    </div>
  );
}
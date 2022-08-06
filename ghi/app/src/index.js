import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


async function loadInventory() {
  const manufacturerResponse = await fetch('http://localhost:8100/api/manufacturers/');
  const automobileResponse = await fetch('http://localhost:8100/api/automobiles/');
  const serviceResponse = await fetch('http://localhost:8080/api/service/');
  
  let manufacturerData, automobileData, serviceData;

  if (manufacturerResponse.ok) {
    manufacturerData = await manufacturerResponse.json();
  } else {
    console.error(manufacturerResponse);
  }

  if (automobileResponse.ok) {
    automobileData = await automobileResponse.json();
  } else {
    console.error(automobileResponse);
  }

  if (serviceResponse.ok) {
    serviceData = await serviceResponse.json();
  } else {
    console.error(serviceResponse);
  }

  root.render(
    <React.StrictMode>
        <App manufacturers={manufacturerData} automobiles={automobileData} />
    </React.StrictMode>
  );
}

loadInventory();

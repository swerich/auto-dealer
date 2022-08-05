import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import ManufacturerList from './ManufacturerList';
import VehicleModels from './VehicleModels.js';
import AutomobileForm from './AutomobileForm';
import NewVehicleModelForm from './NewVehicleModelForm';
import AutomobileList from './AutomobileList';
import ManufacturerForm from './ManufacturerForm';
import SaleList from './SaleList'
import SalesPersonForm from './SalesPersonForm';
import SaleRecordForm from './SaleRecordForm';
import NewCustomerForm from './NewCustomerForm';


function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/automobiles/new" element={<AutomobileForm />} />
          <Route path="/sales" element={<SaleList />} />
          <Route path="sales_people/new" element={<SalesPersonForm />} />
          <Route path="/automobiles" element={<AutomobileList />} />
          <Route path="/manufacturers/new" element={<ManufacturerForm />} />
          <Route path="/manufacturers" element={<ManufacturerList />} />
          <Route path="/sales/new" element={<SaleRecordForm />} />
          <Route path="/customers/new" element={<NewCustomerForm />} />





          





          <Route path="/models" element={<VehicleModels />} />
          <Route path="/models/new" element={<NewVehicleModelForm />} />



        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import ManufacturerList from './ManufacturerList';
import VehicleModels from './VehicleModels.js';
import AutomobileForm from './AutomobileForm';
import NewVehicleModelForm from './NewVehicleModelForm';
import AutomobileList from './AutomobileList';
import ManufacturerForm from './ManufacturerForm';
import AppointmentsList from './AppointmentsList';
// import AppointmentForm from '.AppointmentsForm';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/automobiles/new" element={<AutomobileForm />} />
          <Route path="/automobiles" element={<AutomobileList />} />
          <Route path="/manufacturers/new" element={<ManufacturerForm />} />
          <Route path="/manufacturers" element={<ManufacturerList />} />
          <Route path="/appointments" element={<AppointmentsList />} />
          {/* <Route path="/appointments/new" element={<AppointmentForm />} /> */}

          <Route path="/models" element={<VehicleModels />} />
          <Route path="/models/new" element={<NewVehicleModelForm />} />



        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

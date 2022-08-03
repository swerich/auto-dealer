import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
// import ManufacturerList from './ManufacturerList';
import VehicleModels from './VehicleModels.js';
import AutomobileForm from './AutomobileForm';
import NewVehicleModelForm from './NewVehicleModelForm';
import AutomobileList from './AutomobileList';


function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/automobiles/new" element={<AutomobileForm />} />
          <Route path="/automobiles" element={<AutomobileList />} />

          {/* <Route path="manufacturers" element={<ManufacturerList manufacturers={props.manufacturers} />} /> */}
          <Route path="/models" element={<VehicleModels />} />
          <Route path="/models/new" element={<NewVehicleModelForm />} />



        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

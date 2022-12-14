import { NavLink } from 'react-router-dom';

function Nav() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">CarCar</NavLink>
        <NavLink className="navbar-brand" to="/models">Vehicle's</NavLink>
        <NavLink className="navbar-brand" to="/automobiles/new">Automobile Form</NavLink>
        <NavLink className="navbar-brand" to="/automobiles">Automobile List</NavLink>
        <NavLink className="navbar-brand" to="/manufacturers/new">Manufacturer Form</NavLink>
        <NavLink className="navbar-brand" to="/sales_people/new">Add A Sales Person</NavLink>
        <NavLink className="navbar-brand" to="/manufacturers">Manufacturer List</NavLink>
        <NavLink className="navbar-brand" to="/sales_people">Sales person history</NavLink>

        <NavLink className="navbar-brand" to="/sales">All Sales</NavLink>
        <NavLink className="navbar-brand" to="/customers/new">Add a customer</NavLink>
        <NavLink className="navbar-brand" to="/sales/new">Record a new sale</NavLink>

        

        



        
        <NavLink className="navbar-brand" to="/models/create">Add a vehicle model</NavLink>
        <NavLink className="navbar-brand" to="/appointments">Service Appointment List</NavLink>
        <NavLink className="navbar-brand" to="/appointments/new">Add Service Appointment</NavLink>
        <NavLink className="navbar-brand" to="/models/new">Add a Vehicle Model</NavLink>
        <NavLink className="navbar-brand" to="/service_history">Service History</NavLink>
        <NavLink className="navbar-brand" to="/technicians">Technician</NavLink>

        
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Nav;

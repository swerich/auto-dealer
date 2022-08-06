import React from 'react';

class NewTechnicianForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            technician: "",
            employee_number: "",
        }

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangeTechnician = this.handleChangeTechnician.bind(this);
        this.handleChangeEmployee_Number = this.handleChangeEmployee_Number.bind(this)
    }

    async component() {
        const url = 'http://localhost:8080/api/technicians'

        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            this.setState({technicians: data.technicians});

        }
    }
    async handleSubmit(event) {
        event.preventDefault();
        const data = { ...this.state };

        const locationUrl = 'http://localhost:8080/api/technicians'
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const response = await fetch(locationUrl, fetchConfig)
        if (response.ok) {
            const newTechnician = await response.json();
            console.log(newTechnician);
            this.setState({
                technician: "",
            employee_number: "",
            })
        }
    }

    handleChangeTechnician(event) {
        const value = event.target.value;
        this.setState({ technician: value });
    }

    handleChangeEmployee_Number(event) {
        const value = event.target.value;
        this.setState({ employee_number: value});
    }

    render () {
        return (
            <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Add Technician</h1>
                    <form onSubmit={this.handleSubmit} id="create-conference-form">
                        <div className="form-floating mb-3">
                            <input onChange={this.handleChangeTechnician} value={this.state.technician} placeholder="technician" required type="text" name="technician" id="technician" className="form-control" />
                            <label htmlFor="VIN">Tehcnician</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handleChangeEmployee_Number} value={this.state.employee_number} placeholder="employee_number" required type="text" name="employee_number" id="employee_number" className="form-control" />
                            <label htmlFor="customer">Employee Number</label>
                        </div>
                        <button className="btn btn-primary">Add</button>
                    </form>
                </div>
            </div>
        </div>
        );
    }
}

export default NewTechnicianForm;
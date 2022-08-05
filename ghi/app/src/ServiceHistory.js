import React from 'react';


class ServiceHistory extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            customer: "",
            date: "",
            technician: "",
            reason: "",
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangeCustomer = this.handleChangeCustomer.bind(this);
        this.handleChangeDate = this.handleChangeDate.bind(this);
        this.handleChangeTechnician = this.handleChangeTechnician.bind(this);
        this.handleChangeReason = this.handleChangeReason.bind(this);
    }
    async componentDidMount() {
        const url = 'http://localhost:8080/api/appointments';

        const response = await fetch(url);

        if (response.ok) {
            const data = await fetch(url);
            this.setState({service_history: data.service_history});
        }
    }
    async handleSubmit(event) {
        event.preventDefault();
        const data = { ...this.state };

        const locationUrl = 'http://localhost:8080/api/appointments';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'content-type': 'application/json',
            },
        };
        const response = await fetch(locationUrl, fetchConfig)
        if (response.ok) {
            const serviceHistory = await response.json();
            console.log(serviceHistory);
            this.setState({
                customer: "",
                date: "",
                technician: "",
                reason: "",
            })
        }
    }

    handleChangeCustomer(event) {
        const value = event.target.value;
        this.setState({ customer: value });
    }

    handleChangeDate(event) {
        const value = event.target.value;
        this.setState({ date: value });
    }

    handleChangeTechnician(event) {
        const value = event.target.value;
        this.setState({ technician: value });
    }

    handleChangeReason(event) {
        const value = event.target.value;
        this.setState({ reason: value });
    }

    render () {
        return (
            <div className="row">
                <div className="offset-3 col-6">
                    <div className="shadow p-4 mt-4">
                        <h1>Show Service History</h1>
                        <form onSubmit={this.handleSubmit} id="create-conference-form">
                            <div className="form-floating mb-3">
                                <input onChange={this.handleChangeVIN} value={this.state.VIN} placeholder="VIN" required type="text" name="VIN" id="VIN" className="form-control" />
                                <label htmlFor="VIN">VIN</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleChangeCustomer} value={this.state.customer} placeholder="customer" required type="text" name="customer" id="customer" className="form-control" />
                                <label htmlFor="customer">Customer</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleChangeDate} value={this.state.date} placeholder="date" required type="text" name="date" id="date" className="form-control" />
                                <label htmlFor="date">Date and Time</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleChangeTechnician} value={this.state.technician} placeholder="technician" required type="text" name="technician" id="technician" className="form-control" />
                                <label htmlFor="date">Technician</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input onChange={this.handleChangeReason} value={this.state.reason} placeholder="reason" required type="text" name="reason" id="reason" className="form-control" />
                                <label htmlFor="reason">Reason</label>
                            </div>
                            <button className="btn btn-primary">Add</button>
                        </form>
                  

                    </div>
                </div>
            </div>
        );
    }
}

export default ServiceHistory;
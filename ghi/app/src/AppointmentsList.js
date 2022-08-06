import React from "react";

class AppointmentList extends React.Component {
    constructor(props) {
        super(props) 
        this.state = {
            appointments: [],
        }
    }

    async getAppointments() {
        const autoURL = 'http://localhost:8080/api/service_appointments'
        try {
            const autoResponse = await fetch(autoURL);
            if (autoResponse.ok) {
                const autoData = await autoResponse.json()
                console.log("Junk", autoData)
                this.setState({
                    appointments: autoData.appts,
                })
            } else {
                console.log("something here")
            }
        } catch (e) {
            console.error(e);
        }
    }

    async componentDidMount() {
        this.getAppointments();
    }

    render() {
        return (
            <React.Fragment>
                <h2 className="display-5 fw-bold">Service Appointments</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>VIN</th>
                            <th>Customer Name</th>
                            <th>Date and Time</th>
                            <th>Assigned Technician</th>
                            <th>Reason</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.appointments.map(appointment => {
                            return (
                                <tr key={appointment.vin}>
                                    <td>{appointment.customer_name}</td>
                                    <td>{appointment.date.split("T")[0]}</td>
                                    <td>{appointment.time.split("T")[1].slice(0, 5)}</td>
                                    <td>{appointment.technician.name}</td>
                                    <td>{appointment.reason}</td>
                                    {/* <td>{(appointment.vip)? "False" :"True"}</td>
                                    <td>{appointment.status}</td> */}
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
            </React.Fragment>
        );
    }
}

export default AppointmentList
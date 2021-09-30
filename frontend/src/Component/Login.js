import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import {Card, Button, Form} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';



class Login extends Component {
	constructor(props) {
		super(props);

		this.state = {
			username: "",
			password: "",
			buttonState: "inactive",
			userID: "",
		};

		this.handleSubmit = this.handleSubmit.bind(this);
		this.handleChange = this.handleChange.bind(this);
	}

	handleChange(event, stateName) {
		if (stateName === "username") {
			this.setState({ username: event.target.value });
		} else {
			this.setState({ password: event.target.value });
		}

		if (this.state.username != "" && this.state.password != "") {
			this.setState({ buttonState: "active" });
		}
		console.log(this.state);
	}

	handleSubmit(event) {
		fetch("/login", {
			method: "POST",
			headers: {
			  "SECRET_KEY": "",
			},
			body: JSON.stringify({
				username: this.state.username,
				password: this.state.password,
			}),
		})
			.then((response) => response.json())
			.then((data) => {
				this.setState({ userID: data.ID });
				console.log(data);
				this.props.history.push({
					pathname: "/home",
					state: { custID: data.ID, firstName: data.firstName },
				});
			});
	}

	render() {
		return (
			<div className="login-page" 
            style={{display: 'flex', justifyContent: 'center', alignItems: 'center',margin:'10pt'}}>
                
                <Card bg="light" style={{height: "25em", width: "25%"}}>
                    <Card.Body style={{paddingTop: "50px"}}>
                        <Card.Title>Login</Card.Title>
                        <div style={{height: "20px"}}/>
                        <Form style={{textAlign: "center"}}>
                            <Form.Label>Username</Form.Label>
                            <Form.Control 
                                type="text" 
                                placeholder="Enter username"
                                onChange={e => {
                                    this.handleChange(e, "username");
                                }}
                                value={this.state.username}
                            />
                            <div style={{height: "20px"}}/>
                            <Form.Label>Password</Form.Label>
                            <Form.Control 
                                type="password" 
                                placeholder="Enter password"
                                onChange={e => {
                                    this.handleChange(e, "password");
                                }}
                                value={this.state.password}
                            />
                        </Form>
                        <label style={{'color': 'red'}}>
                                {this.state.error}
                        </label>
                        <br/>
                        <div style={{height: "20px"}}/>
                        <Button className="Button" variant="primary" onClick={this.handleSubmit}>
                            Login
                        </Button>
                    </Card.Body>
                </Card>
            </div>
        );
    }

}

export default withRouter(Login);
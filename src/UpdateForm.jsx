import React from 'react';


class UpdateForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        preffered_major: '',
        sat: '',
        act: '',
        gpa: '',
        school_size: '',
        location: '',
        pub_or_priv: '',
        wtp: '',
        username: ''
      };
      this.handleSubmit = this.handleSubmit.bind(this)
      this.myChangeHandler = this.myChangeHandler.bind(this)
    }
    

    myChangeHandler (e) {
      this.setState({
        [e.target.name]: e.target.value
      });
    }

    handleSubmit(event) {
      console.log('this happened')
      let state = this.state

  fetch('/st_update', {
    method: 'POST',
    body: JSON.stringify({
        "preffered_major" : state.preffered_major,
        "sat": state.sat,
        "act": state.act,
        "gpa" : state.gpa,
        "school_size": state.school_size,
        "location": state.location, 
        "pub_or_priv": state.pub_or_priv,
        "wtp": state.wtp,
        "username" : state.username
        })
  })
  console.log(this.state.username)
      event.preventDefault();
    }

    

    render() {
      return (
        <form onSubmit={this.handleSubmit}> 
        <h1>Hello!</h1>
        <p>Enter your username:</p>
        <input
          type='text'
          name='username'
          value = {this.state.username}
          onChange={this.myChangeHandler}
        />
        <p>Preffered Major:</p>
        <input
          type='text'
          name='preffered_major'
          value = {this.state.preffered_major}
          onChange={this.myChangeHandler}  
        />
        <p>Update your SAT Score:</p>
        <input
          type='text'
          name='sat'
          value = {this.state.sat}
          onChange={this.myChangeHandler}
        />
        <p>Update your ACT Score:</p>
        <input
          type='text'
          name='act'
          value = {this.state.act}
          onChange={this.myChangeHandler}
        />
        <p>Update your GPA:</p>
        <input
          type='text'
          name='gpa'
          value = {this.state.gpa}
          onChange={this.myChangeHandler}
        />
        <p>Update your preffered school size:</p>
        <input
          type='text'
          name='school_size'
          value = {this.state.school_size}
          onChange={this.myChangeHandler}  
        />
        <p>Update your preffered location:</p>
        <input
          type='text'
          name='location'
          value = {this.state.location}
          onChange={this.myChangeHandler}  
        />
         <p>Update if it is public or private:</p>
        <input
          type='text'
          name='pub_or_priv'
          value = {this.state.pub_or_priv}
          onChange={this.myChangeHandler}  
        />
         <p>Update your willingness to pay:</p>
        <input
          type='text'
          name='wtp'
          value = {this.state.wtp}
          onChange={this.myChangeHandler}  
        />
        <input type="submit" value="Submit" 
        /> 
        </form>
      );
    }
  }
  export default UpdateForm;
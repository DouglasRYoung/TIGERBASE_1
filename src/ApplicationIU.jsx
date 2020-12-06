import React from 'react';
//import ReactDOM from 'react-dom';
class ApplicationIU extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        preffered_major: 0,
        sat_score: 0,
        act_score: 0,
        gpa: 0,
        school_size: 0,
        location: 0,
        pub_or_priv: 0,
        wtp: 0,
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

  fetch('/at_insert', {
    method: 'POST',
    body: JSON.stringify({
        "preffered_major": state.preffered_major,
        "sat_score":state.sat_score,
        "act_score":state.act_score,
        "gpa":state.gpa,
        "school_size": state.school_size,
        "location_": state.location,
        "pub_or_priv": state.pub_or_priv,
        "willingness_topay":state.wtp,
        "username" : state.username
        })
  })
  console.log(this.state.preffered_major)
  console.log(this.state.username)

      event.preventDefault();
    }

    render() {
      return (
        <form onSubmit={this.handleSubmit}> 
        <h1>Create Application Ranking:</h1>
        <p>Enter your username:</p>
        <input
          type='text'
          name='username'
          value = {this.state.username}
          onChange={this.myChangeHandler}
        />
        <h2>(provide integer rank value for each category)</h2>
        <p>Enter preffered_major rank:</p>
        <input
          type='text'
          name='preffered_major'
          value = {this.state.preffered_major}
          onChange={this.myChangeHandler}
        />
        <p>Enter sat_score rank:</p>
        <input
          type='text'
          name='sat_score'
          value = {this.state.sat_score}
          onChange={this.myChangeHandler}
        />
        <p>Enter act_score rank:</p>
        <input
          type='text'
          name='act_score'
          value = {this.state.act_score}
          onChange={this.myChangeHandler}
        />
        <p>Enter GPA rank:</p>
        <input
          type='text'
          name='gpa'
          value = {this.state.gpa}
          onChange={this.myChangeHandler}
        />
        <p>Enter School Size rank:</p>
        <input
          type='text'
          name='school_size'
          value = {this.state.school_size}
          onChange={this.myChangeHandler}
        />
        <p>Enter Location rank:</p>
        <input
          type='text'
          name='location'
          value = {this.state.location}
          onChange={this.myChangeHandler}
        />
        <p>Enter Pub/Priv rank:</p>
        <input
          type='text'
          name='pub_or_priv'
          value = {this.state.pub_or_priv}
          onChange={this.myChangeHandler}
        />
        <p>Enter willingness_topay rank:</p>
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
  //preffered_major,sat_score,act_score,gpa,school_size,location_,pub_or_priv,willingness_topay,username
  export default ApplicationIU;
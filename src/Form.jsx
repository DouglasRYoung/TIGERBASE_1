import React from 'react';
//import ReactDOM from 'react-dom';
class Form extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        preffered_major: '',
        sat_score: '',
        act_score: '',
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
    //preffered_major,sat_score,act_score,gpa,school_size,location_,pub_or_priv,willingness_topay,username

   // myChangeHandler = (event) => {
    /*myChangeHandler(event){

      //let nam = event.target.name;
      let pm = event.target.value;
      let sat = event.target.sat_score;
      let act = event.target.act_score;
      let gpa = event.target.gpa;
      let size = event.target.school_size;
      let locale = event.target.location;
      let pubOrPriv = event.target.pub_or_priv;
      let WTP = event.target.wtp;
      let name = event.target.username;
      this.setState({pm, sat, act, gpa, size, locale, pubOrPriv, WTP, name});
    }*/


    myChangeHandler (e) {
      this.setState({
        [e.target.name]: e.target.value
      });
    }

    handleSubmit(event) {
      console.log('this happened')
      /*fetch('/st_insert').then(res => res.json()).then(data => {
        console.log(data)
        return data
      });*/
      let state = this.state

  fetch('/st_insert', {
    method: 'POST',
    body: JSON.stringify({
        //"key": state["key"],
        
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
        <h1>Hello!</h1>
        <p>Enter your preffered_major:</p>
        <input
          type='text'
          name='preffered_major'
          value = {this.state.preffered_major}
          onChange={this.myChangeHandler}
        />
        <p>Enter your sat_score:</p>
        <input
          type='text'
          name='sat_score'
          value = {this.state.sat_score}
          onChange={this.myChangeHandler}
        />
        <p>Enter your act_score:</p>
        <input
          type='text'
          name='act_score'
          value = {this.state.act_score}
          onChange={this.myChangeHandler}
        />
        <p>Enter your GPA:</p>
        <input
          type='text'
          name='gpa'
          value = {this.state.gpa}
          onChange={this.myChangeHandler}
        />
        <p>Enter your School Size:</p>
        <input
          type='text'
          name='school_size'
          value = {this.state.school_size}
          onChange={this.myChangeHandler}
        />
        <p>Enter your Location:</p>
        <input
          type='text'
          name='location'
          value = {this.state.location}
          onChange={this.myChangeHandler}
        />
        <p>Enter your Pub/Priv:</p>
        <input
          type='text'
          name='pub_or_priv'
          value = {this.state.pub_or_priv}
          onChange={this.myChangeHandler}
        />
        <p>Enter your willingness_topay:</p>
        <input
          type='text'
          name='wtp'
          value = {this.state.wtp}
          onChange={this.myChangeHandler}
        />
        <p>Enter your username:</p>
        <input
          type='text'
          name='username'
          value = {this.state.username}
          onChange={this.myChangeHandler}
        />
        <input type="submit" value="Submit" 
        /> 
        </form>
      );
    }
  }
  //preffered_major,sat_score,act_score,gpa,school_size,location_,pub_or_priv,willingness_topay,username
  export default Form;
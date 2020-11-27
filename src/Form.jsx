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
    }
    //preffered_major,sat_score,act_score,gpa,school_size,location_,pub_or_priv,willingness_topay,username

    myChangeHandler = (event) => {
      //let nam = event.target.name;
      let pm = event.target.preffered_major;
      let sat = event.target.sat_score;
      let act = event.target.act_score;
      let gpa = event.target.gpa;
      let size = event.target.school_size;
      let locale = event.target.location;
      let pubOrPriv = event.target.pub_or_priv;
      let WTP = event.target.wtp;
      let name = event.target.username;
      this.setState({pm, sat, act, gpa, size, locale, pubOrPriv, WTP, name});
    }

    handleSubmit(event) {
      //alert('A name was submitted: ' + this.state.value);
      console.log('this happened')
      /*fetch('/st_insert').then(res => res.json()).then(data => {
        console.log(data)
        return data
      });*/
      fetch("/st_insert", {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/json",
        },
        body:JSON.stringify(this.state)
        }
    ).then(response => {

    return response.json()
  })

      event.preventDefault();
    }

    

    render() {
      return (
        <form onSubmit={this.handleSubmit}> 
        <h1>Hello!</h1>
        <p>Enter your preffered_major:</p>
        <input
          type='text'
          name='Preffered Major'
          onChange={this.myChangeHandler}
        />
        <p>Enter your sat_score:</p>
        <input
          type='text'
          name='SAT Score'
          onChange={this.myChangeHandler}
        />
        <p>Enter your act_score:</p>
        <input
          type='text'
          name='ACT Score'
          onChange={this.myChangeHandler}
        />
        <p>Enter your GPA:</p>
        <input
          type='text'
          name='GPA'
          onChange={this.myChangeHandler}
        />
        <p>Enter your School Size:</p>
        <input
          type='text'
          name='School Size'
          onChange={this.myChangeHandler}
        />
        <p>Enter your Location:</p>
        <input
          type='text'
          name='Location'
          onChange={this.myChangeHandler}
        />
        <p>Enter your Pub/Priv:</p>
        <input
          type='text'
          name='Pub/Priv'
          onChange={this.myChangeHandler}
        />
        <p>Enter your willingness_topay:</p>
        <input
          type='text'
          name='WTP'
          onChange={this.myChangeHandler}
        />
        <p>Enter your username:</p>
        <input
          type='text'
          name='username'
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
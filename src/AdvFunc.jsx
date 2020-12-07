import React from 'react';


class AdvFunc extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          username: '',
          colleges: []
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
  
    fetch('/adv_func', {
      method: 'POST',
      body: JSON.stringify({
          "username" : state.username
          })
    }).then(res => res.json()).then(data => {
      console.log(data)
      this.setState({colleges: data})
    });
    //console.log(this.state.username)
        event.preventDefault();
      }
  
      render() {
        return (
          <form onSubmit={this.handleSubmit}> 
          <h1>See Your Best Fit Colleges:</h1>
          
          <p>Enter your username:</p>
          <input
            type='text'
            name='username'
            value = {this.state.username}
            onChange={this.myChangeHandler}
          />
          <input type="submit" value="Submit" 
          /> 
          <p>Your Top 3 Schools: <br />
             #1: {this.state.colleges[0]} <br />
             #2: {this.state.colleges[1]} <br /> 
             #3: {this.state.colleges[2]} <br />  
          </p> 
          </form>
        );
      }
    }
  export default AdvFunc;
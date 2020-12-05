import React from 'react';


class CostComparison extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
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

  fetch('/ct_cost', {
    method: 'POST',
    body: JSON.stringify({
        "username" : state.username
        })
  })
  console.log(this.state.username)
      event.preventDefault();
    }

    render() {
      return (
        <form onSubmit={this.handleSubmit}> 
        <h1>Find University Based On Location:</h1>
        
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
  export default CostComparison;
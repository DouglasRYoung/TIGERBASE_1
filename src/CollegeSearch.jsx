import React from 'react';

class CollegeSearch extends React.Component {

    constructor(props) {
      super(props);
      this.state = {
        lookUp: '',
        college: [] 
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
      //let state = this.state
      fetch('/ct_get', {
        method: 'POST',
        body: JSON.stringify({
            "lookUp" : this.state.lookUp
            })
      }).then(res => res.json()).then(data => {
        console.log(data)
        this.setState({college: data})
      });
      //console.log(this.state.username)
      event.preventDefault();
    }

    

    render() {
      return (
        <form onSubmit={this.handleSubmit}> 
        <h1>College Search:</h1>
        
        <p>Enter College name:</p>
        <input
          type='text'
          name='lookUp'
          value = {this.state.lookUp}
          onChange={this.myChangeHandler}
        />
        <input type="submit" value="Submit" 
        />
        <p>College: {this.state.college[1]} <br /> 
           Majors: {this.state.college[2]} <br /> 
           SAT Avg: {this.state.college[3]} <br /> 
           ACT Avg: {this.state.college[4]} <br /> 
           GPA Avg: {this.state.college[5]} <br /> 
           Population: {this.state.college[6]} <br /> 
           Location: {this.state.college[7]} <br /> 
           Type: {this.state.college[8]} <br /> 
           Tuition: ${this.state.college[9]}
        </p> 
        </form>
      );
    }
  }
  export default CollegeSearch;
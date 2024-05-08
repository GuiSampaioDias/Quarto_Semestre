import React from 'react'

class NameForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {value: ''};
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      console.log(event.target.value);
      this.setState({value: event.target.value});
    }
  
    handleSubmit(event) {
     
      event.preventDefault();
      window.location.href = "https://www.google.com/search?q=" + this.state.value;    

    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Valor:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Enviar" />
        </form>
      );
    }
  }
  export default NameForm;
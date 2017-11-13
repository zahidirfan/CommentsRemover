import React, { Component } from 'react';
import './App.css';
import './pygments.css';

class SnippetForm extends Component {

    constructor (props){
      super(props);
      this.state = {
        snippets: [],
        snippet : []
      };
      this.handleChange.bind(this);
    }
    componentDidMount() {
      fetch('snippets/')
        .then(res => res.json())
        .then(snippets => this.setState({ snippets }));
    }

    handleChange(e){
      var index = e.target.value;
      console.log(index);
      fetch('snippets/highlight/'+ index)
        .then(res => res.json()
      )
        .then (snippet => this.setState({snippet})
      )
    }

    render() {
      return (
        <div className="col-sm-8">
            select snippet : <select onChange= {this.handleChange.bind(this)}> options={this.state.snippets.map(snippet =>  <option value = {snippet.id}> {snippet.id}</option>)}</select>
            <div className='col-sm-4' dangerouslySetInnerHTML={{
                   __html: this.state.snippet.code
                 }}/>
             <div className='col-sm-4'dangerouslySetInnerHTML={{
                    __html: this.state.snippet.code
                  }}/>
       </div>
      );
    }
  }

  export default SnippetForm;

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
      var index = document.getElementById("snippet-index").value;
      var comments = document.getElementById('comments').checked;

      if (comments === false) {
        fetch('snippets/highlight/'+ index)
          .then(res => res.json()
        )
          .then (snippet => this.setState({snippet})
        )
      } else {
        fetch('snippets/nocomments/'+ index)
          .then(res => res.json()
        )
          .then (snippet => this.setState({snippet})
        )
      }
    }

    render() {
      return (
        <div className="col-sm-12">
            select snippet : <select id="snippet-index" onChange= {this.handleChange.bind(this)}> options={this.state.snippets.map(snippet =>  <option value = {snippet.id}> {snippet.id}</option>)}</select>
            comments : <input id="comments" type="checkbox" onChange= {this.handleChange.bind(this)}/>
            <div align="left" className='col-sm-6' dangerouslySetInnerHTML={{
                   __html: this.state.snippet.code
                 }}/>
       </div>
      );
    }
  }

  export default SnippetForm;

import React, { Component } from 'react';
import './App.css';
import './pygments.css';

class AnalysisForm extends Component {

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

    handleChange(){
      var code = document.getElementById("code").value;

      fetch('snippets/highlight/')
        .then(res => res.json()
      )
        .then (snippet => this.setState({snippet})
      )
    }

    render() {
      return (
        <div className="row">
            <div align='left' className="col-sm-8">
              <label align='left' for='code'>Please paste your code and press analysis button</label>
              <textarea class="form-control" rows="15" id="code"></textarea>
              <input id="analysis" value= "Analysis" type="button" onChange= {this.handleChange.bind(this)}/>
            </div>
            <div id="analysis-result"></div>
       </div>
      );
    }
  }

  export default AnalysisForm;

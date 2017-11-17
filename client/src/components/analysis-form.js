import React, { Component } from 'react';
import './App.css';
import './pygments.css';

class AnalysisForm extends Component {

    constructor (props){
      super(props);
      this.state = {
        language : 'default'
      }

      this.handleChange.bind(this);
    }
    componentDidMount() {

    }

    handleChange(){
      var code = document.getElementById("code").value;
      // TODO : Need to add code to analyse the code and return language

      fetch("/analyse_code/",
      {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          method: "POST",
          body: JSON.stringify({'code': code})
      })
        .then(function(res){
            console.log(res);
            
        })
        .catch(function(res){ console.log(res) })
    }

    render() {
      return (
        <div className="row">
            <div align='left' className="col-sm-8">
              <label align='left' for='code'>Please paste your code and press analysis button</label>
              <textarea class="form-control" rows="15" id="code"></textarea>
              <input id="analysis" value= "Analysis" type="button" onClick= {this.handleChange.bind(this)}/>
            </div>
            <div id="analysis-result"></div>
       </div>
      );
    }
  }

  export default AnalysisForm;

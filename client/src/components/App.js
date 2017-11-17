import React, { Component } from 'react';
import './App.css';
import SnippetForm from './snippet-form';
import AnalysisForm from './analysis-form';
import {BrowserRouter, Route, Link } from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <header className="App-header">
            <h1 className="App-title"> xComment.io</h1>
          </header>
          <div class="row">
           <div class="col-sm-2"> <Link to="/">Home</Link></div>
           <div class="col-sm-2"><Link to="/analyse">Analyse Code</Link></div>
          </div>

          <Route exact={true} path="/" component = {SnippetForm}/>
          <Route path="/analyse" component = {AnalysisForm}/>

        </div>
      </BrowserRouter>
    );
  }
}

export default App;

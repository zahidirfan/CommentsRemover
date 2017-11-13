import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import SnippetForm from './snippet-form';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title"> xComment.io</h1>
        </header>
        <SnippetForm/>

      </div>
    );
  }
}

export default App;

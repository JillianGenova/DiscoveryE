import React, { Component } from 'react';
import { useLocation } from "react-router-dom";


function Search() {
    const location = useLocation();
    return <h2>{location.state.params}</h2>;
}

// exporting home component for other files to use
export default Search
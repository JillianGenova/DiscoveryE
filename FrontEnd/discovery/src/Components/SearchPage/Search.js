import React, { Component } from 'react';
import { useLocation } from "react-router-dom";
import "./Search.css"

const Search = () => {
    const location = useLocation();

    return (
        //<h2>{location.state.params}</h2>
        <div>
            <div class="topnav">
                <a class="active" href="#home">Home</a>
            </div>
            <div class="sidebar">
                <a class="active" href="#home">Home</a>
            </div>
        </div>

    );
}

export default Search
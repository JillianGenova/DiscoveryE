import React, { Component, useState } from 'react';
import { useLocation } from "react-router-dom";
import axios from 'axios';


function Search() {
    const location = useLocation();
    const [currentTime, setCurrentTime] = useState(0);
    const [msg, setMsg] = useState('');

    var myParams = {
        data: location.state.params
    }

    axios.post('http://localhost:3000/search', {location})
            .then(function(response){
                console.log(response);
                setMsg(response.data)
       //Perform action based on response
        })
        .catch(function(error){
            console.log(error);
       //Perform action based on error
        });


    //fetch('/time').then(res => res.json()).then(data => {
      //  setMsg(data.time);
    //});

    return <h2>The current time is {msg}.</h2>;
}

// exporting home component for other files to use
export default Search
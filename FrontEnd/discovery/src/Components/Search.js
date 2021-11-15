import React, { Component, useState } from 'react';
import { useLocation } from "react-router-dom";


function Search() {
    const location = useLocation();
    const [currentTime, setCurrentTime] = useState(0);
    const [msg, setMsg] = useState('');

    fetch('/search',{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body: JSON.stringify({'msg': location.state.params})
    });

    fetch('/time').then(res => res.json()).then(data => {
        setMsg(data.time);
    });

    return <h2>The current time is {msg}.</h2>;
}

// exporting home component for other files to use
export default Search
import React from 'react';
import "./Marker.css"

const Marker = ({ text }) => {
    return(
    <div className="MarkerStyle">
        <span class="markertooltiptext"> {text} </span>
    </div>
);
}

export default Marker;
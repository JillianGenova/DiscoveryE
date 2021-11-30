import React from 'react';
import './BusinessButton.css';

const BusinessButton = ({ text }) => {

    return (
        <>
            <button
                className="businessButton"
                id={`button-${text}`}
            >
                {text}
                <span class="tooltiptext">Tooltip text</span>
            </button>
        </>
    )
}

export default BusinessButton;
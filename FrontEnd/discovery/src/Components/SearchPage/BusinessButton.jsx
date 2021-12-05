import React from 'react';
import './BusinessButton.css';

const BusinessButton = ({ text }) => {

    return (
        <>
            <button
                className="businessButton"
                id={`button-${text}`}
            >
                <span> 
                    {text}
                    <br />
                    {text}
                </span>
            </button>
        </>
    )
}

export default BusinessButton;
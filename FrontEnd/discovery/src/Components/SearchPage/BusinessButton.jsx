import React from 'react';
import './BusinessButton.css';

const BusinessButton = ({ text, onClick, checked }) => {

    return (
        <>
            <button
                className="businessButton"
                id={`button-${text}`}
            >
                {text}
            </button>
        </>
    )
}

export default BusinessButton;
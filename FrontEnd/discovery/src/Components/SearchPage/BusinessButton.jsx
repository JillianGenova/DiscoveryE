import React from 'react';
import './BusinessButton.css';

const BusinessButton = ({ business }) => {

    return (
        <>
            <button
                className="businessButton"
                id={`button-${business.name}`}
            >
                <span className='businessName'> {business.name} </span>
                <br />
                <span className='businessAddress'> {business.location.address} </span>
                <br />
                <a className='businessUrl' href={business.url}> Website </a>
                
            </button>
        </>
    )
}

export default BusinessButton;
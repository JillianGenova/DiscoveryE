import React from 'react';
import './StyledButton.css';

const StyledButton = ({ text, onClick, checked }) => {

    return (
        <>
            <button
                type='checkbox'
                id={`button-${text}`}
                onClick={() => onClick()}
                checked={!!checked}
                className={checked ? 'selectedClass' : 'unselectedClass'}
            >
                {text}
            </button>
        </>
    )
}

export default StyledButton;
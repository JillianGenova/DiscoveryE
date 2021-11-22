import React from 'react';
import "./Marker.css"

// const Wrapper = styled.div`
//   position: absolute;
//   top: 50%;
//   left: 50%;
//   width: 18px;
//   height: 18px;
//   background-color: #000;
//   border: 2px solid #fff;
//   border-radius: 100%;
//   user-select: none;
//   transform: translate(-50%, -50%);
//   cursor: ${(props) => (props.onClick ? 'pointer' : 'default')};
//   &:hover {
//     z-index: 1;
//   }
// `;


const Marker = ({ text, onClick }) => {
    return(
    <div
        className="MarkerStyle"
        alt={text}
        onClick={onClick}
    />
);
}

export default Marker;